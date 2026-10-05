---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Positional Encoding[^1]
> Information about token order injected into a [[Transformer]], needed because [[Self-Attention|self-attention]] is [[Equivariant Function|equivariant]] to permutations of its inputs and so ignores order (e.g. "The woman ate the raccoon" vs. "The raccoon ate the woman").

# Types
- **Absolute positional encoding**: a matrix $\boldsymbol{\Pi} \in \mathbb{R}^{D \times N}$ with a distinct column for each position is added to the data, $\mathbf{X} \leftarrow \mathbf{X} + \boldsymbol{\Pi}$. It can be hand-chosen or learned, and added at the network input or at every layer; sometimes it is added only when computing the queries and keys, not the values.[^2]
	- **Sinusoidal (predefined)**: the original transformer (Vaswani et al., 2017) used sinusoids of geometrically spaced frequencies; for position $n$ and dimension index $i$,
	  $$
	  \begin{align}
	  \Pi_{2i,\,n} = \sin\left(\frac{n}{10000^{2i/D}}\right), \qquad \Pi_{2i+1,\,n} = \cos\left(\frac{n}{10000^{2i/D}}\right).
	  \end{align}
	  $$
	  It extends to any $N$.[^3]
	- **Learned**: used by e.g. GPT3, BERT, and the [[Vision Transformer]].
- **Relative positional encoding**: the absolute position of a word matters much less than the offset between two words (the input may be a fragment, a sentence, or many sentences). A parameter $\pi_{a,b}$ is learned for each offset between key position $a$ and query position $b$ and is used to modify the attention matrix, by adding, multiplying, or otherwise altering it.[^4]

# Properties
- **Adding vs. concatenating**: since usually $D > N$, the encodings lie in a subspace of $\mathbb{R}^D$; because the word embeddings are learned, the network can in principle keep words and positions in orthogonal subspaces and recover the positional component as needed.[^5]
- **Sinusoidal properties**: (i) the relative position of two encodings is recoverable by a linear operation, since for each frequency the pair $(\sin, \cos)$ at position $n + k$ is a rotation of the pair at $n$ by an angle depending only on $k$; (ii) the [[Dot Product|dot product]] between encodings generally decreases with the distance between positions.[^5]
- Learned encodings in GPT3 and BERT show a [[Cosine Similarity|cosine similarity]] that generally declines with relative distance but also has a periodic component (Wang et al., 2020).[^5]

[^1]: [Prince, p. 213](zotero://open-pdf/library/items/BWT7FYX5?page=227&annotation=QUSJZKJ7); [Prince, p. 213](zotero://open-pdf/library/items/BWT7FYX5?page=227&annotation=LS2XE8XW)
[^2]: [Prince, p. 213](zotero://open-pdf/library/items/BWT7FYX5?page=227&annotation=YK3749KS)
[^3]: [Prince, p. 213](zotero://open-pdf/library/items/BWT7FYX5?page=227&annotation=LS2XE8XW); formula from Vaswani et al. (2017).
[^4]: [Prince, p. 214](zotero://open-pdf/library/items/BWT7FYX5?page=228&annotation=W6EX2A7Q)
[^5]: [Prince, p. 236](zotero://open-pdf/library/items/BWT7FYX5?page=250&annotation=DQHYGD7E)
