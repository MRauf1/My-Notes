---
tags:
  - philosophy
  - epistemology
---

# Definition
> [!info] Accuracy Argument (Joyce, 1998)[^1]
> An argument for [[Probabilism]] using purely epistemic goals, namely that beliefs should be as accurate as possible:
> - **[[Accuracy Theorem]].** If a set of beliefs violates the rules of probability, then it is [[Accuracy Dominance|accuracy dominated]] by one that doesn't.
> - **P1.** If you hold a dominated set of beliefs, then you are irrational.
> - **C.** Therefore, if your [[Credence|degrees of belief]] violate the rules of probability, then you are irrational.

Accuracy is measured by assigning each proposition its truth-value (X) \in \{0, 1\}$ at world $ ($ if true, /bin/zsh$ if false) and scoring a set of degrees of belief $ by its distance from these truth-values, with lower scores meaning greater accuracy. The standard choice is the Brier score (squared distance)
825810
\begin{align}
I(b, w) = \sum_{X \in B} \big(b(X) - w(X)\big)^2
\end{align}
825810

# Properties
- Unlike the [[Dutch Book Argument]], it is not pragmatic: it appeals to [[Epistemic Rationality|epistemic]] value (truth) rather than money.
- P1 is undermined if holding dominated beliefs were unavoidable, so the argument also needs the [[Converse Accuracy Theorem]].
- P1 looks compelling: if you can change your beliefs in a way that guarantees they become more accurate, you seem rationally obliged to do so, though this too has been questioned.
- Using the raw (unsquared) distance does not work; the theorem holds for the Brier score and, more generally, for any strictly proper scoring rule (Predd et al., 2009), and the choice of inaccuracy measure is a main point of contention.

[^1]: [A Critical Introduction to Formal Epistemology](zotero://open-pdf/library/items/9XYCZDPF?page=46)
