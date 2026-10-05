---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Residual Network as Ensemble (Unraveled Network)[^1]
> Substituting each line of a [[Residual Connection|residual network]] into the next "unravels" it into the input plus a sum of smaller networks:
> $$
> \begin{align}
> \mathbf{y} = \mathbf{x} + \mathrm{f}_1[\mathbf{x}] + \mathrm{f}_2\big[\mathbf{x} + \mathrm{f}_1[\mathbf{x}]\big] + \mathrm{f}_3\Big[\mathbf{x} + \mathrm{f}_1[\mathbf{x}] + \mathrm{f}_2\big[\mathbf{x} + \mathrm{f}_1[\mathbf{x}]\big]\Big] + \mathrm{f}_4\big[\,\cdots\,\big]
> \end{align}
> $$
> so a residual network can be interpreted as an [[Ensemble Learning|ensemble]] of shorter networks whose outputs are summed. Equivalently, $K$ residual blocks create $2^K$ paths with differing numbers of transformations between input and output (each block is either traversed or skipped).

# Properties
- **Empirical support** (Veit et al., 2016): deleting layers of a trained residual network (and hence a subset of paths) only modestly affects performance, whereas removing a layer of a purely sequential network (e.g. VGG) is catastrophic.[^2]
- **Effective paths are short**: gradients vanish along long paths. In a residual network with $54$ blocks, almost all gradient updates during training came from paths of length $5$ to $17$ blocks, which constitute only $0.45\%$ of all paths. Adding more blocks effectively adds more parallel short paths rather than making the network truly deeper.[^2]
- Each block appears in $2^{K-1}$ of the paths, including a direct path of length one, which is why the gradient for each block has an identity term and short chains that mitigate [[Shattered Gradients]].[^3]

[^1]: [Prince, p. 189](zotero://open-pdf/library/items/BWT7FYX5?page=203&annotation=28NMNQFK); [Prince, p. 191](zotero://open-pdf/library/items/BWT7FYX5?page=205&annotation=GMMY7LK5); [Prince, p. 191](zotero://open-pdf/library/items/BWT7FYX5?page=205&annotation=3Z4ZT9ZY)
[^2]: [Prince, p. 202](zotero://open-pdf/library/items/BWT7FYX5?page=216&annotation=D22LZIQU)
[^3]: [Prince, p. 191](zotero://open-pdf/library/items/BWT7FYX5?page=205&annotation=3Z4ZT9ZY)
