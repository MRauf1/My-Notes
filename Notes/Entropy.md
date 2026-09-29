---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Entropy[^1][^2]
> The entropy of a discrete random variable $x$ is the expected [[Information Content|information content]], i.e. the average amount of information transmitted when sending its value:
> $$
> \begin{align}
> \mathrm{H}[x] = -\sum_x p(x) \ln p(x)
> \end{align}
> $$
> measured in nats (natural log) or, with $\log_2$, in bits; the two differ by a factor of $\ln 2$. By convention $p \ln p = 0$ when $p = 0$, since $\lim_{p \to 0} p \ln p = 0$.

**Statistical-mechanics view.** Divide $N$ identical objects among bins, with $n_i$ objects in bin $i$. The number of ways to do so, ignoring rearrangements within each bin, is the **multiplicity** (weight of the macrostate)
$$
\begin{align}
W = \frac{N!}{\prod_i n_i!}, \qquad \mathrm{H} = \frac{1}{N}\ln W = \frac{1}{N}\ln N! - \frac{1}{N}\sum_i \ln n_i!
\end{align}
$$
Letting $N \to \infty$ with the fractions $n_i/N$ fixed and applying [[Stirling's Approximation]] $\ln N! \simeq N\ln N - N$ gives
$$
\begin{align}
\mathrm{H} = -\lim_{N \to \infty}\sum_i \left(\frac{n_i}{N}\right)\ln\left(\frac{n_i}{N}\right) = -\sum_i p_i \ln p_i
\end{align}
$$
A specific arrangement of objects is a **microstate**; the occupation fractions $n_i/N$ define a **macrostate**. Interpreting the bins as states $x_i$ of a random variable with $p(x_i) = p_i$ recovers the definition, so entropy measures disorder.[^3][^4]

# Properties
- $\mathrm{H} \geq 0$ since $0 \leq p_i \leq 1$, with minimum $0$ when one $p_i = 1$ and all others are $0$.[^5]
- Sharply peaked distributions have low entropy; spread-out ones have high entropy. Over $M$ states the maximum is attained by the uniform distribution $p(x_i) = 1/M$, giving $\mathrm{H} = \ln M$. This follows by maximizing $\tilde{\mathrm{H}} = -\sum_i p(x_i)\ln p(x_i) + \lambda\left(\sum_i p(x_i) - 1\right)$ with a Lagrange multiplier; the Hessian $\frac{\partial^2 \tilde{\mathrm{H}}}{\partial p(x_i)\,\partial p(x_j)} = -I_{ij}\frac{1}{p_i}$ is negative definite, confirming a maximum. It also follows from [[Jensen's Inequality]].[^6]
- By the [[Noiseless Coding Theorem]], entropy is a lower bound on the average number of bits needed to transmit the state of a random variable.
- The continuous analogue is [[Differential Entropy]]; entropy of a joint splits via [[Conditional Entropy]].
- Relative entropy between two distributions is the [[Kullback-Leibler Divergence]], and the [[Cross-Entropy Loss]] $-\sum_x p(x)\ln q(x)$ equals $\mathrm{H}[p] + \mathrm{KL}(p \| q)$.

[^1]: [Bishop, 2006, p. 49](zotero://open-pdf/library/items/5G99AZ8U?page=69&annotation=LKQQKPJK)
[^2]: [Bishop, 2006, p. 50](zotero://open-pdf/library/items/5G99AZ8U?page=70&annotation=94TEZGNG)
[^3]: [Bishop, 2006, p. 51](zotero://open-pdf/library/items/5G99AZ8U?page=71&annotation=ZNWGPTJN)
[^4]: [Bishop, 2006, p. 51](zotero://open-pdf/library/items/5G99AZ8U?page=71&annotation=I5MW6A2V)
[^5]: [Bishop, 2006, p. 51](zotero://open-pdf/library/items/5G99AZ8U?page=71&annotation=H8DJSDEC)
[^6]: [Bishop, 2006, p. 52](zotero://open-pdf/library/items/5G99AZ8U?page=72&annotation=KXSRZBFP)
