---
tags:
  - statistics
  - categorical_variable_prediction
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (P-Value)
> If [[Test Statistic]] $T$ tends to be larger under $H_a$, then the p-value is
> $$
> \begin{align}
> P-\text{value} = P_{H_0}(T \geq t_0)
> \end{align}
> $$
> where $t_0$ is the observed value of $T$.

> [!info] Definition 2 (General P-Value)[^1]
> Let $T(\mathbf{X})$ be a [[Test Statistic]] for $H_0: \theta \in \omega_0$ in which larger values indicate stronger deviation from $H_0$, and let $t_{\text{obs}} = T(\mathbf{x})$ for the observed data $\mathbf{x}$. The p-value (observed significance level) is
> $$
> \begin{align}
> p(\mathbf{x}) = \sup_{\theta \in \omega_0} P_\theta\big(T(\mathbf{X}) \geq t_{\text{obs}}\big)
> \end{align}
> $$
> which is $P_{H_0}(T(\mathbf{X}) \geq t_{\text{obs}})$ for a [[Simple Hypothesis|simple]] null. Equivalently, for a nested family of level-$\alpha$ [[Critical Region|critical regions]] $C_\alpha$,
> $$
> \begin{align}
> p(\mathbf{x}) = \inf\{\alpha \in (0, 1) : \mathbf{x} \in C_\alpha\}
> \end{align}
> $$
> the smallest significance level at which the observed data lead to rejection.

Reject $H_0$ if $P$-value $\leq \alpha$. The smaller the value, the greater the evidence against $H_0$.

**Interpretation (the data-driven, Fisherian view).** Instead of fixing $\alpha$ first and checking whether the data land in $C_\alpha$, the question is reversed: "Given the specific data $\mathbf{x}$ I just observed, what is the probability under $H_0$ of observing something at least as extreme?" The p-value is a data-based significance level. Because $C_\alpha = \{\mathbf{x} : T(\mathbf{x}) \geq c_\alpha\}$ with $P_{H_0}(T(\mathbf{X}) \geq c_\alpha) = \alpha$,
$$
\begin{align}
T(\mathbf{x}) \geq c_\alpha \iff p(\mathbf{x}) \leq \alpha
\end{align}
$$
so $H_0$ is rejected if and only if $p \leq \alpha$, and retained if and only if $p > \alpha$. As $\alpha$ grows, the critical region expands, and the p-value is the exact boundary value of $\alpha$ at which it first touches the observed $\mathbf{x}$: it is a cutoff on the $\alpha$-axis. Anyone choosing a significance level $\alpha \geq p$ rejects $H_0$, and anyone choosing $\alpha < p$ does not.[^2]

# Types
- [[Mid P-Value]]
- Bootstrap p-value ([[Bootstrap Hypothesis Test]]).

# Properties
- Uniform under the null: if $H_0$ is simple and $T$ is continuous, then the random variable $P = p(\mathbf{X})$ satisfies $P \sim \text{Uniform}(0, 1)$ under $H_0$, since $P = 1 - F_{H_0}(T)$ ([[Probability Integral Transform]]); hence $P_{H_0}(P \leq \alpha) = \alpha$, and the test "reject if $p \leq \alpha$" has size exactly $\alpha$.
- For a discrete $T$ or a composite null, $P_\theta(P \leq \alpha) \leq \alpha$ for $\theta \in \omega_0$: the p-value is conservative (stochastically larger than uniform).
- For two-sided alternatives, "at least as extreme" is measured in both tails, e.g. $P_{H_0}(|T| \geq |t_{\text{obs}}|)$.
- It avoids the need for a [[Randomized Test]] with discrete statistics.
- It is not the probability that $H_0$ is true, and it does not measure the size of an effect; a small p-value can come from a trivial effect with a large sample. Current practice (e.g. the 2016 American Statistical Association statement) recommends reporting it alongside effect sizes and [[Confidence Interval|confidence intervals]] rather than as a bare reject/retain verdict.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=296)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=295)
