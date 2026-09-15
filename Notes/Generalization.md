---
tags:
  - computer_science
  - computer_vision
---

# Definition

...

When [[Machine Learning|learning]] a model, there are three factors that guide the model towards a solution.[^1]

1) [[Hypothesis Space|Hypothesis Space]] places a hard constraint on which types of [[Function|functions]] can be picked.
2) [[Bayes' Theorem|Priors]] place a soft constraint on which models are preferred. Use priors when they are good guesses to the underlying solution as overreliance on priors means ignoring more of the data.
3) Data places a soft constraints on which models fit the (training) data well (low approximation error). The more data one has, the less they have to rely on modeling tools.

What can be achieved by one method can be achieved by the others (note the hard/soft constraints though). In other words, as [[Ilya Sutskever|Ilya Sutskever]] puts it, "methods...are extra training data in disguise".

![[Pasted image 20250611155435.png]]

![[Needle in Haystack of Hypotheses.png]]

# Properties
- Visualized as searching for a "needle of truth" within the full space of mappings $\mathcal{X} \to \mathcal{Y}$: the [[Hypothesis Space]] rules out most of this space entirely, the data isolates a region of high likelihood, and the prior isolates a region of high probability a priori; a learning algorithm that maximizes likelihood times prior finds a solution in the overlap of these two regions.
- [[The Bitter Lesson (Sutton)|Sutton's Bitter Lesson]] can be framed with these same three tools: hand-designed, human priors tend to eventually be outperformed by simply providing more data and more compute to a more general-purpose hypothesis space and learning method. In the terms of this chapter, Sutton is arguing that, historically, the "soft constraint" of a strong human-authored prior has been a worse long-run bet than relaxing that prior and instead scaling the "data" and "hypothesis space" tools, since general methods that hardly rely on hand-crafted priors tend to make better use of additional compute and data than niche methods do.

[^1]: https://visionbook.mit.edu/problem_of_generalization.html