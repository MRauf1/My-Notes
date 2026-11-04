---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!abstract] Finite Hypothesis Class Generalization Bound[^1]
> Let $\{(X_i, Y_i)\}_{i=1}^n$ be drawn i.i.d. from $P_{X,Y}$ over $\mathcal{X} \times \{0, 1\}$, let $\mathcal{F}$ be a finite [[Hypothesis Space|hypothesis class]] of classifiers $\mathcal{X} \to \{0, 1\}$, and let $f^\star = \arg\min_{f \in \mathcal{F}} \mathbb{E}[\mathbb{I}[f(X) \neq Y]]$. The [[Empirical Risk Minimization|ERM]] classifier
> $$
> \begin{align}
> \hat{f} = \arg\min_{f \in \mathcal{F}} \frac{1}{n}\sum_{i=1}^n \mathbb{I}[f(X_i) \neq Y_i]
> \end{align}
> $$
> satisfies, with probability at least $1 - \delta$,
> $$
> \begin{align}
> \mathbb{E}[\mathbb{I}[\hat{f}(X) \neq Y]] - \mathbb{E}[\mathbb{I}[f^\star(X) \neq Y]] \leq \sqrt{\frac{2}{n}\ln\frac{2|\mathcal{F}|}{\delta}}.
> \end{align}
> $$

# Properties
- **Proof outline.**
  1. For a fixed $f$, the losses $\mathbb{I}[f(X_i) \neq Y_i]$ are i.i.d. in $[0, 1]$ with mean $\mathbb{E}[\mathbb{I}[f(X) \neq Y]]$. So by [[Hoeffding's Inequality]], with probability $1 - \delta'$ their average is within $\sqrt{\frac{1}{2n}\ln\frac{2}{\delta'}}$ of that mean.
  2. A union bound ([[Boole's Inequality]]) over $\mathcal{F}$ with $\delta' = \delta/|\mathcal{F}|$ gives a [[Uniform Deviation Bound]] of $\sqrt{\frac{1}{2n}\ln\frac{2|\mathcal{F}|}{\delta}}$.
  3. Excess risk is at most twice the uniform deviation, and $2\sqrt{\frac{1}{2n}\ln\frac{2|\mathcal{F}|}{\delta}} = \sqrt{\frac{2}{n}\ln\frac{2|\mathcal{F}|}{\delta}}$.
- The class size enters only through $\ln|\mathcal{F}|$, so exponentially large finite classes are learnable with polynomially many samples. Infinite classes need a capacity measure in place of $|\mathcal{F}|$.
- The excess-risk rate is $O(1/\sqrt{n})$. It holds for any distribution $P_{X,Y}$ and compares $\hat{f}$ only to the best classifier in $\mathcal{F}$, not to the Bayes classifier.
- Same template as the [[Uniform Sampling Simple Regret Bound]]: Hoeffding for each candidate, a union bound, then a decision-loss decomposition.

# Questions
> [!question]- Why can't Hoeffding's inequality be applied directly to the training error of $\hat{f}$?
> $\hat{f}$ is selected using the same sample. Conditioned on being selected, $\mathbb{I}[\hat{f}(X_i) \neq Y_i]$ are not i.i.d. draws with mean $\mathbb{E}[\mathbb{I}[\hat{f}(X) \neq Y]]$; ERM favours hypotheses whose training error is luckily low. Hoeffding's inequality holds for each *fixed* $f$, so we need it for all $f \in \mathcal{F}$ at once, which is the union bound and the source of the $\ln|\mathcal{F}|$.

> [!question]- Where is finiteness of $\mathcal{F}$ used, and how does the bound scale with $|\mathcal{F}|$?
> Only in the union bound: $\Pr[\exists f : \text{deviation} > \epsilon] \leq |\mathcal{F}| \cdot 2e^{-2n\epsilon^2}$, which is vacuous for infinite $\mathcal{F}$. Solving for $\epsilon$ gives the logarithmic cost $\ln(2|\mathcal{F}|/\delta)$, so the sample size needed for excess risk $\epsilon$ is $n \geq \frac{2}{\epsilon^2}\ln\frac{2|\mathcal{F}|}{\delta}$.

> [!question]- Application: In Paper 1, suppose the truncation level is picked from $K \in \{1, \dots, K_{\max}\}$ by minimizing held-out error, with each candidate's loss in $[0, 1]$. How many held-out samples guarantee that the chosen level is within $\epsilon$ of the best candidate with probability $1 - \delta$, and what must hold for the bound to apply?
> Treat the $K_{\max}$ fitted candidates as a finite class $\mathcal{F}$ and the held-out selection as ERM. The bound gives excess held-out risk $\leq \sqrt{\frac{2}{n}\ln\frac{2K_{\max}}{\delta}}$, so $n \geq \frac{2}{\epsilon^2}\ln\frac{2K_{\max}}{\delta}$ suffices. That's only logarithmic in the number of truncation levels.
>
> This requires the candidates to be fixed before the held-out data are seen (fitted on a separate training split), the held-out samples to be i.i.d., and the loss to be bounded in $[0, 1]$ (rescale otherwise). If the same data both fit and select the expansions, the class is data-dependent and the argument fails.

[^1]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), pp. 3–4](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=3)
