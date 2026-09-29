---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!abstract] Noiseless Coding Theorem (Shannon, 1948)[^1]
> The [[Entropy|entropy]] of a random variable is a lower bound on the average number of bits needed to transmit its state.

# Properties
- The bound is approached by assigning shorter codes to more probable states: an optimal code gives state $x$ a length of about $-\log_2 p(x)$ bits, its [[Information Content|information content]].
- Coding with a model $q$ instead of the true $p$ costs an average of $\mathrm{KL}(p \| q)$ extra nats, so the best compression requires knowing the true distribution; this ties data compression to [[Density Estimation]] ([[Kullback-Leibler Divergence]]).

[^1]: [Bishop, 2006, p. 50](zotero://open-pdf/library/items/5G99AZ8U?page=70&annotation=DLLUHG25)
