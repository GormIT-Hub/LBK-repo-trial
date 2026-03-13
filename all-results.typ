#set page(
  paper: "a4",
  margin: (x: .5cm, y: .5cm),
)
#set text(
  font: "New Computer Modern",
  size: 11pt
)

#set par(
  first-line-indent: 2em,
  spacing: 0.5em,
  justify: true,
  leading: 0.5em
)

#show math.equation: set text(font: "New Computer Modern Math", weight: "regular", size: 11pt) // put this back to 11pt after this document
#set math.equation(numbering: "(1)", supplement: [])

#align(center)[#image("tabele-lokacijePor.pdf", width: 90%)]
#align(center)[#image("ratio_of_poreLocations.png", width: 100%)]

= Nav1.5

#let nav = csv("poration-times/all/Nav1.5_all.csv")

#align(center)[
  #table(
  columns: 4,
  ..for (trajectory,frame,resids,check) in nav {
    (trajectory,frame,resids,check)
  }
)
  #image("Nav1.5-locations.png", width: 80%)
]
#v(8em)
== Cumulative sum -- channel
+ #underline[*SOD ions*]
#grid(
  columns: (1fr, 1fr), // 2 parts text, 1 part image
  column-gutter: 5pt,
  [
    #align(center + horizon)[
      #figure(
        image("plots/cumsum-channel/Nav1.5-2100_dep-cumsum-sod.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/Nav1.5-1800_dep-cumsum-sod.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    ),
    #figure(
        image("plots/cumsum-channel/Nav1.5-1500_dep-cumsum-sod.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    )
    ]
  ],
  [
    #align(center + horizon)[
      #figure(
        image("plots/cumsum-channel/Nav1.5-2100_hyp-cumsum-sod.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/Nav1.5-1800_hyp-cumsum-sod.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/Nav1.5-1500_hyp-cumsum-sod.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
    )
    ]
  ],
)
#v(16em)
2. #underline[*CLA ions*]
#grid(
  columns: (1fr, 1fr), // 2 parts text, 1 part image
  column-gutter: 5pt,
  [
    #align(center + horizon)[
      #figure(
        image("plots/cumsum-channel/Nav1.5-2100_dep-cumsum-cla.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/Nav1.5-1800_dep-cumsum-cla.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    ),
    #figure(
        image("plots/cumsum-channel/Nav1.5-1500_dep-cumsum-cla.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    )
    ]
  ],
  [
    #align(center + horizon)[
      #figure(
        image("plots/cumsum-channel/Nav1.5-2100_hyp-cumsum-cla.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/Nav1.5-1800_hyp-cumsum-cla.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/Nav1.5-1500_hyp-cumsum-cla.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
      )
    ]
  ],
)
#v(16em)
== Cumulative sum -- VSDs
#grid(
  columns: (1fr, 1fr),
  column-gutter: 0pt,
  [
    //#align(center)[#underline[*SOD ions*]]
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 2.5pt,
      [
      #align(center + horizon)[
        #figure(
            image("plots/cumsum-vsds/Nav1.5-2100_dep-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        ),
        #figure(
            image("plots/cumsum-vsds/Nav1.5-1800_dep-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        ),
        #figure(
            image("plots/cumsum-vsds/Nav1.5-1500_dep-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        ),
        ]
      ],
      [
      #align(center + horizon)[
        #figure(
        image("plots/cumsum-vsds/Nav1.5-2100_hyp-sod.png", width: 100%),
        caption: [*SOD ions*],
        supplement: [Slika]
        ),
        #figure(
            image("plots/cumsum-vsds/Nav1.5-1800_hyp-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        ),
         #figure(
            image("plots/cumsum-vsds/Nav1.5-1500_hyp-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        ),
        ]
      ]
    )
  ],
  [//#align(center)[#underline[*CLA ions*]]
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 2.5pt,
      [
      #align(center + horizon)[
        #figure(
            image("plots/cumsum-vsds/Nav1.5-2100_dep-cla.png", width: 100%),
            caption: [*CLA ions*],
            supplement: [Slika]
        ),
         #figure(
            image("plots/cumsum-vsds/Nav1.5-1800_dep-cla.png", width: 100%),
            caption: [*CLA ions*],
            supplement: [Slika]
        ),
        #figure(
            image("plots/cumsum-vsds/Nav1.5-1500_dep-cla.png", width: 100%),
            caption: [*CLA ions*],
            supplement: [Slika]
        ),
        ]
      ],
      [
      #align(center + horizon)[
        #figure(
        image("plots/cumsum-vsds/Nav1.5-2100_hyp-cla.png", width: 100%),
          caption: [*CLA ions*],
          supplement: [Slika]
        ),
        #figure(
        image("plots/cumsum-vsds/Nav1.5-1800_hyp-cla.png", width: 100%),
          caption: [*CLA ions*],
          supplement: [Slika]
        ),
        #figure(
        image("plots/cumsum-vsds/Nav1.5-1500_hyp-cla.png", width: 100%),
          caption: [*CLA ions*],
          supplement: [Slika]
        ),
        ]
      ]
    )
  ]
)

