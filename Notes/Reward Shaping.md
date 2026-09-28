---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Reward Shaping[^1]
> A form of [[Shaping (Machine Learning)|shaping]] in which the full-scale problem is kept but bonus rewards ("pseudorewards", "shaping rewards", i.e. incentives) are added to point the learner in the right direction or encourage behaviours correlated with success.

# Properties
- Incentives are playing with fire: one risks "the folly of rewarding A, while hoping for B" (Kerr). RL agents, like children, find loopholes, and with vast compute and trials they will exploit any flaw ([[Reward Hacking]]).[^2]
- **Potential-based shaping** (Ng, Harada, Russell): shaping is safe iff it forms a "conservative field", i.e. the bonus is a difference of a potential $\Phi$ over states,
$$\begin{align}
F(s, a, s') = \gamma\, \Phi(s') - \Phi(s),
\end{align}$$
so that returning to a starting state nets zero. This is necessary and sufficient for the optimal policy under shaped reward to coincide with that under the original reward.[^3]
- "It is better to design performance measures according to what one actually wants in the environment, rather than according to how one thinks the agent should behave": reward states of the world (progress toward the goal), not the agent's actions.[^4]
- **Evolution as reward designer**: evolution gave us rewards not for reproductive success directly but for its *predictors*, a two-level optimisation in which evolution shapes what we find rewarding and we optimise those rewards; what matters is the interaction between a reward function and the behaviour it engenders.[^5]
- Distinguishing sharply between what you want and what you reward is part of the solution.[^6]

[^1]: [Christian, 2021, p. 164](zotero://open-pdf/library/items/P27SWKW4?page=164&annotation=IX8SLWX7)
[^2]: [Christian, 2021, p. 165](zotero://open-pdf/library/items/P27SWKW4?page=165&annotation=THRHW732); [Christian, 2021, p. 167](zotero://open-pdf/library/items/P27SWKW4?page=167&annotation=T92TDY64); [Christian, 2021, p. 167](zotero://open-pdf/library/items/P27SWKW4?page=167&annotation=MDQS46TY)
[^3]: [Christian, 2021, p. 170](zotero://open-pdf/library/items/P27SWKW4?page=170&annotation=DI67RJP3); [Christian, 2021, p. 170](zotero://open-pdf/library/items/P27SWKW4?page=170&annotation=LP9AFILG)
[^4]: [Christian, 2021, p. 170](zotero://open-pdf/library/items/P27SWKW4?page=170&annotation=RGP386FF)
[^5]: [Christian, 2021, p. 171](zotero://open-pdf/library/items/P27SWKW4?page=171&annotation=62ZM38H8); [Christian, 2021, p. 173](zotero://open-pdf/library/items/P27SWKW4?page=173&annotation=CKWK87RA); [Christian, 2021, p. 174](zotero://open-pdf/library/items/P27SWKW4?page=174&annotation=GD2DW5YZ); [Christian, 2021, p. 174](zotero://open-pdf/library/items/P27SWKW4?page=174&annotation=XB7FCXQZ)
[^6]: [Christian, 2021, p. 175](zotero://open-pdf/library/items/P27SWKW4?page=175&annotation=GTCXV6JU)
