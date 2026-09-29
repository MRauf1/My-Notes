---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Three Approaches to Decision Problems[^1][^2]
> The problem of predicting $t$ (or a class $\mathcal{C}_k$) from $\mathbf{x}$ splits into an **inference stage**, which learns probabilities from training data, and a **decision stage**, which uses them to act optimally. In decreasing order of complexity:
> 1. **[[Generative Model|Generative]]**: infer the class-conditional densities $p(\mathbf{x} | \mathcal{C}_k)$ and priors $p(\mathcal{C}_k)$ (or the joint $p(\mathbf{x}, \mathcal{C}_k)$ directly), then obtain the posterior via [[Bayes' Theorem]],
> $$
> \begin{align}
> p(\mathcal{C}_k | \mathbf{x}) = \frac{p(\mathbf{x} | \mathcal{C}_k)\,p(\mathcal{C}_k)}{p(\mathbf{x})}, \qquad p(\mathbf{x}) = \sum_k p(\mathbf{x} | \mathcal{C}_k)\,p(\mathcal{C}_k)
> \end{align}
> $$
> 2. **[[Discriminative Model|Discriminative]]**: infer the posterior $p(\mathcal{C}_k | \mathbf{x})$ directly, then apply decision theory.
> 3. **[[Discriminant Function]]**: learn a function $f(\mathbf{x})$ that maps inputs directly to decisions.
>
> For regression the analogous approaches are:[^3]
> 1. infer the joint $p(\mathbf{x}, t)$, normalize to $p(t | \mathbf{x})$, then marginalize to the conditional mean $\mathbb{E}[t | \mathbf{x}]$;
> 2. infer $p(t | \mathbf{x})$ directly, then marginalize to the conditional mean;
> 3. find a [[Regression Function|regression function]] $y(\mathbf{x})$ directly from the training data.

The joint distribution $p(\mathbf{x}, t)$ is the most complete summary of the uncertainty; determining it is **inference** and is typically the hard part, while the decision stage is generally simple, even trivial, once inference is solved.[^4]

# Properties
- Approach 1 is the most demanding: with high-dimensional $\mathbf{x}$, class-conditional densities need large training sets. The priors $p(\mathcal{C}_k)$, however, can often be estimated from the class fractions in the training set.[^5]
- Approach 1 also yields the marginal $p(\mathbf{x})$, enabling [[Novelty Detection|novelty detection]] of inputs where predictions may be unreliable.
- If only decisions are needed, approach 1 can be wasteful; approach 2 gives the posteriors directly.[^6]
- **Compensating for class priors**: after training on an artificially balanced data set, divide the posteriors by the class fractions of that data set, multiply by the class fractions of the target population, and renormalize; this follows since posteriors are proportional to priors, and requires approaches 1 or 2.[^7]
- **Combining models**: posteriors from models of separate inputs (e.g. images $\mathbf{x}_I$ and blood tests $\mathbf{x}_B$) combine under the conditional independence $p(\mathbf{x}_I, \mathbf{x}_B | \mathcal{C}_k) = p(\mathbf{x}_I | \mathcal{C}_k)\,p(\mathbf{x}_B | \mathcal{C}_k)$, giving $p(\mathcal{C}_k | \mathbf{x}_I, \mathbf{x}_B) \propto p(\mathcal{C}_k | \mathbf{x}_I)\,p(\mathcal{C}_k | \mathbf{x}_B)/p(\mathcal{C}_k)$; this is the [[Naive Bayes Classifier|naive Bayes]] assumption, under which the marginal $p(\mathbf{x}_I, \mathbf{x}_B)$ typically does not factorize.[^8]
- The relative merits for regression follow the same lines as for classification.

[^1]: [Bishop, 2006, p. 43](zotero://open-pdf/library/items/5G99AZ8U?page=63&annotation=XZ9NVEBU)
[^2]: [Bishop, 2006, p. 43](zotero://open-pdf/library/items/5G99AZ8U?page=63&annotation=I9CU6JKG)
[^3]: [Bishop, 2006, p. 47](zotero://open-pdf/library/items/5G99AZ8U?page=67&annotation=IBH2LDDG)
[^4]: [Bishop, 2006, p. 38](zotero://open-pdf/library/items/5G99AZ8U?page=58&annotation=8C8T4EIF)
[^5]: [Bishop, 2006, p. 43](zotero://open-pdf/library/items/5G99AZ8U?page=63&annotation=A5PJ8XMD)
[^6]: [Bishop, 2006, p. 44](zotero://open-pdf/library/items/5G99AZ8U?page=64&annotation=FNCQYKUP)
[^7]: [Bishop, 2006, p. 45](zotero://open-pdf/library/items/5G99AZ8U?page=65&annotation=6SKI8QAQ)
[^8]: [Bishop, 2006, p. 46](zotero://open-pdf/library/items/5G99AZ8U?page=66&annotation=A6H63P2K)