#v(30em)
= Cav1.1
#let cav = csv("poration-times/all/Cav1.1_all.csv")

#align(center)[
  #table(
  columns: 4,
  ..for (trajectory,frame,resids,check) in nav {
    (trajectory,frame,resids,check)
  }
)
  #image("Cav1.1-locations.png", width: 80%)
]

#v(10em)
== Cumulative sum -- channel
No activity through the channel.

== Cumulative sum -- VSDs

#grid(
  columns: (1fr, 1fr),
  column-gutter: 0pt,
  [
    //#align(center)[#underline[*SOD ions*]]
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 2.5pt,
      [
      #align(center + horizon)[
        #figure(
            image("plots/cumsum-vsds/Cav1.1-2100_dep-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        ),
        #figure(
            image("plots/cumsum-vsds/Cav1.1-1800_dep-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        ),
        #figure(
            image("plots/cumsum-vsds/Cav1.1-1500_dep-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        )
        ]
      ],
      [
      #align(center + horizon)[
        #figure(
        image("plots/cumsum-vsds/Cav1.1-2100_hyp-sod.png", width: 100%),
        caption: [*SOD ions*],
        supplement: [Slika]
        ),
        #figure(
            image("plots/cumsum-vsds/Cav1.1-1800_hyp-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        ),
         #figure(
            image("plots/cumsum-vsds/Cav1.1-1500_hyp-sod.png", width: 100%),
            caption: [*SOD ions*],
            supplement: [Slika]
        )
        ]
      ]
    )
  ],
  [//#align(center)[#underline[*CLA ions*]]
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 2.5pt,
      [
      #align(center + horizon)[
        #figure(
            image("plots/cumsum-vsds/Cav1.1-2100_dep-cla.png", width: 100%),
            caption: [*CLA ions*],
            supplement: [Slika]
        ),
         #figure(
            image("plots/cumsum-vsds/Cav1.1-1800_dep-cla.png", width: 100%),
            caption: [*CLA ions*],
            supplement: [Slika]
        ),
        #figure(
            image("plots/cumsum-vsds/Cav1.1-1500_dep-cla.png", width: 100%),
            caption: [*CLA ions*],
            supplement: [Slika]
        )
        ]
      ],
      [
      #align(center + horizon)[
        #figure(
        image("plots/cumsum-vsds/Cav1.1-2100_hyp-cla.png", width: 100%),
          caption: [*CLA ions*],
          supplement: [Slika]
        ),
        #figure(
        image("plots/cumsum-vsds/Cav1.1-1800_hyp-cla.png", width: 100%),
          caption: [*CLA ions*],
          supplement: [Slika]
        ),
        #figure(
        image("plots/cumsum-vsds/Cav1.1-1500_hyp-cla.png", width: 100%),
          caption: [*CLA ions*],
          supplement: [Slika]
        )
        ]
      ]
    )
  ]
)

