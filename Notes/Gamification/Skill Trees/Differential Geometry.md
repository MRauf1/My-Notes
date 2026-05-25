```mermaid
flowchart TD
    classDef completed fill:#FFD700,stroke:#FF8C00,stroke-width:4px,rx:10px,ry:10px,color:#000000,font-weight:bold;
    classDef incomplete fill:#1E293B,stroke:#64748B,stroke-width:3px,stroke-dasharray: 5 5,rx:10px,ry:10px,color:#CBD5E1;
    classDef prereq fill:#8A2BE2,stroke:#4B0082,stroke-width:4px,rx:10px,ry:10px,color:#FFFFFF,font-weight:bold;

    %% PREREQUISITES
    PRE_CALC12_1["[Calculus] 12.1 - 3D Coordinate Systems"]:::prereq
    PRE_CALC12_2["[Calculus] 12.2 - Vectors"]:::prereq
    PRE_CALC12_3["[Calculus] 12.3 - The Dot Product"]:::prereq
    PRE_CALC13_1["[Calculus] 13.1 - Vector Functions and Space Curves"]:::prereq
    PRE_CALC13_3["[Calculus] 13.3 - Arc Length and Curvature"]:::prereq
    PRE_CALC14_3["[Calculus] 14.3 - Partial Derivatives"]:::prereq
    PRE_CALC14_6["[Calculus] 14.6 - Directional Derivatives"]:::prereq
    PRE_CALC16_2["[Calculus] 16.2 - Line Integrals"]:::prereq
    PRE_CALC16_6["[Calculus] 16.6 - Parametric Surfaces"]:::prereq
    PRE_CALC16_8["[Calculus] 16.8 - Stokes' Theorem"]:::prereq
    PRE_DE1_1["[Diff Eq] 1.1 - DEs and Models"]:::prereq
    PRE_LA2_1["[Linear Algebra] 2.1 - Linear Maps"]:::prereq
    PRE_LA4_1["[Linear Algebra] 4.1 - Inner Products"]:::prereq
    PRE_LA4_5["[Linear Algebra] 4.5 - Isometries"]:::prereq
    PRE_RA1_5["[Real Analysis] 1.5 - Euclidean Spaces"]:::prereq
    PRE_RA2_2["[Real Analysis] 2.2 - Metric Spaces"]:::prereq
    PRE_RA2_3["[Real Analysis] 2.3 - Compact Sets"]:::prereq
    PRE_RA2_4["[Real Analysis] 2.4 - Perfect Sets and Connected Sets"]:::prereq
    PRE_RA9_3["[Real Analysis] 9.3 - The Inverse and Implicit Function Theorems"]:::prereq
    PRE_RA10_2["[Real Analysis] 10.2 - Partitions of Unity and Change of Variables"]:::prereq
    PRE_RA10_3["[Real Analysis] 10.3 - Differential Forms"]:::prereq
    PRE_SPIVAK_4_2["[Calc on Manifolds] 4 - Fields and Forms"]:::prereq
    PRE_SPIVAK_5_1["[Calc on Manifolds] 5 - Manifolds"]:::prereq
    PRE_SPIVAK_5_3["[Calc on Manifolds] 5 - Stokes' Theorem on Manifolds"]:::prereq
    PRE_AA1_1["[Abstract Algebra] 1.1 - Basic Axioms and Examples"]:::prereq
    PRE_AA1_7["[Abstract Algebra] 1.7 - Group Actions"]:::prereq
    PRE_AA6_3["[Abstract Algebra] 6.3 - A Word on Free Groups"]:::prereq
    PRE_AA11_5["[Abstract Algebra] 11.5 - Tensor Algebras, Symmetric and Exterior Algebras"]:::prereq
    PRE_HTPI4_6["[How to Prove It] 4.6 - Equivalence Relations"]:::prereq
    PRE_HTPI7_2["[How to Prove It] 7.2 - Countable and Uncountable Sets"]:::prereq

    %% NEW TOPOLOGY PREREQUISITES
    PRE_TOP_12["[Topology] 12 - Topological Spaces"]:::prereq
    PRE_TOP_15["[Topology] 15 - Product Topology"]:::prereq
    PRE_TOP_16["[Topology] 16 - Subspace Topology"]:::prereq
    PRE_TOP_18["[Topology] 18 - Continuous Functions"]:::prereq
    PRE_TOP_22["[Topology] 22 - The Quotient Topology"]:::prereq
    PRE_TOP_23["[Topology] 23 - Connected Spaces"]:::prereq
    PRE_TOP_26["[Topology] 26 - Compact Spaces"]:::prereq
    PRE_TOP_31["[Topology] 31 - The Separation Axioms"]:::prereq
    PRE_TOP_52["[Topology] 52 - The Fundamental Group"]:::prereq
    PRE_TOP_53["[Topology] 53 - Covering Spaces"]:::prereq
    PRE_TOP_70["[Topology] 70 - The Seifert-van Kampen Theorem"]:::prereq

    %% ==========================================
    %% DIFFERENTIAL GEOMETRY (O'NEILL)
    %% ==========================================
    
    %% CHAPTER 1: CALCULUS ON EUCLIDEAN SPACE
    DG1_1["1.1 - Euclidean Space"]:::incomplete
    DG1_2["1.2 - Tangent Vectors"]:::incomplete
    DG1_3["1.3 - Directional Derivatives"]:::incomplete
    DG1_4["1.4 - Curves in R^3"]:::incomplete
    DG1_5["1.5 - 1-Forms"]:::incomplete
    DG1_6["1.6 - Differential Forms"]:::incomplete
    DG1_7["1.7 - Mappings"]:::incomplete
    DG1_8["1.8 - Summary"]:::incomplete

    PRE_RA1_5 --> DG1_1
    PRE_CALC12_1 --> DG1_1
    DG1_1 --> DG1_2
    PRE_CALC12_2 --> DG1_2
    DG1_2 --> DG1_3
    PRE_CALC14_6 --> DG1_3
    DG1_2 --> DG1_4
    PRE_CALC13_1 --> DG1_4
    DG1_3 --> DG1_5
    DG1_5 --> DG1_6
    PRE_RA10_3 --> DG1_6
    DG1_6 --> DG1_7
    DG1_7 --> DG1_8

    %% CHAPTER 2: FRAME FIELDS
    DG2_1["2.1 - Dot Product"]:::incomplete
    DG2_2["2.2 - Curves"]:::incomplete
    DG2_3["2.3 - The Frenet Formulas"]:::incomplete
    DG2_4["2.4 - Arbitrary-Speed Curves"]:::incomplete
    DG2_5["2.5 - Covariant Derivatives"]:::incomplete
    DG2_6["2.6 - Frame Fields"]:::incomplete
    DG2_7["2.7 - Connection Forms"]:::incomplete
    DG2_8["2.8 - The Structural Equations"]:::incomplete
    DG2_9["2.9 - Summary"]:::incomplete

    DG1_2 --> DG2_1
    PRE_CALC12_3 --> DG2_1
    DG1_4 --> DG2_2
    DG2_1 --> DG2_2
    DG2_2 --> DG2_3
    PRE_CALC13_3 --> DG2_3
    DG2_3 --> DG2_4
    DG1_3 --> DG2_5
    DG2_5 --> DG2_6
    DG2_6 --> DG2_7
    DG2_7 --> DG2_8
    DG2_8 --> DG2_9

    %% CHAPTER 3: EUCLIDEAN GEOMETRY
    DG3_1["3.1 - Isometries of R^3"]:::incomplete
    DG3_2["3.2 - The Tangent Map of an Isometry"]:::incomplete
    DG3_3["3.3 - Orientation"]:::incomplete
    DG3_4["3.4 - Euclidean Geometry"]:::incomplete
    DG3_5["3.5 - Congruence of Curves"]:::incomplete
    DG3_6["3.6 - Summary"]:::incomplete

    PRE_LA4_5 --> DG3_1
    DG3_1 --> DG3_2
    PRE_LA2_1 --> DG3_2
    DG3_2 --> DG3_3
    DG3_3 --> DG3_4
    DG3_4 --> DG3_5
    DG3_5 --> DG3_6

    %% CHAPTER 4: CALCULUS ON A SURFACE
    DG4_1["4.1 - Surfaces in R^3"]:::incomplete
    DG4_2["4.2 - Patch Computations"]:::incomplete
    DG4_3["4.3 - Differentiable Functions and Tangent Vectors"]:::incomplete
    DG4_4["4.4 - Differential Forms on a Surface"]:::incomplete
    DG4_5["4.5 - Mappings of Surfaces"]:::incomplete
    DG4_6["4.6 - Integration of Forms"]:::incomplete
    DG4_7["4.7 - Topological Properties of Surfaces"]:::incomplete
    DG4_8["4.8 - Manifolds"]:::incomplete
    DG4_9["4.9 - Summary"]:::incomplete

    PRE_CALC16_6 --> DG4_1
    DG4_1 --> DG4_2
    DG4_2 --> DG4_3
    DG1_6 --> DG4_4
    DG4_3 --> DG4_4
    DG4_3 --> DG4_5
    DG4_4 --> DG4_6
    DG4_6 --> DG4_7
    DG4_7 --> DG4_8
    PRE_SPIVAK_5_1 --> DG4_8
    DG4_8 --> DG4_9

    %% CHAPTER 5: SHAPE OPERATORS
    DG5_1["5.1 - The Shape Operator of M c R^3"]:::incomplete
    DG5_2["5.2 - Normal Curvature"]:::incomplete
    DG5_3["5.3 - Gaussian Curvature"]:::incomplete
    DG5_4["5.4 - Computational Techniques"]:::incomplete
    DG5_5["5.5 - The Implicit Case"]:::incomplete
    DG5_6["5.6 - Special Curves in a Surface"]:::incomplete
    DG5_7["5.7 - Surfaces of Revolution"]:::incomplete
    DG5_8["5.8 - Summary"]:::incomplete

    DG4_3 --> DG5_1
    DG5_1 --> DG5_2
    DG5_2 --> DG5_3
    DG5_3 --> DG5_4
    DG5_4 --> DG5_5
    DG5_4 --> DG5_6
    DG5_6 --> DG5_7
    DG5_7 --> DG5_8

    %% CHAPTER 6: GEOMETRY OF SURFACES IN R^3
    DG6_1["6.1 - The Fundamental Equations"]:::incomplete
    DG6_2["6.2 - Form Computations"]:::incomplete
    DG6_3["6.3 - Some Global Theorems"]:::incomplete
    DG6_4["6.4 - Isometries and Local Isometries"]:::incomplete
    DG6_5["6.5 - Intrinsic Geometry of Surfaces in R^3"]:::incomplete
    DG6_6["6.6 - Orthogonal Coordinates"]:::incomplete
    DG6_7["6.7 - Integration and Orientation"]:::incomplete
    DG6_8["6.8 - Total Curvature"]:::incomplete
    DG6_9["6.9 - Congruence of Surfaces"]:::incomplete
    DG6_10["6.10 - Summary"]:::incomplete

    DG5_3 --> DG6_1
    DG6_1 --> DG6_2
    DG6_2 --> DG6_3
    DG3_1 --> DG6_4
    DG6_2 --> DG6_4
    DG6_4 --> DG6_5
    DG6_5 --> DG6_6
    DG4_6 --> DG6_7
    DG6_5 --> DG6_7
    DG6_7 --> DG6_8
    DG6_8 --> DG6_9
    DG6_9 --> DG6_10

    %% CHAPTER 7: RIEMANNIAN GEOMETRY
    DG7_1["7.1 - Geometric Surfaces"]:::incomplete
    DG7_2["7.2 - Gaussian Curvature"]:::incomplete
    DG7_3["7.3 - Covariant Derivative"]:::incomplete
    DG7_4["7.4 - Geodesics"]:::incomplete
    DG7_5["7.5 - Clairaut Parametrizations"]:::incomplete
    DG7_6["7.6 - The Gauss-Bonnet Theorem"]:::incomplete
    DG7_7["7.7 - Applications of Gauss-Bonnet"]:::incomplete
    DG7_8["7.8 - Summary"]:::incomplete

    DG6_5 --> DG7_1
    DG7_1 --> DG7_2
    DG5_3 --> DG7_2
    DG2_5 --> DG7_3
    DG7_1 --> DG7_3
    DG7_3 --> DG7_4
    DG7_4 --> DG7_5
    DG6_8 --> DG7_6
    DG7_4 --> DG7_6
    DG7_6 --> DG7_7
    DG7_7 --> DG7_8

    %% CHAPTER 8: GLOBAL STRUCTURE OF SURFACES
    DG8_1["8.1 - Length-Minimizing Properties of Geodesics"]:::incomplete
    DG8_2["8.2 - Complete Surfaces"]:::incomplete
    DG8_3["8.3 - Curvature and Conjugate Points"]:::incomplete
    DG8_4["8.4 - Covering Surfaces"]:::incomplete
    DG8_5["8.5 - Mappings That Preserve Inner Products"]:::incomplete
    DG8_6["8.6 - Surfaces of Constant Curvature"]:::incomplete
    DG8_7["8.7 - Theorems of Bonnet and Hadamard"]:::incomplete
    DG8_8["8.8 - Summary"]:::incomplete

    DG7_4 --> DG8_1
    DG4_7 --> DG8_2
    DG8_1 --> DG8_2
    DG7_2 --> DG8_3
    DG8_2 --> DG8_3
    DG8_2 --> DG8_4
    DG8_4 --> DG8_5
    DG8_3 --> DG8_6
    DG8_6 --> DG8_7
    DG8_7 --> DG8_8

    %% ==========================================
    %% AN INTRODUCTION TO MANIFOLDS (TU)
    %% ==========================================
    
    %% CHAPTER 1: EUCLIDEAN SPACES
    TU_1["1 - Smooth Functions on a Euclidean Space"]:::incomplete
    TU_2["2 - Tangent Vectors in R^n as Derivations"]:::incomplete
    TU_3["3 - The Exterior Algebra of Multicovectors"]:::incomplete
    TU_4["4 - Differential Forms on R^n"]:::incomplete

    PRE_RA1_5 --> TU_1
    PRE_CALC14_3 --> TU_1
    TU_1 --> TU_2
    PRE_CALC14_6 --> TU_2
    PRE_AA11_5 --> TU_3
    TU_2 --> TU_4
    TU_3 --> TU_4
    PRE_SPIVAK_4_2 --> TU_4

    %% CHAPTER 2: MANIFOLDS
    TU_5["5 - Manifolds"]:::incomplete
    TU_6["6 - Smooth Maps on a Manifold"]:::incomplete
    TU_7["7 - Quotients"]:::incomplete

    PRE_RA2_2 --> TU_5
    PRE_SPIVAK_5_1 --> TU_5
    DG4_8 --> TU_5
    TU_1 --> TU_6
    TU_5 --> TU_6
    TU_5 --> TU_7

    %% CHAPTER 3: THE TANGENT SPACE
    TU_8["8 - The Tangent Space"]:::incomplete
    TU_9["9 - Submanifolds"]:::incomplete
    TU_10["10 - Categories and Functors"]:::incomplete
    TU_11["11 - The Rank of a Smooth Map"]:::incomplete
    TU_12["12 - The Tangent Bundle"]:::incomplete
    TU_13["13 - Bump Functions and Partitions of Unity"]:::incomplete
    TU_14["14 - Vector Fields"]:::incomplete

    TU_2 --> TU_8
    TU_6 --> TU_8
    TU_8 --> TU_9
    PRE_RA9_3 --> TU_9
    TU_6 --> TU_10
    TU_8 --> TU_11
    TU_8 --> TU_12
    TU_5 --> TU_13
    PRE_RA10_2 --> TU_13
    TU_12 --> TU_14

    %% CHAPTER 4: LIE GROUPS AND LIE ALGEBRAS
    TU_15["15 - Lie Groups"]:::incomplete
    TU_16["16 - Lie Algebras"]:::incomplete

    PRE_AA1_1 --> TU_15
    TU_6 --> TU_15
    TU_14 --> TU_16
    TU_15 --> TU_16

    %% CHAPTER 5: DIFFERENTIAL FORMS
    TU_17["17 - Differential 1-Forms"]:::incomplete
    TU_18["18 - Differential k-Forms"]:::incomplete
    TU_19["19 - The Exterior Derivative"]:::incomplete
    TU_20["20 - The Lie Derivative and Interior Multiplication"]:::incomplete

    TU_4 --> TU_17
    TU_12 --> TU_17
    TU_17 --> TU_18
    TU_3 --> TU_18
    TU_18 --> TU_19
    TU_14 --> TU_20
    TU_19 --> TU_20

    %% CHAPTER 6: INTEGRATION
    TU_21["21 - Orientations"]:::incomplete
    TU_22["22 - Manifolds with Boundary"]:::incomplete
    TU_23["23 - Integration on Manifolds"]:::incomplete

    TU_18 --> TU_21
    TU_5 --> TU_22
    TU_13 --> TU_23
    TU_21 --> TU_23
    TU_22 --> TU_23
    PRE_SPIVAK_5_3 --> TU_23

    %% CHAPTER 7: DE RHAM THEORY
    TU_24["24 - De Rham Cohomology"]:::incomplete
    TU_25["25 - The Long Exact Sequence in Cohomology"]:::incomplete
    TU_26["26 - The Mayer-Vietoris Sequence"]:::incomplete
    TU_27["27 - Homotopy Invariance"]:::incomplete
    TU_28["28 - Computation of de Rham Cohomology"]:::incomplete
    TU_29["29 - Proof of Homotopy Invariance"]:::incomplete

    TU_19 --> TU_24
    TU_24 --> TU_25
    TU_25 --> TU_26
    TU_24 --> TU_27
    TU_26 --> TU_28
    TU_27 --> TU_28
    TU_27 --> TU_29

    %% ==========================================
    %% INTRO TO TOPOLOGICAL MANIFOLDS (LEE)
    %% ==========================================
    
    LEE_1["1 - Introduction"]:::incomplete
    LEE_2_1["2.1 - Topologies"]:::incomplete
    LEE_2_2["2.2 - Convergence and Continuity"]:::incomplete
    LEE_2_3["2.3 - Hausdorff Spaces"]:::incomplete
    LEE_2_4["2.4 - Bases and Countability"]:::incomplete
    LEE_2_5["2.5 - Manifolds"]:::incomplete
    
    PRE_TOP_12 --> LEE_2_1
    PRE_RA2_2 --> LEE_2_1
    LEE_2_1 --> LEE_2_2
    PRE_TOP_18 --> LEE_2_2
    LEE_2_1 --> LEE_2_3
    PRE_TOP_31 --> LEE_2_3
    PRE_HTPI7_2 --> LEE_2_4
    LEE_2_1 --> LEE_2_4
    LEE_2_3 --> LEE_2_5
    LEE_2_4 --> LEE_2_5
    
    LEE_3_1["3.1 - Subspaces"]:::incomplete
    LEE_3_2["3.2 - Product Spaces"]:::incomplete
    LEE_3_3["3.3 - Disjoint Union Spaces"]:::incomplete
    LEE_3_4["3.4 - Quotient Spaces"]:::incomplete
    LEE_3_5["3.5 - Adjunction Spaces"]:::incomplete
    LEE_3_6["3.6 - Topological Groups and Group Actions"]:::incomplete
    
    LEE_2_1 --> LEE_3_1
    PRE_TOP_16 --> LEE_3_1
    LEE_2_1 --> LEE_3_2
    PRE_TOP_15 --> LEE_3_2
    LEE_2_1 --> LEE_3_3
    PRE_HTPI4_6 --> LEE_3_4
    PRE_TOP_22 --> LEE_3_4
    LEE_2_1 --> LEE_3_4
    LEE_3_4 --> LEE_3_5
    PRE_AA1_1 --> LEE_3_6
    PRE_AA1_7 --> LEE_3_6
    LEE_3_2 --> LEE_3_6
    
    LEE_4_1["4.1 - Connectedness"]:::incomplete
    LEE_4_2["4.2 - Compactness"]:::incomplete
    LEE_4_3["4.3 - Local Compactness"]:::incomplete
    LEE_4_4["4.4 - Paracompactness"]:::incomplete
    LEE_4_5["4.5 - Proper Maps"]:::incomplete
    
    PRE_RA2_4 --> LEE_4_1
    PRE_TOP_23 --> LEE_4_1
    LEE_2_1 --> LEE_4_1
    PRE_RA2_3 --> LEE_4_2
    PRE_TOP_26 --> LEE_4_2
    LEE_2_1 --> LEE_4_2
    LEE_4_2 --> LEE_4_3
    LEE_4_3 --> LEE_4_4
    LEE_4_2 --> LEE_4_5
    
    LEE_5_1["5.1 - Cell Complexes and CW Complexes"]:::incomplete
    LEE_5_2["5.2 - Topological Properties of CW Complexes"]:::incomplete
    LEE_5_3["5.3 - Classification of 1-Dimensional Manifolds"]:::incomplete
    LEE_5_4["5.4 - Simplicial Complexes"]:::incomplete
    
    LEE_3_4 --> LEE_5_1
    LEE_3_5 --> LEE_5_1
    LEE_5_1 --> LEE_5_2
    LEE_2_5 --> LEE_5_3
    LEE_4_1 --> LEE_5_3
    LEE_5_1 --> LEE_5_4
    
    LEE_6_1["6.1 - Surfaces"]:::incomplete
    LEE_6_2["6.2 - Connected Sums of Surfaces"]:::incomplete
    LEE_6_3["6.3 - Polygonal Presentations of Surfaces"]:::incomplete
    LEE_6_4["6.4 - The Classification Theorem"]:::incomplete
    LEE_6_5["6.5 - The Euler Characteristic"]:::incomplete
    LEE_6_6["6.6 - Orientability"]:::incomplete
    
    LEE_2_5 --> LEE_6_1
    LEE_4_2 --> LEE_6_1
    LEE_6_1 --> LEE_6_2
    LEE_6_1 --> LEE_6_3
    LEE_6_2 --> LEE_6_4
    LEE_6_3 --> LEE_6_4
    LEE_6_3 --> LEE_6_5
    LEE_6_1 --> LEE_6_6
    
    LEE_7_1["7.1 - Homotopy"]:::incomplete
    LEE_7_2["7.2 - The Fundamental Group"]:::incomplete
    LEE_7_3["7.3 - Homomorphisms Induced by Continuous Maps"]:::incomplete
    LEE_7_4["7.4 - Homotopy Equivalence"]:::incomplete
    LEE_7_5["7.5 - Higher Homotopy Groups"]:::incomplete
    LEE_7_6["7.6 - Categories and Functors"]:::incomplete
    
    LEE_2_2 --> LEE_7_1
    LEE_7_1 --> LEE_7_2
    PRE_TOP_52 --> LEE_7_2
    LEE_7_2 --> LEE_7_3
    LEE_7_1 --> LEE_7_4
    LEE_7_2 --> LEE_7_5
    LEE_7_3 --> LEE_7_6
    
    LEE_8_1["8.1 - Lifting Properties of the Circle"]:::incomplete
    LEE_8_2["8.2 - The Fundamental Group of the Circle"]:::incomplete
    LEE_8_3["8.3 - Degree Theory for the Circle"]:::incomplete
    
    LEE_7_2 --> LEE_8_1
    LEE_8_1 --> LEE_8_2
    LEE_8_2 --> LEE_8_3
    
    LEE_9_1["9.1 - Free Products"]:::incomplete
    LEE_9_2["9.2 - Free Groups"]:::incomplete
    LEE_9_3["9.3 - Presentations of Groups"]:::incomplete
    LEE_9_4["9.4 - Free Abelian Groups"]:::incomplete
    
    PRE_AA1_1 --> LEE_9_1
    LEE_9_1 --> LEE_9_2
    PRE_AA6_3 --> LEE_9_2
    LEE_9_2 --> LEE_9_3
    LEE_9_2 --> LEE_9_4
    
    LEE_10_1["10.1 - Statement of the Theorem"]:::incomplete
    LEE_10_2["10.2 - Applications"]:::incomplete
    LEE_10_3["10.3 - Fundamental Groups of Compact Surfaces"]:::incomplete
    LEE_10_4["10.4 - Proof of the Seifert-Van Kampen Theorem"]:::incomplete
    
    LEE_7_2 --> LEE_10_1
    PRE_TOP_70 --> LEE_10_1
    LEE_9_1 --> LEE_10_1
    LEE_10_1 --> LEE_10_2
    LEE_6_4 --> LEE_10_3
    LEE_10_1 --> LEE_10_3
    LEE_10_1 --> LEE_10_4
    
    LEE_11_1["11.1 - Definitions and Basic Properties"]:::incomplete
    LEE_11_2["11.2 - The General Lifting Problem"]:::incomplete
    LEE_11_3["11.3 - The Monodromy Action"]:::incomplete
    LEE_11_4["11.4 - Covering Homomorphisms"]:::incomplete
    LEE_11_5["11.5 - The Universal Covering Space"]:::incomplete
    
    LEE_2_2 --> LEE_11_1
    PRE_TOP_53 --> LEE_11_1
    LEE_11_1 --> LEE_11_2
    LEE_7_2 --> LEE_11_2
    LEE_11_2 --> LEE_11_3
    LEE_11_1 --> LEE_11_4
    LEE_11_2 --> LEE_11_5
    
    LEE_12_1["12.1 - The Automorphism Group of a Covering"]:::incomplete
    LEE_12_2["12.2 - Quotients by Group Actions"]:::incomplete
    LEE_12_3["12.3 - The Classification Theorem"]:::incomplete
    LEE_12_4["12.4 - Proper Group Actions"]:::incomplete
    
    LEE_11_4 --> LEE_12_1
    LEE_3_6 --> LEE_12_2
    LEE_11_1 --> LEE_12_2
    LEE_11_5 --> LEE_12_3
    LEE_12_1 --> LEE_12_3
    LEE_12_2 --> LEE_12_4
    
    LEE_13_1["13.1 - Singular Homology Groups"]:::incomplete
    LEE_13_2["13.2 - Homotopy Invariance"]:::incomplete
    LEE_13_3["13.3 - Homology and the Fundamental Group"]:::incomplete
    LEE_13_4["13.4 - The Mayer-Vietoris Theorem"]:::incomplete
    LEE_13_5["13.5 - Homology of Spheres"]:::incomplete
    LEE_13_6["13.6 - Homology of CW Complexes"]:::incomplete
    LEE_13_7["13.7 - Cohomology"]:::incomplete
    
    LEE_7_6 --> LEE_13_1
    LEE_13_1 --> LEE_13_2
    LEE_7_2 --> LEE_13_3
    LEE_13_1 --> LEE_13_3
    LEE_13_1 --> LEE_13_4
    LEE_13_4 --> LEE_13_5
    LEE_5_1 --> LEE_13_6
    LEE_13_1 --> LEE_13_6
    LEE_13_1 --> LEE_13_7

    %% ==========================================
    %% INTRO TO SMOOTH MANIFOLDS (LEE)
    %% ==========================================
    
    LEESM_1["1 - Smooth Manifolds"]:::incomplete
    LEESM_2["2 - Smooth Maps"]:::incomplete
    LEESM_3["3 - Tangent Vectors"]:::incomplete
    LEESM_4["4 - Submersions, Immersions, and Embeddings"]:::incomplete
    LEESM_5["5 - Submanifolds"]:::incomplete
    LEESM_6["6 - Sard's Theorem"]:::incomplete
    LEESM_7["7 - Lie Groups"]:::incomplete
    LEESM_8["8 - Vector Fields"]:::incomplete
    LEESM_9["9 - Integral Curves and Flows"]:::incomplete
    LEESM_10["10 - Vector Bundles"]:::incomplete
    LEESM_11["11 - The Cotangent Bundle"]:::incomplete
    LEESM_12["12 - Tensors"]:::incomplete
    LEESM_13["13 - Riemannian Metrics"]:::incomplete
    LEESM_14["14 - Differential Forms"]:::incomplete
    LEESM_15["15 - Orientations"]:::incomplete
    LEESM_16["16 - Integration on Manifolds"]:::incomplete
    LEESM_17["17 - De Rham Cohomology"]:::incomplete
    LEESM_18["18 - The de Rham Theorem"]:::incomplete
    LEESM_19["19 - Distributions and Foliations"]:::incomplete
    LEESM_20["20 - The Exponential Map"]:::incomplete
    LEESM_21["21 - Quotient Manifolds"]:::incomplete
    LEESM_22["22 - Symplectic Manifolds"]:::incomplete

    LEE_2_5 --> LEESM_1
    PRE_CALC14_3 --> LEESM_1
    LEESM_1 --> LEESM_2
    PRE_RA10_2 --> LEESM_2
    LEESM_2 --> LEESM_3
    PRE_CALC12_2 --> LEESM_3
    PRE_LA2_1 --> LEESM_3
    LEESM_3 --> LEESM_4
    PRE_RA9_3 --> LEESM_4
    LEE_11_4 --> LEESM_4
    LEESM_4 --> LEESM_5
    LEESM_5 --> LEESM_6
    LEESM_2 --> LEESM_7
    PRE_AA1_1 --> LEESM_7
    LEESM_3 --> LEESM_8
    LEESM_7 --> LEESM_8
    LEESM_8 --> LEESM_9
    PRE_DE1_1 --> LEESM_9
    LEESM_5 --> LEESM_10
    LEESM_10 --> LEESM_11
    PRE_CALC16_2 --> LEESM_11
    LEESM_11 --> LEESM_12
    PRE_AA11_5 --> LEESM_12
    LEESM_12 --> LEESM_13
    PRE_LA4_1 --> LEESM_13
    LEESM_12 --> LEESM_14
    PRE_RA10_3 --> LEESM_14
    LEESM_14 --> LEESM_15
    LEESM_15 --> LEESM_16
    PRE_CALC16_8 --> LEESM_16
    LEESM_16 --> LEESM_17
    LEE_13_7 --> LEESM_17
    LEESM_17 --> LEESM_18
    LEE_13_1 --> LEESM_18
    LEESM_8 --> LEESM_19
    LEESM_7 --> LEESM_20
    LEESM_9 --> LEESM_20
    LEESM_7 --> LEESM_21
    LEE_12_2 --> LEESM_21
    LEESM_14 --> LEESM_22

    %% ==========================================
    %% INTRO TO RIEMANNIAN MANIFOLDS (LEE)
    %% ==========================================
    
    LEERM_1["1 - What Is Curvature?"]:::incomplete
    LEERM_2["2 - Riemannian Metrics"]:::incomplete
    LEERM_3["3 - Model Riemannian Manifolds"]:::incomplete
    LEERM_4["4 - Connections"]:::incomplete
    LEERM_5["5 - The Levi-Civita Connection"]:::incomplete
    LEERM_6["6 - Geodesics and Distance"]:::incomplete
    LEERM_7["7 - Curvature"]:::incomplete
    LEERM_8["8 - Riemannian Submanifolds"]:::incomplete
    LEERM_9["9 - The Gauss-Bonnet Theorem"]:::incomplete
    LEERM_10["10 - Jacobi Fields"]:::incomplete
    LEERM_11["11 - Comparison Theory"]:::incomplete
    LEERM_12["12 - Curvature and Topology"]:::incomplete

    LEESM_1 --> LEERM_1
    LEESM_13 --> LEERM_2
    LEERM_2 --> LEERM_3
    LEESM_7 --> LEERM_3
    LEESM_8 --> LEERM_4
    LEESM_12 --> LEERM_4
    LEERM_2 --> LEERM_5
    LEERM_4 --> LEERM_5
    LEERM_5 --> LEERM_6
    LEERM_5 --> LEERM_7
    LEESM_5 --> LEERM_8
    LEERM_7 --> LEERM_8
    LEESM_16 --> LEERM_9
    LEERM_7 --> LEERM_9
    LEERM_6 --> LEERM_10
    LEERM_7 --> LEERM_10
    LEERM_10 --> LEERM_11
    LEERM_11 --> LEERM_12
    LEE_11_1 --> LEERM_12

    %% ==========================================
    %% CLASS ASSIGNMENTS
    %% ==========================================
    class DG1_1,DG1_2,DG1_3,DG1_4,DG1_5,DG1_6,DG1_7,DG1_8,DG2_1,DG2_2,DG2_3,DG2_4,DG2_5,DG2_6,DG2_7,DG2_8,DG2_9,DG3_1,DG3_2,DG3_3,DG3_4,DG3_5,DG3_6,DG4_1,DG4_2,DG4_3,DG4_4,DG4_5,DG4_6,DG4_7,DG4_8,DG4_9,DG5_1,DG5_2,DG5_3,DG5_4,DG5_5,DG5_6,DG5_7,DG5_8,DG6_1,DG6_2,DG6_3,DG6_4,DG6_5,DG6_6,DG6_7,DG6_8,DG6_9,DG6_10,DG7_1,DG7_2,DG7_3,DG7_4,DG7_5,DG7_6,DG7_7,DG7_8,DG8_1,DG8_2,DG8_3,DG8_4,DG8_5,DG8_6,DG8_7,DG8_8 incomplete;
    
    class TU_1,TU_2,TU_3,TU_4,TU_5,TU_6,TU_7,TU_8,TU_9,TU_10,TU_11,TU_12,TU_13,TU_14,TU_15,TU_16,TU_17,TU_18,TU_19,TU_20,TU_21,TU_22,TU_23,TU_24,TU_25,TU_26,TU_27,TU_28,TU_29 incomplete;
    
    class LEE_1,LEE_2_1,LEE_2_2,LEE_2_3,LEE_2_4,LEE_2_5,LEE_3_1,LEE_3_2,LEE_3_3,LEE_3_4,LEE_3_5,LEE_3_6,LEE_4_1,LEE_4_2,LEE_4_3,LEE_4_4,LEE_4_5,LEE_5_1,LEE_5_2,LEE_5_3,LEE_5_4,LEE_6_1,LEE_6_2,LEE_6_3,LEE_6_4,LEE_6_5,LEE_6_6,LEE_7_1,LEE_7_2,LEE_7_3,LEE_7_4,LEE_7_5,LEE_7_6,LEE_8_1,LEE_8_2,LEE_8_3,LEE_9_1,LEE_9_2,LEE_9_3,LEE_9_4,LEE_10_1,LEE_10_2,LEE_10_3,LEE_10_4,LEE_11_1,LEE_11_2,LEE_11_3,LEE_11_4,LEE_11_5,LEE_12_1,LEE_12_2,LEE_12_3,LEE_12_4,LEE_13_1,LEE_13_2,LEE_13_3,LEE_13_4,LEE_13_5,LEE_13_6,LEE_13_7 incomplete;

    class LEESM_1,LEESM_2,LEESM_3,LEESM_4,LEESM_5,LEESM_6,LEESM_7,LEESM_8,LEESM_9,LEESM_10,LEESM_11,LEESM_12,LEESM_13,LEESM_14,LEESM_15,LEESM_16,LEESM_17,LEESM_18,LEESM_19,LEESM_20,LEESM_21,LEESM_22 incomplete;

    class LEERM_1,LEERM_2,LEERM_3,LEERM_4,LEERM_5,LEERM_6,LEERM_7,LEERM_8,LEERM_9,LEERM_10,LEERM_11,LEERM_12 incomplete;

    class TOP_1,TOP_2,TOP_3,TOP_4,TOP_5,TOP_6,TOP_7,TOP_8,TOP_9,TOP_10,TOP_11,TOP_12,TOP_13,TOP_14,TOP_15,TOP_16,TOP_17,TOP_18,TOP_19,TOP_20,TOP_21,TOP_22,TOP_23,TOP_24,TOP_25,TOP_26,TOP_27,TOP_28,TOP_29,TOP_30,TOP_31,TOP_32,TOP_33,TOP_34,TOP_35,TOP_36,TOP_37,TOP_38,TOP_39,TOP_40,TOP_41,TOP_42,TOP_43,TOP_44,TOP_45,TOP_46,TOP_47,TOP_48,TOP_49,TOP_50,TOP_51,TOP_52,TOP_53,TOP_54,TOP_55,TOP_56,TOP_57,TOP_58,TOP_59,TOP_60,TOP_61,TOP_62,TOP_63,TOP_64,TOP_65,TOP_66,TOP_67,TOP_68,TOP_69,TOP_70,TOP_71,TOP_72,TOP_73,TOP_74,TOP_75,TOP_76,TOP_77,TOP_78,TOP_79,TOP_80,TOP_81,TOP_82,TOP_83,TOP_84,TOP_85 incomplete;
```