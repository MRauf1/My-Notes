---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Hash Code
> An integer, in the same $w$-bit range used by a [[Hash Table]], associated with a non-integer data item (a string, object, array, or other compound structure) so that the hash table can operate on it as if it were an integer.[^1]

A hash code mapping should satisfy: (1) if $x$ and $y$ are equal, then $x.\text{hashCode}()$ and $y.\text{hashCode}()$ are equal; (2) if $x$ and $y$ are not equal, then $\Pr\{x.\text{hashCode}() = y.\text{hashCode}()\}$ should be small (close to $1/2^w$). Property (1) guarantees that a value equal to one already stored will be found; property (2) minimizes collisions caused by the conversion itself, keeping unequal objects likely to land at different table locations.[^1]

# Types
- **Primitive types**: values like `char`, `byte`, `int`, and `float` already have a binary representation of $w$ or fewer bits, which is used directly as the integer hash code — equal values necessarily get equal hash codes, and different values get different ones.[^2]
- **Compound objects with a fixed number of parts**: for an object made of parts $P_0, \dots, P_{r-1}$ with hash codes $x_0, \dots, x_{r-1}$, choose mutually independent random $w$-bit integers $z_0, \dots, z_{r-1}$ and a random odd $2w$-bit integer $z$, and combine them with $$h(x_0, \dots, x_{r-1}) = \left(z \left(\sum_{i=0}^{r-1} z_i x_i\right) \bmod 2^{2w}\right) \operatorname{div} 2^w.$$ The final multiplication by $z$ and division by $2^w$ applies [[Multiplicative Hashing]] to reduce the $2w$-bit intermediate sum to a $w$-bit result.[^3]
- **Sequences of variable length**: the fixed-arity combination above requires one random $z_i$ per component and so breaks down when the number of components varies; see [[Polynomial Hash Code]] for a construction that instead evaluates a polynomial over a prime field.[^4]

# Properties
> [!abstract] Theorem 5.3[^5]
> Let $x_0, \dots, x_{r-1}$ and $y_0, \dots, y_{r-1}$ each be sequences of $w$-bit integers in $\{0, \dots, 2^w-1\}$, with $x_i \neq y_i$ for at least one index $i \in \{0, \dots, r-1\}$. Then $\Pr\{h(x_0, \dots, x_{r-1}) = h(y_0, \dots, y_{r-1})\} \leq 3/2^w$.

[^1]: [Morin, p. 117](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 117](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 118](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 119](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 118](zotero://select/library/items/HYS8NDAB)
