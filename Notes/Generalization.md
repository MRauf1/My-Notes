---
tags: computer_science, computer_vision
---

# Definition

...

When [[Machine Learning|learning]] a model, there are three factors that guide the model towards a solution.[^1]

1) [[Hypothesis Space|Hypothesis Space]] places a hard constraint on which types of [[Function|functions]] can be picked.
2) [[Bayes' Theorem|Priors]] place a soft constraint on which models are preferred. Use priors when they are good guesses to the underlying solution as overreliance on priors means ignoring more of the data.
3) Data places a soft constraints on which models fit the (training) data well (low approximation error). The more data one has, the less they have to rely on modeling tools.

What can be achieved by one method can be achieved by the others (note the hard/soft constraints though). In other words, as [[Ilya Sutskever|Ilya Sutskever]] puts it, "methods...are extra training data in disguise".

![[Pasted image 20250611155435.png]]

[^1]: https://visionbook.mit.edu/problem_of_generalization.html