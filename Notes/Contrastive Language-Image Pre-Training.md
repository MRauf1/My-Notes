---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Contrastive Language-Image Pre-Training (CLIP)[^1]
> Joint training of an image encoder and a text encoder on $N$ image-caption pairs using a contrastive pre-training task (Radford et al., 2021). The model produces an $N \times N$ matrix of compatibility scores between images and captions, and the loss pushes the $N$ correct pairs (the diagonal) to high scores and the $N^2 - N$ incorrect pairs to low scores.

# Properties
- A contrastive form of [[Self-Supervised Learning]] that needs only naturally co-occurring image-text pairs, not manual labels.
- The scores are typically [[Cosine Similarity|cosine similarities]] of the normalized embeddings scaled by a learned temperature, and the loss is a symmetric [[Cross-Entropy Loss|cross-entropy]] over the rows (image→text) and columns (text→image) of the matrix.[^2]
- The learned joint embedding enables text-conditional image generation: Ramesh et al. (2021, 2022) train a diffusion decoder to invert the CLIP image encoder.[^1]

[^1]: [Prince, p. 238](zotero://open-pdf/library/items/BWT7FYX5?page=252&annotation=J7LMNWCC)
[^2]: Added from general knowledge.
