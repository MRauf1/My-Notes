---
tags:
  - psychology
  - behavioral_economics
---

# Definition
> [!info] Hyperbolic Discounting (Time Inconsistency)[^1]
> Valuing a reward $A$ delayed by $D$ as
> $$
> \begin{align}
> V(A, D) = \frac{A}{1 + kD}
> \end{align}
> $$
> (Mazur, 1987), which discounts steeply over short delays and gently over long ones. The way the brain evaluates rewards is inconsistent across time: we value the present more than the future.

# Properties
- **Preference reversal.** Under exponential discounting $V = A e^{-rD}$, the ratio of values of $A_1$ at delay $D$ and $A_2$ at delay $D + \Delta$ is $\frac{A_1}{A_2} e^{r\Delta}$, which is independent of $D$, so choices are consistent over time. Under hyperbolic discounting the ratio $\frac{A_1 (1 + k(D+\Delta))}{A_2 (1 + kD)}$ grows as $D \to 0$. A larger-later reward preferred from afar can therefore lose to a smaller-sooner one as both draw near. Compare the exponential [[Discount Factor]] of reinforcement learning.
- **Immediate- vs. delayed-return environments.** The brain evolved where actions deliver immediate, clear outcomes. Modern life, a delayed-return environment, emerged only recently (beginning with agriculture, dominant over the last few centuries).[^2]
- **Consequence for habits.** The costs of good habits come now and their benefits later; bad habits are the reverse. Hence the *Cardinal Rule of Behavior Change*: "What is immediately rewarded is repeated. What is immediately punished is avoided."[^3]
- **Remedy.** Add a little immediate pleasure to habits that pay off in the long run and a little immediate pain to those that don't. Choose immediate rewards that reinforce your identity.[^4] This is supported by evidence: earlier rewards for persisting increased intrinsic motivation more than delayed ones (Woolley and Fishbach, 2018).
- **Delayed gratification.** Clear cites research that people willing to delay gratification do better.[^5] A large replication of the marshmallow test found the link to later achievement about half as large as originally reported, and much smaller after controlling for family background and early cognitive ability (Watts, Duncan and Quan, 2018).
- **Risk perception.** We overestimate immediate but unlikely threats and underestimate distant but likely ones.[^6]
- Related: [[Commitment Device]], [[Law of Reward]], [[Willpower]].

[^1]: [Clear, p. 147](zotero://open-pdf/library/items/N7HGMVC4?page=147&annotation=VBSPIBDX); [p. 250](zotero://open-pdf/library/items/N7HGMVC4?page=250&annotation=S2GTCWUX)
[^2]: [Clear, p. 146](zotero://open-pdf/library/items/N7HGMVC4?page=146&annotation=JSVM9GUD); [p. 147](zotero://open-pdf/library/items/N7HGMVC4?page=147&annotation=2D99S5SR); [p. 147](zotero://open-pdf/library/items/N7HGMVC4?page=147&annotation=Y43PRIVY); [p. 250](zotero://open-pdf/library/items/N7HGMVC4?page=250&annotation=3VGB5ZXW)
[^3]: [Clear, p. 147](zotero://open-pdf/library/items/N7HGMVC4?page=147&annotation=7DEJAFBC); [p. 148](zotero://open-pdf/library/items/N7HGMVC4?page=148&annotation=TSKM695I); [p. 148](zotero://open-pdf/library/items/N7HGMVC4?page=148&annotation=65BZ76CV); [p. 148](zotero://open-pdf/library/items/N7HGMVC4?page=148&annotation=V7VUCLIR)
[^4]: [Clear, p. 149](zotero://open-pdf/library/items/N7HGMVC4?page=149&annotation=TS7SLCN2); [p. 149](zotero://open-pdf/library/items/N7HGMVC4?page=149&annotation=DNF62DLW); [p. 150](zotero://open-pdf/library/items/N7HGMVC4?page=150&annotation=HXKFKBCB)
[^5]: [Clear, p. 148](zotero://open-pdf/library/items/N7HGMVC4?page=148&annotation=4AFG25VA); [p. 148](zotero://open-pdf/library/items/N7HGMVC4?page=148&annotation=LWGKTRGH)
[^6]: [Clear, p. 251](zotero://open-pdf/library/items/N7HGMVC4?page=251&annotation=FZZI8624); [p. 251](zotero://open-pdf/library/items/N7HGMVC4?page=251&annotation=7RV2GV6C)
