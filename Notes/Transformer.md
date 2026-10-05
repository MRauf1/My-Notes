---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Transformer[^1]
> A network that processes a sequence of tokens by passing their embeddings $\mathbf{X} \in \mathbb{R}^{D \times N}$ through a series of $K$ [[Transformer Layer|transformer layers]]. A typical NLP pipeline is
> $$
> \begin{align}
> \text{text} \xrightarrow{\text{tokenizer}} \text{tokens} \xrightarrow{\ \boldsymbol{\Omega}_e\ } \mathbf{X} \xrightarrow{\text{(+ positional encoding)}} \text{transformer layers} \xrightarrow{} \text{output embeddings}
> \end{align}
> $$
> ([[Tokenization]], [[Word Embedding]], [[Positional Encoding]]).

# Types
- [[Transformer Encoder]]: transforms text embeddings into a representation supporting a variety of tasks (e.g. BERT).
- [[Transformer Decoder]]: predicts the next token to continue the input text (e.g. GPT3).
- [[Encoder-Decoder Transformer]]: converts one sequence into another (sequence-to-sequence tasks such as machine translation).
- [[Vision Transformer]]: applies an encoder to image patches.

# Properties
- Built on [[Self-Attention|dot-product self-attention]], which shares parameters across positions (so it handles inputs of differing lengths) and connects tokens with strengths that depend on the tokens themselves.[^2]
- **Quadratic complexity**: in an encoder every token interacts with every other, so computation scales as $\mathcal{O}(N^2)$ in the sequence length; a decoder has about half as many interactions but is still quadratic. This limits sequence length and motivates [[Sparse Attention]].[^3]
- **Training is difficult** and requires both [[Learning Rate Warm-Up|learning rate warm-up]] and [[Adam]]. Without warm-up the gradients vanish and the Adam updates shrink (Xiong et al., 2020; Huang et al., 2020). Interacting causes:[^4]
	- [[Residual Connection|residual connections]] cause [[Exploding Gradients|exploding gradients]], which normalization prevents;
	- [[Layer Normalization|LayerNorm]] is used instead of [[Batch Normalization|BatchNorm]] because NLP statistics vary greatly between batches; placed outside the residual blocks it makes gradients shrink backwards through the network ([[Transformer Layer]]);
	- the relative weight of the residual and self-attention paths changes with depth at initialization ([[Residual Network Variance at Initialization]]);
	- gradients for the query and key parameters are smaller than for the value parameters (Liu et al., 2020), which necessitates Adam.
- Usually pre-trained with [[Self-Supervised Learning|self-supervision]] on huge corpora, then fine-tuned ([[Transfer Learning]]).

[^1]: [Prince, p. 216](zotero://open-pdf/library/items/BWT7FYX5?page=230&annotation=897QSUBG); [Prince, p. 218](zotero://open-pdf/library/items/BWT7FYX5?page=232&annotation=HPHSQVWE); [Prince, p. 218](zotero://open-pdf/library/items/BWT7FYX5?page=232&annotation=NY3HXNU5); [Prince, p. 219](zotero://open-pdf/library/items/BWT7FYX5?page=233&annotation=9RXDP7GE)
[^2]: [Prince, p. 208](zotero://open-pdf/library/items/BWT7FYX5?page=222&annotation=XMS46XET)
[^3]: [Prince, p. 227](zotero://open-pdf/library/items/BWT7FYX5?page=241&annotation=8DBPLMGU); [Prince, p. 227](zotero://open-pdf/library/items/BWT7FYX5?page=241&annotation=PRM9WBFC)
[^4]: [Prince, p. 237](zotero://open-pdf/library/items/BWT7FYX5?page=251&annotation=X6CE7KIZ)
