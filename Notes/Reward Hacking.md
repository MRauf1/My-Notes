---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Reward Hacking[^1]
> An [[Accident (Machine Learning)|accident]] in which the formal [[Reward Function|reward]] or [[Objective Function|objective function]], which is only an attempt to capture the designer's informal intent, admits a clever "easy" solution that is valid in a literal sense and formally maximises it, but perverts the spirit of the designer's intent (i.e. the objective is "gamed"). It generalises the wireheading problem, in which an agent tampers directly with its own reward signal.

# Properties
- From the agent's point of view a reward hack is not a bug but simply how the environment works, and hence a valid strategy like any other (e.g. exploiting a buffer overflow in the reward implementation).[^2]
- Pursuit of reward hacks leads to coherent but unanticipated behaviour, with potential for harm in real-world systems.[^2]
- Causes:[^3]
	- *Partially observed goals*: the reward can only depend on the agent's imperfect perceptions, not the true world state. A reward function over actions and observations equivalent to the true objective always exists (by reducing the POMDP to a belief-state [[Markov Decision Process|MDP]]), but it usually involves complicated long-term dependencies and is prohibitively hard to use in practice.
	- *Complicated systems*: the probability of a viable hack grows greatly with the complexity of the agent and its available strategies.
	- *Abstract rewards*: sophisticated rewards referring to abstract concepts (e.g. learned by a neural network) are vulnerable to adversarial counterexamples.
	- *[[Goodhart's Law]]*: a proxy that correlates with task success in normal use stops doing so once it is strongly optimised.
	- *Feedback loops*: the objective contains a self-amplifying component that ends up dominating the designer's intent.
	- *Environmental embedding*: the reward is physically implemented within the environment, so a sufficiently capable agent could tamper with it (wireheading).
- Rather than patching individual failures, wrong objectives are better viewed as emerging from general causes that make choosing the right objective hard; mitigating these causes is a valuable safety contribution.[^4]
- Approaches:[^4]
	- *Adversarial reward functions*: treat the reward function as an agent that actively searches for scenarios the ML system claims are high reward but a human labels low reward.
	- *Model lookahead*: in model-based RL, give reward based on anticipated future states rather than the present one, penalising plans to replace the reward function.
	- *Adversarial blinding*: use adversarial techniques to blind the model to certain variables, e.g. how the reward is generated.
	- *Careful engineering*: formal verification, practical testing, and sandboxing of the agent.
	- *Reward capping*: cap the maximum possible reward to prevent extreme, low-probability, high-payoff strategies.
	- *Counterexample resistance*: use adversarial training, architectural choices, and uncertainty estimation against adversarial counterexamples to learned rewards.
	- *Multiple rewards*: combine several differently implemented rewards (e.g. averaging or taking the minimum), which are harder to hack simultaneously.
	- *Reward pretraining*: train a fixed reward function ahead of time via supervised learning from interaction, so it cannot be influenced by the agent's later behaviour.
	- *Variable indifference*: make the agent optimise some variables while being indifferent to (not steering) others.
	- *Trip wires*: deliberately introduce plausible vulnerabilities that the agent can exploit, and monitor them to detect reward hacking attempts.
- A central concern of the [[Value Alignment Problem]].

[^1]: [Amodei et al., 2016, p. 2](zotero://open-pdf/library/items/JKJMXPTZ?page=2&annotation=YVHFFCBY); [Amodei et al., 2016, p. 7](zotero://open-pdf/library/items/JKJMXPTZ?page=7&annotation=I99VXPQV)
[^2]: [Amodei et al., 2016, p. 7](zotero://open-pdf/library/items/JKJMXPTZ?page=7&annotation=Q33DS6BL); [Amodei et al., 2016, p. 7](zotero://open-pdf/library/items/JKJMXPTZ?page=7&annotation=I99VXPQV)
[^3]: [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=K6D84YDC); [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=IRVMNAPT); [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=3BWSG8UJ); [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=RADMPIXJ); [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=PEKTHT23); [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=ZUHYKAA6); [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=UZFNLYTW); [Amodei et al., 2016, p. 8](zotero://open-pdf/library/items/JKJMXPTZ?page=8&annotation=CEFAAQQ3); [Amodei et al., 2016, p. 9](zotero://open-pdf/library/items/JKJMXPTZ?page=9&annotation=ACSZFU4E)
[^4]: [Amodei et al., 2016, p. 9](zotero://open-pdf/library/items/JKJMXPTZ?page=9&annotation=Z7I7WIH9); [Amodei et al., 2016, p. 9](zotero://open-pdf/library/items/JKJMXPTZ?page=9&annotation=AJCY7C5Q); [Amodei et al., 2016, p. 9](zotero://open-pdf/library/items/JKJMXPTZ?page=9&annotation=3V84C3FP); [Amodei et al., 2016, p. 10](zotero://open-pdf/library/items/JKJMXPTZ?page=10&annotation=YTI8XYWC); [Amodei et al., 2016, p. 10](zotero://open-pdf/library/items/JKJMXPTZ?page=10&annotation=7BHUS8X7); [Amodei et al., 2016, p. 10](zotero://open-pdf/library/items/JKJMXPTZ?page=10&annotation=XKK42YIG); [Amodei et al., 2016, p. 10](zotero://open-pdf/library/items/JKJMXPTZ?page=10&annotation=2L4787MF); [Amodei et al., 2016, p. 10](zotero://open-pdf/library/items/JKJMXPTZ?page=10&annotation=BZXBWF25); [Amodei et al., 2016, p. 10](zotero://open-pdf/library/items/JKJMXPTZ?page=10&annotation=ID762BKA); [Amodei et al., 2016, p. 10](zotero://open-pdf/library/items/JKJMXPTZ?page=10&annotation=7K5U3HFM); [Amodei et al., 2016, p. 11](zotero://open-pdf/library/items/JKJMXPTZ?page=11&annotation=PWBLI8FW)
