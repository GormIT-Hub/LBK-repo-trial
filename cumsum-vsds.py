import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict

# --- DATA LOADING FUNCTIONS ---

def get_lengths(path):
    """Parses simulation lengths from candidate CSVs."""
    csvs = list(path.iterdir())
    # Filter for cleaned files
    results_csvs = list(filter(lambda csv: csv.name[:2] == 'CL', csvs)) 
    lens_dict = {}

    for csv in results_csvs:
        traj = csv.name
        try: 
            df = pd.read_csv(csv)
            length = df['traj_len'].iloc[0]
            # Match naming convention for dict lookup
            lens_dict[traj.replace('CLEANED-', '')] = length
        except (pd.errors.EmptyDataError, KeyError, IndexError):
            print(f'Empty or malformed dataframe for traj {traj}')
            continue
    return lens_dict

def get_channel_df(protein: str, path_results: str, path_candidates: str):
    """Reads ion data and attaches simulation lengths."""
    path_to_results = Path(path_results)
    path_to_candidates = Path(path_candidates)

    lens_dict = get_lengths(path_to_candidates)
    dfs_dict = {}

    for result in list(path_to_results.iterdir()):
        if not result.name.endswith('.csv'): continue
        print(result)
        try: 
            df = pd.read_csv(result) 
            df['traj_len'] = lens_dict[result.name]
            # Extract run name (e.g., '1500_dep_1')
            df['traj'] = result.name.replace(protein+'-', '')[:-4]
            dfs_dict[result.name] = df
        except (pd.errors.EmptyDataError, KeyError):
            print(f'Skipping {result.name}: Missing length or empty data.')
            continue

    return dfs_dict

def filtered_dict(dict_dfs: dict):
    """Groups simulations by TMV and Polarity."""
    d1 = defaultdict(list)
    for key in dict_dfs.keys():
        if '2100' in key:
            tag = '2100_dep' if 'dep' in key else '2100_hyp'
        elif '1800' in key:
            tag = '1800_dep' if 'dep' in key else '1800_hyp'
        elif '1500' in key:
            tag = '1500_dep' if 'dep' in key else '1500_hyp'
        else:
            tag = 'other'
        d1[tag].append(dict_dfs[key])
    return d1

def select_ion(protein: str) -> str:
    """Returns the relevant ion type based on protein."""
    if protein in ('Nav1.5', 'Cav1.1'):
        return 'SOD'
    elif protein == 'BK':
        return 'CLA'
    else:
        return 'SOD' # Fallback

# --- PLOTTING FUNCTIONS ---

def plot_cumulative_by_region(df: pd.DataFrame, 
                             protein: str, 
                             region: str,
                             ax,
                             color: str,
                             stride: float) -> float:
    """Plots a single region's cumulative sum, extending to the end of the simulation."""
    ion = select_ion(protein)
    df_region = df[(df['type'] == ion) & (df['region'] == region)].copy()
    
    traj_end_frame = int(df['traj_len'].iloc[0])

    # If no ions in this region, plot a flat zero-line
    if df_region.empty:
        #ax.step([0, traj_end_frame * stride], [0, 0], where="post", 
        #        label=region, alpha=0.7, linewidth=1.5, color=color)
        return 0.0

    df_region = df_region.sort_values("frame")
    counts_per_frame = df_region.groupby("frame").size()
    cumulative = counts_per_frame.cumsum()

    # Add anchors for start and end
    if 0 not in cumulative.index:
        cumulative.loc[0] = 0
    
    total_ions = cumulative.max()
    cumulative.loc[traj_end_frame] = total_ions
    cumulative = cumulative.sort_index()

    time_ns = cumulative.index * stride

    ax.step(
        time_ns,
        cumulative.values,
        where="post",
        label=region,
        alpha=0.8,
        linewidth=1.9,
        color=color
    )
    return total_ions

def plot_cumsum_vsd_grid(protein: str, results_path: str, candidates_path: str, stride: float = 0.01):
    """Generates a 4x1 grid of subplots for each simulation group with independent legends."""
    d = get_channel_df(protein, results_path, candidates_path)
    d_filtered = filtered_dict(d)
    
    # Consistent colors for VSD regions
    region_colors = {
        'VSD1': '#1f77b4', 'VSD2': '#ff7f0e', 
        'VSD3': '#2ca02c', 'VSD4': '#d62728'
    }

    for group_key, simulations in d_filtered.items():
        if not simulations: continue
        
        # Based on your snippet: 4 rows, 1 column
        fig, axes = plt.subplots(4, 1, figsize=(4, 12), sharex=True)
        # axes = axes.flatten() # flattening not strictly needed for 4,1 but good for safety
        
        # Sort by run number (assumes last char of traj name is 1, 2, 3, or 4)
        try:
            vals = sorted(simulations, key=lambda df: int(df['traj'].iloc[0][-1]))
        except (ValueError, IndexError):
            vals = simulations 

        for i, run_df in enumerate(vals):
            if i >= 4: break 
            
            ax = axes[i]
            run_name = run_df['traj'].iloc[0]
            
            # --- LOCAL REGION CHECK ---
            # Instead of using simulations[0], we look at the specific dataframe for this run
            current_run_regions = sorted(run_df['region'].unique())
            
            for region in current_run_regions:
                plot_cumulative_by_region(
                    run_df, protein, region, ax, 
                    color=region_colors.get(region), stride=stride
                )

            ax.set_title(f"{run_name}", fontsize=10, fontweight='bold')
            ax.set_ylabel("število ionov")
            ax.grid(True, alpha=0.3, linestyle=':')
            
            # --- INDEPENDENT LEGEND FOR EVERY SUBPLOT ---
            ax.legend(
                fancybox=False, 
                frameon=True, 
                facecolor='white', 
                edgecolor='k', 
                framealpha=0.5, 
                loc='upper left',
                fontsize='small'
            )

            # Only set x-label on the bottom-most plot
            if i == 3:
                ax.set_xlabel("t (ns)")

        plt.tight_layout()
        
        # Save each group plot
        save_name = f"{protein}-{group_key}-cla.png"
        plt.savefig(save_name, dpi=300)
    
    plt.show()

# --- EXECUTION ---

if __name__ == "__main__":
    # SET YOUR PATHS HERE
    MY_PROTEIN = "BK" # or "BK", "Cav1.1"
    RESULTS_DIR = fr"/Users/jancagalj/Work/LBK/MD/Proteins/Results-all/{MY_PROTEIN}/RESULTS/VSDs/ions-all"
    CANDIDATES_DIR = f"/Users/jancagalj/Work/LBK/MD/Proteins/Results-all/{MY_PROTEIN}/CANDIDATES/VSDs/ions"

    plot_cumsum_vsd_grid(MY_PROTEIN, RESULTS_DIR, CANDIDATES_DIR, stride=0.01)