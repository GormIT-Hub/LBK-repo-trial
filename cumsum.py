import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from collections import defaultdict

#import glob

def get_lengths(path):

    csvs = list(path.iterdir())
    results_csvs = list(filter(lambda csv: csv.name[:2] == 'CL', csvs)) 
    lens_dict = {}

    for csv in results_csvs:
        traj = csv.name
        try: 
            df = pd.read_csv(csv)
            length = df['traj_len'].iloc[0]
            lens_dict[traj.replace('CLEANED-', '')] = length
        except pd.errors.EmptyDataError:
            print(f'Empty dataframe for traj {traj}')
            continue

    return lens_dict


def get_channel_df(protein:str):
    
    path_to_results = Path(fr'/Users/jancagalj/Work/LBK/MD/Proteins/Results-all/{protein}/RESULTS/Channel/ions-all')
    path_to_candidates = Path(fr'/Users/jancagalj/Work/LBK/MD/Proteins/Results-all/{protein}/CANDIDATES/Channel/ions')

    lens_dict = get_lengths(path_to_candidates)
    dfs_dict = {}

    for result in list(path_to_results.iterdir()):
        try: 
            df = pd.read_csv(result) 
            df['traj_len'] = lens_dict[result.name]
            df['traj'] = result.name.replace(protein+'-', '')[:-4]
            dfs_dict[result.name] = df
        except pd.errors.EmptyDataError:
            print(f'Empty dataframe for traj {result.name}')
            continue

    return dfs_dict

def filtered_dict(dict_dfs: dict):

    d1 = defaultdict(list)
    
    for key in list(dict_dfs.keys()):
        if '2100' in key:
            d1['2100_dep'].append(dict_dfs[key]) if 'dep' in key else d1['2100_hyp'].append(dict_dfs[key])
        elif '1800' in key:
            d1['1800_dep'].append(dict_dfs[key]) if 'dep' in key else d1['1800_hyp'].append(dict_dfs[key])
        elif '1500' in key:
            d1['1500_dep'].append(dict_dfs[key]) if 'dep' in key else d1['1500_hyp'].append(dict_dfs[key])

    return d1

def select_ion(protein: str) -> str:
    if protein in ('Nav1.5', 'Cav1.1'):
        return 'CLA' #return 'CLA'
    elif protein == 'BK':
        return 'POT' #return 'CLA'
    else:
        raise ValueError(f"Unknown protein: {protein}")
"""
def plot_cumulative(df: pd.DataFrame, 
                    length0,
                    protein: str, 
                    ax
    ) -> None:

    ion = select_ion(protein)
    
    df_ion = df[df['type'] == ion].copy()

    if df_ion.empty:
        return

    df_ion = df_ion.sort_values("frame")

    # Count events per frame
    counts_per_frame = df_ion.groupby("frame").size()
    cumulative = counts_per_frame.cumsum()
    #print(cumulative)
    #print(cumulative.max())

    length = df['traj_len'].iloc[0]

    # Anchor start at frame 0 and end at traj_len
    cumulative.loc[0] = 0
    #cumulative.loc[length0] = cumulative.max()
    cumulative = cumulative.sort_index()

    # Step plot
    ax.step(
        cumulative.index,
        cumulative.values,
        where="post",
        label=df['traj'].iloc[0],
        alpha=0.8,
        linewidth=1.9
    )
    return cumulative.max()

def plot_cumsum_channel(protein: str):

    d = get_channel_df(protein)
    d_filtered = filtered_dict(d)
    print(d_filtered) # key je simulacija, value je df
    
    for key in list(d_filtered.keys()):
        fig, ax = plt.subplots(figsize=(8, 5))
        longest = max(df['traj_len'].iloc[0] for df in d_filtered[key])
        print(d_filtered[key][0]['traj_len'].iloc[0])
        vals = sorted(d_filtered[key], key=lambda df: int(df['traj'].iloc[0][-1]))
        for val in vals:
            maxVal = plot_cumulative(
                    val,
                    d_filtered[key][0]['traj_len'].iloc[0],
                    protein,
                    ax=ax
            )
            print(maxVal)

        ax.set_xlabel("frame")
        ax.set_ylabel(f"število ionov")
        ax.legend(fancybox = False, frameon=True, facecolor='white', edgecolor='k', framealpha=0.5)
        ax.grid(True, alpha = 0.5, linestyle=':')
        plt.tight_layout()
        #plt.savefig(f'{protein}-{TMVs[0]}-{polarities[0]}.png', dpi=300, bbox_inches='tight')
    
    plt.show()
"""
def plot_cumulative(df: pd.DataFrame, 
                    protein: str, 
                    ax,
                    stride: float = 0.01 # Adjust this to your ns/frame (e.g., 0.1)
    ) -> float:

    ion = select_ion(protein)
    df_ion = df[df['type'] == ion].copy()
    
    # Get the actual end of the simulation for this specific trajectory
    traj_end_frame = int(df['traj_len'].iloc[0])

    if df_ion.empty:
        # If no ions, draw a flat line at 0 from start to traj_len
        ax.step([0, traj_end_frame * stride], [0, 0], where="post", 
                label=df['traj'].iloc[0], alpha=0.8, linewidth=1.9)
        return 0.0

    df_ion = df_ion.sort_values("frame")

    # Count events per frame and calculate cumulative sum
    counts_per_frame = df_ion.groupby("frame").size()
    cumulative = counts_per_frame.cumsum()

    # --- EXTENSION LOGIC ---
    # 1. Ensure the plot starts at frame 0
    if 0 not in cumulative.index:
        cumulative.loc[0] = 0
    
    # 2. Force the curve to continue until traj_len
    # This creates the "straight line" from the last event to the end
    total_ions = cumulative.max()
    cumulative.loc[traj_end_frame] = total_ions
    
    # Sort index to ensure 0 is first and traj_end is last
    cumulative = cumulative.sort_index()

    # Convert frames to nanoseconds for the x-axis
    time_ns = cumulative.index * stride

    # Step plot ('where=post' ensures the vertical jump happens at the frame of the event)
    ax.step(
        time_ns,
        cumulative.values,
        where="post",
        label=df['traj'].iloc[0],
        alpha=0.8,
        linewidth=1.9
    )

    return total_ions

