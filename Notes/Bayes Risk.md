---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Bayes Risk
> For a decision rule $\delta$, a [[Loss Function|loss]] $L(\theta, \delta(x))$, and a prior $p(\theta)$, the Bayes risk is the loss integrated over the joint distribution $p(\theta, x)$. By [[Fubini's Theorem]], it can be computed in either order:
> $$
> \begin{align}
> r(\delta) = \int \underbrace{\left[\int L(\theta, \delta(x))\,p(x \mid \theta)\,dx\right]}_{\text{frequentist risk } R(\theta, \delta)} p(\theta)\,d\theta = \int \underbrace{\left[\int L(\theta, \delta(x))\,p(\theta \mid x)\,d\theta\right]}_{\text{posterior expected loss}} p(x)\,dx
> \end{align}
> $$

- Integrating over $x$ first gives the frequentist [[Risk Function (Statistics)|risk function]] $R(\theta, \delta)$, one curve over $\theta$.
- Integrating over $\theta$ first gives the Bayesian posterior expected loss, one number for each dataset.

The inner posterior expected loss can be minimized separately for every $x$, and $p(x) \geq 0$. So the rule that minimizes it pointwise, the [[Bayes Estimator]], also minimizes the prior-averaged frequentist risk $r(\delta)$. This is the exact link between the two frameworks ([[Frequentist vs Bayesian Inference]]).

# Properties
- Collapses the risk curve into one number by averaging it against the prior. The frequentist alternative, the worst case $\max_\theta R(\theta, \delta)$, gives the [[Minimax Decision Rule]].
- The prior that maximizes the minimal Bayes risk is least favorable. The Bayes rule for it is minimax.
- Needs $L \geq 0$ (Tonelli) or absolute integrability (Fubini) for the two orders to agree.
