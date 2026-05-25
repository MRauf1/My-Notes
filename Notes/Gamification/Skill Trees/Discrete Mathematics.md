```mermaid
flowchart TD
    classDef completed fill:#FFD700,stroke:#FF8C00,stroke-width:4px,rx:10px,ry:10px,color:#000000,font-weight:bold;
    classDef incomplete fill:#1E293B,stroke:#64748B,stroke-width:3px,stroke-dasharray: 5 5,rx:10px,ry:10px,color:#CBD5E1;
    classDef prereq fill:#8A2BE2,stroke:#4B0082,stroke-width:4px,rx:10px,ry:10px,color:#FFFFFF,font-weight:bold;

    %% PREREQUISITES
    PRE_C1_1["[Precalc] 1.1 Sets of Real Numbers"]:::prereq
    PRE_C1_3["[Precalc] 1.3 Intro to Functions"]:::prereq
    PRE_C5_2["[Precalc] 5.2 Inverse Functions"]:::prereq
    PRE_C9_3["[Precalc] 9.3 Mathematical Induction"]:::prereq

    %% HTPI CHAPTER 1
    HTPI1_1[1.1 Deductive Reasoning and Logical Connectives]:::completed
    HTPI1_2[1.2 Truth Tables]:::completed
    HTPI1_3[1.3 Variables and Sets]:::completed
    HTPI1_4[1.4 Operations on Sets]:::completed
    HTPI1_5[1.5 The Conditional and Biconditional Connectives]:::completed
    HTPI1_1 --> HTPI1_2
    PRE_C1_1 --> HTPI1_3
    HTPI1_3 --> HTPI1_4 & HTPI4_1
    HTPI1_2 --> HTPI1_5

    %% HTPI CHAPTER 2
    HTPI2_1[2.1 Quantifiers]:::completed
    HTPI2_2[2.2 Equivalences Involving Quantifiers]:::completed
    HTPI2_3[2.3 More Operations on Sets]:::completed
    HTPI1_5 --> HTPI2_1
    HTPI2_1 --> HTPI2_2 & HTPI2_3
    HTPI1_4 --> HTPI2_3

    %% HTPI CHAPTER 3
    HTPI3_1[3.1 Proof Strategies]:::completed
    HTPI3_2[3.2 Proofs Involving Negations and Conditionals]:::completed
    HTPI3_3[3.3 Proofs Involving Quantifiers]:::completed
    HTPI3_4[3.4 Proofs Involving Conjunctions and Biconditionals]:::completed
    HTPI3_5[3.5 Proofs Involving Disjunctions]:::completed
    HTPI3_6[3.6 Existence and Uniqueness Proofs]:::completed
    HTPI3_7[3.7 More Examples of Proofs]:::completed
    HTPI2_2 --> HTPI3_1
    HTPI3_1 --> HTPI3_2 & HTPI6_1
    HTPI3_2 --> HTPI3_3
    HTPI3_3 --> HTPI3_4
    HTPI3_4 --> HTPI3_5
    HTPI3_5 --> HTPI3_6
    HTPI3_6 --> HTPI3_7
    HTPI3_7 --> HTPI4_1

    %% HTPI CHAPTER 4
    HTPI4_1[4.1 Ordered Pairs and Cartesian Products]:::incomplete
    HTPI4_2[4.2 Relations]:::incomplete
    HTPI4_3[4.3 More About Relations]:::incomplete
    HTPI4_4[4.4 Ordering Relations]:::incomplete
    HTPI4_5[4.5 Closures]:::incomplete
    HTPI4_6[4.6 Equivalence Relations]:::incomplete
    HTPI4_1 --> HTPI4_2
    HTPI4_2 --> HTPI4_3 & HTPI4_4 & HTPI4_5 & HTPI4_6 & HTPI5_1

    %% HTPI CHAPTER 5
    HTPI5_1[5.1 Functions]:::incomplete
    HTPI5_2[5.2 One-to-one and Onto]:::incomplete
    HTPI5_3[5.3 Inverses of Functions]:::incomplete
    HTPI5_4[5.4 Images and Inverse Images]:::incomplete
    PRE_C1_3 --> HTPI5_1
    HTPI5_1 --> HTPI5_2 & HTPI5_4
    HTPI5_2 --> HTPI5_3 & HTPI7_1
    PRE_C5_2 --> HTPI5_3

    %% HTPI CHAPTER 6
    HTPI6_1[6.1 Proof by Mathematical Induction]:::incomplete
    HTPI6_2[6.2 More Examples]:::incomplete
    HTPI6_3[6.3 Recursion]:::incomplete
    HTPI6_4[6.4 Strong Induction]:::incomplete
    HTPI6_5[6.5 Closures Again]:::incomplete
    PRE_C9_3 --> HTPI6_1
    HTPI6_1 --> HTPI6_2 & HTPI6_4
    HTPI6_2 --> HTPI6_3
    HTPI4_5 --> HTPI6_5

    %% HTPI CHAPTER 7
    HTPI7_1[7.1 Equinumerous Sets]:::incomplete
    HTPI7_2[7.2 Countable and Uncountable Sets]:::incomplete
    HTPI7_3[7.3 The Cantor-Schroder-Bernstein Theorem]:::incomplete
    HTPI7_1 --> HTPI7_2
    HTPI7_2 --> HTPI7_3
`