#v(30em)
= BK
#let moore = csv("poration-times/all/BK_all.csv")

#align(center)[
  #table(
  columns: 4,
  ..for (trajectory,frame,resids,check) in moore {
    (trajectory,frame,resids,check)
  }
)
 #image("BK-locations.png", width: 80%)
]
#v(12em)
== Cumulative sum -- channel
+ #underline[*POT ions*]
#grid(
  columns: (1fr, 1fr), // 2 parts text, 1 part image
  column-gutter: 5pt,
  [
    #align(center + horizon)[
      #figure(
        image("plots/cumsum-channel/BK-2100_dep-cumsum-pot.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/BK-1800_dep-cumsum-pot.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    )
    ]
  ],
  [
    #align(center + horizon)[
      #figure(
        image("plots/cumsum-channel/BK-2100_hyp-cumsum-pot.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/BK-1800_hyp-cumsum-pot.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
    )
    ]
  ],
)

2. #underline[*CLA ions*]
#grid(
  columns: (1fr, 1fr), // 2 parts text, 1 part image
  column-gutter: 5pt,
  [
    #align(center + horizon)[
      #figure(
        image("plots/cumsum-channel/BK-2100_dep-cumsum-cla.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/BK-1800_dep-cumsum-cla.png", width: 100%),
        caption: [Simulations under dep. TMV of 2.1 V],
        supplement: [Slika]
    )
    ]
  ],
  [
    #align(center + horizon)[
      #figure(
        image("plots/cumsum-channel/BK-2100_hyp-cumsum-cla.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
    ),
      #figure(
        image("plots/cumsum-channel/BK-1800_hyp-cumsum-cla.png", width: 100%),
        caption: [Simulations under hyp. TMV of 2.1 V],
        supplement: [Slika]
    )
    ]
  ],
)

== Cumulative sum -- VSDs


#grid(
  columns: (1fr, 1fr),
  column-gutter: 0pt,
  [
    #align(center)[#underline[*POT ions*]]
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 2.5pt,
      [
      #align(center + horizon)[
        #rect(height:50em),
        #figure(
            image("plots/cumsum-vsds/BK-1800_dep-pot.png", width: 100%),
            caption: [*POT ions*],
            supplement: [Slika]
        ),
        ]
      ],
      [
      #align(center + horizon)[
        #figure(
        image("plots/cumsum-vsds/BK-2100_hyp-pot.png", width: 100%),
        caption: [*POT ions*],
        supplement: [Slika]
        ),
        #figure(
            image("plots/cumsum-vsds/BK-1800_hyp-pot.png", width: 100%),
            caption: [*POT ions*],
            supplement: [Slika]
        ),
        ]
      ]
    )
  ],
  [#align(center)[#underline[*CLA ions*]]
    #grid(
      columns: (1fr, 1fr),
      column-gutter: 2.5pt,
      [
      #align(center + horizon)[
        #rect(height:50em),
         #figure(
            image("plots/cumsum-vsds/BK-1800_dep-cla.png", width: 100%),
            caption: [*CLA ions*],
            supplement: [Slika]
        ),
        ]
      ],
      [
      #align(center + horizon)[
        #figure(
        image("plots/cumsum-vsds/BK-2100_hyp-cla.png", width: 100%),
          caption: [*CLA ions*],
          supplement: [Slika]
        ),
        #figure(
        image("plots/cumsum-vsds/BK-1800_hyp-cla.png", width: 100%),
          caption: [*CLA ions*],
          supplement: [Slika]
        ),
        ]
      ]
    )
  ]
)

//#image("tabele-lokacijePor.pdf", width: 100%)