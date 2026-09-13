---
tags:
  - mathematics
  - pre_calculus
---

# Definition
> [!info] Definition 1 (Inequality Sign Change)[^1]
> Given an [[Inequality]] $a \diamond b$ (where $\diamond \in \{<, \leq, >, \geq, \neq\}$) and a [[Function|function]] $f$ defined on an [[Interval Notation|interval]] containing $a, b$, applying $f$ to both sides of the inequality preserves or reverses the direction of $\diamond$ depending on the monotonicity (or injectivity) of $f$.

# Types
## Strictly Increasing
- **Strictly increasing, strict premise (preserved, strict):** If $f$ is [[Increasing Function|strictly increasing]] and $a < b$, then $f(a) < f(b)$.
- **Strictly increasing, weak premise (preserved, weak):** If $f$ is [[Increasing Function|strictly increasing]] and $a \leq b$, then $f(a) \leq f(b)$.

## Strictly Decreasing
- **Strictly decreasing, strict premise (reversed, strict):** If $f$ is [[Decreasing Function|strictly decreasing]] and $a < b$, then $f(a) > f(b)$.
- **Strictly decreasing, weak premise (reversed, weak):** If $f$ is [[Decreasing Function|strictly decreasing]] and $a \leq b$, then $f(a) \geq f(b)$.

## Non-Decreasing
- **Nondecreasing, weak premise (preserved, weak):** If $f$ is [[Non-Decreasing Function|non-decreasing]] (i.e. $a < b \implies f(a) \leq f(b)$ for all $a, b$ in the interval) and $a \leq b$, then $f(a) \leq f(b)$.
- **Nondecreasing, strict premise (preserved, weak conclusion):** If $f$ is [[Non-Decreasing Function|non-decreasing]] and $a < b$, then only $f(a) \leq f(b)$ is guaranteed; the strict premise does not force a strict conclusion, since $f$ is permitted to be flat.

## Non-Increasing
- **Nonincreasing, weak premise (reversed, weak):** If $f$ is nonincreasing (i.e. $a < b \implies f(a) \geq f(b)$ for all $a, b$ in the interval) and $a \leq b$, then $f(a) \geq f(b)$.
- **Nonincreasing, strict premise (reversed, weak conclusion):** If $f$ is nonincreasing and $a < b$, then only $f(a) \geq f(b)$ is guaranteed, for the same reason as the nondecreasing case.

## Constant Function
- **Constant function (any premise, exact equality):** If $f$ is constant on the interval (i.e. $f(a) = f(b)$ for all $a, b$ in it), then $f(a) = f(b)$ regardless of whether the premise is $a < b$, $a \leq b$, $a > b$, or $a \geq b$. This is not an independent case: a constant function is simultaneously [[Non-Decreasing Function|non-decreasing]] and nonincreasing, so both $f(a) \leq f(b)$ and $f(a) \geq f(b)$ hold at once, forcing the strictly stronger conclusion $f(a) = f(b)$.

## Equal
- **Equal inputs (preserved trivially):** If $a = b$, then $f(a) = f(b)$ for any [[Function|function]] $f$, regardless of monotonicity, since $f$ is well-defined.

## Not Equal
- **Injective function, not-equal premise (preserved):** If $f$ is injective on the interval — guaranteed whenever $f$ is [[Increasing Function|strictly increasing]] or [[Decreasing Function|strictly decreasing]], though injectivity does not itself require monotonicity — and $a \neq b$, then $f(a) \neq f(b)$.
- **Non-injective function, not-equal premise (not guaranteed):** If $f$ is not injective — as with a [[Non-Decreasing Function|non-decreasing]] or nonincreasing function that is not strictly monotonic, or a constant function — then $a \neq b$ does not guarantee $f(a) \neq f(b)$; e.g. a constant function has $f(a) = f(b)$ even though $a \neq b$.

# Properties
- A [[Monotonic Function|monotonic function]] is either increasing or decreasing on its entire domain, so its sign-change behavior is consistent throughout that domain.
- A function that is neither nondecreasing nor nonincreasing on an interval (i.e. not monotonic there) has no fixed sign-change rule on that interval; the effect on $\diamond$ depends on the specific sub-interval containing $a, b$.
- General rule: the conclusion is only as strict as the weaker of the premise and the function's monotonicity — a strict conclusion $f(a) < f(b)$ (or $f(a) > f(b)$) requires both a strict premise ($a < b$) and strict monotonicity; if either is merely weak/non-strict, only a weak conclusion ($\leq$ or $\geq$) is guaranteed.
- The cases for premises $a > b$ and $a \geq b$ are not listed separately: they follow immediately from the $a < b$ and $a \leq b$ cases above by swapping the roles of $a$ and $b$.

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=113)
