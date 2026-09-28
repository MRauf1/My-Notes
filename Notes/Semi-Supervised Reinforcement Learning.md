---
tags:
  - computer_science
  - philosophy
---

# Definition
> [!info] Semi-Supervised Reinforcement Learning[^1]
> A variant of [[Reinforcement Learning|reinforcement learning]] in which the agent can only see its reward on a small fraction of timesteps or episodes, yet its performance is still evaluated on the reward from all episodes, so it must optimise total reward based only on the limited reward samples it observes.

# Types
- *Active setting*: the agent may request to see the reward on whichever episodes or timesteps are most useful for learning, aiming to be economical in both the number of feedback requests and total training time. Considered the most interesting setting.[^2]
- *Random setting*: the reward is visible on a random subset of timesteps or episodes.[^2]
- Intermediate possibilities between the two.[^2]

# Properties
- The reinforcement-learning analogue of [[Semi-Supervised Learning|semi-supervised learning]], with reward playing the role of labels.
- Baseline: ignore unlabelled episodes and run ordinary RL on the labelled ones, which generally learns very slowly. The challenge is to exploit unlabelled episodes to learn almost as quickly and robustly as if all episodes were labelled.[^3]
- An important subtask is identifying proxies that predict the reward, and learning the conditions under which those proxies are valid.[^4]
- Approaches:[^5]
	- *Supervised reward learning*: train a model to predict reward from state, then use it to estimate reward on unlabelled episodes.
	- *Semi-supervised or active reward learning*: combine the above with traditional semi-supervised or active learning to learn the reward estimator faster.
	- *Unsupervised value iteration*: use observed transitions of unlabelled episodes to make more accurate Bellman updates, as in [[Value Iteration]].
	- *Unsupervised model learning*: in model-based RL, use observed transitions of unlabelled episodes to improve the quality of the model.
- A strong approach would be a first step towards [[Scalable Oversight]] and mitigating other AI safety problems, and would be useful for RL independently of safety.[^6]

[^1]: [Amodei et al., 2016, p. 11](zotero://open-pdf/library/items/JKJMXPTZ?page=11&annotation=723JIFE6)
[^2]: [Amodei et al., 2016, p. 12](zotero://open-pdf/library/items/JKJMXPTZ?page=12&annotation=USN3HN5D)
[^3]: [Amodei et al., 2016, p. 12](zotero://open-pdf/library/items/JKJMXPTZ?page=12&annotation=VUH4NUNH)
[^4]: [Amodei et al., 2016, p. 12](zotero://open-pdf/library/items/JKJMXPTZ?page=12&annotation=WYG5BM85)
[^5]: [Amodei et al., 2016, p. 12](zotero://open-pdf/library/items/JKJMXPTZ?page=12&annotation=WXIZBNVD); [Amodei et al., 2016, p. 12](zotero://open-pdf/library/items/JKJMXPTZ?page=12&annotation=B84559P9); [Amodei et al., 2016, p. 12](zotero://open-pdf/library/items/JKJMXPTZ?page=12&annotation=ZUP8DS4Y); [Amodei et al., 2016, p. 12](zotero://open-pdf/library/items/JKJMXPTZ?page=12&annotation=UZQCNTTJ); [Amodei et al., 2016, p. 12](zotero://open-pdf/library/items/JKJMXPTZ?page=12&annotation=Q5VEBE6J)
[^6]: [Amodei et al., 2016, p. 13](zotero://open-pdf/library/items/JKJMXPTZ?page=13&annotation=N92Z2VCL)