def plot_cumsum_channel(protein: str, stride: float = 0.01):
    d = get_channel_df(protein)
    d_filtered = filtered_dict(d)
    
    for key in d_filtered.keys():
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Sort trajectories by the numeric ID at the end of the name
        vals = sorted(d_filtered[key], key=lambda df: int(df['traj'].iloc[0][-1]))
        
        for val in vals:
            plot_cumulative(
                val,
                protein,
                ax=ax,
                stride=stride
            )

        #ax.set_title(f"Cumulative Permeation: {protein} ({key})")
        ax.set_xlabel("t (ns)")
        ax.set_ylabel("število ionov")
        ax.legend(fancybox=False, frameon=True, facecolor='white', 
                  edgecolor='k', framealpha=0.5, loc='upper left')
        ax.grid(True, alpha=0.3, linestyle=':')
        plt.tight_layout()

        plt.savefig(f'{protein}-{key}-cumsum-cla.png', dpi=300, bbox_inches='tight')
    
    plt.show()
# plot_cumsum_vsd -> 
# mogoče za vsako napetost in za vsak run pri dep oz. hyp -> en 2x2 subplot
# pol pa splotaš skozi vsak VSD kaj se dogaja in dodaš v zgornji desni rob (oz pač nekam) lokacijo nastanka pore 
# ta inset maš lokacijo nastanka pore ubistvu scatter plot proteina, označeni vsdji in pol mean coordinate of the two P atoms kot nek križec gor
# naredi še kodo da prepozna poro v lipidni domeni -> ne komplicirat, postopek roughly nasledn:
# 1. razparceliraj membrano in ziteriraj skozi vse kose
# 2. v vsaki parceli shrani kolko p atomov je blo v sredini te parcele (tle se moreš odločit al je boljše imet en COM za celo membrano al enga za vsako parcelo)
# 3. poglej če v kaki parceli dve p glavi oz če v neghbouring 2 (1 v vsaki)
# 3.1 če 2 glavi ustavi (poglej še če isto drži čez nek interval - verjetno moreš upoštevat tudi neighbouring cells); zanimiv pogoj b biu tudi če začnejo pol na tistem mestu ioni prehajt
# 3.2 če 1 v vsaki poglej če je njuna razdalja dovolj majhna da so pač blizu (nevem kako bi smiselno to izbrau) - kriterij iz 3.1 bi mogu tudi veljat
# 4. vrni čase pomoje če vse ok drugače nadaljuj



if __name__ == '__main__':

    plot_cumsum_channel('Nav1.5')
    