---
tags: mathematics, pre_calculus
---

# Definition

> [!info] Definition 1 (Polynomial Function)[^1]
>  Function of form
> $$
> \begin{align}
> f(x) = a_n x^n + a_{n - 1} x^{n - 1} + \dots + a_1 x + a_0
> \end{align}
> $$
> where $a^n, a^{n - 1}, \dots, a_1, a_0 \in \mathbb{R}$ and $n \in \mathbb{N} \cup \{0\}$. The [[Domain|domain]] is $(- \infty, \infty)$.

[[Function|Function]] of a [[Polynomial|polynomial]].

# Properties

- [[Degree of Polynomial|Degree of Polynomial]]
- [[Multiplicity|Multiplicity]]

## Terms of the Function

- $a_n x^n$ is the leading [[Term|term]] of the function
- $a_n$ is the leading [[Coefficient|coefficient]] of the function
- $a_0$ is the [[Constant|constant]] term of the function

## Degree of the Function

- $n$ is the degree of the function
- $f(x) = 0$ has no degree (undefined), although can sometimes be defined to be $0$ or $-\infty$

## Multiplicity of the Function

- For a polynomial function $f$ and $x = c$ being a zero with multiplicity $m$
	- $m$ is [[Even Number|even]] $\implies$ the [[Graph|graph]] of $f(x)$ touches and rebounds from the $x$-[[Axis|axis]] at $(c, 0)$
	- $m$ is [[Odd Number|odd]] $\implies$ the [[Graph|graph]] of $f(x)$ passes through the $x$-[[Axis|axis]] at $(c, 0)$

## End Behavior

- End behavior of a polynomial function $f(x) = a_n x^n \dots + a_0$ with $a_n \neq 0$ matches the end behavior of the polynomial function $g(x) = a_n x^n$

### Function with an [[Even Number|Even]] Degree

- $a_n > 0 \implies \lim_{x \to -\infty} = \infty \land \lim_{x \to \infty} = \infty$
- $a_n < 0 \implies \lim_{x \to -\infty} = -\infty \land \lim_{x \to \infty} = -\infty$

### Function with an [[Odd Number|Odd]] Degree

- $a_n > 0 \implies \lim_{x \to -\infty} = -\infty \land \lim_{x \to \infty} = \infty$
- $a_n < 0 \implies \lim_{x \to -\infty} = \infty \land \lim_{x \to \infty} = -\infty$

## Solutions (Zeros) of the Function

### Number of Solutions
- A polynomial function of degree $n \geq 1$ has at most $n$ [[Real Number|real]] zeros (including multiplicities)
- [[Descartes' Rule of Signs|Descartes' Rule of Signs]]
- [[Fundamental Theorem of Algebra|Fundamental Theorem of Algebra]]
- [[Complex Factorization Theorem|Complex Factorization Theorem]]
- [[Real Factorization Theorem|Real Factorization Theorem]]

### Interval of Solutions

- [[Cauchy's Bound|Cauchy's Bound]]
- [[Polynomial Upper and Lower Bounds|Polynomial Upper and Lower Bounds]]

### Finding the Solutions

- [[Rational Zeros Theorem|Rational Zeros Theorem]]
- [[Conjugate Pairs Theorem|Conjugate Pairs Theorem]]

## Other

- [[Intermediate Value Theorem|Intermediate Value Theorem]]
- For a polynomial function of degree $n \geq 1$, the following statements are equivalent:
	- $c \in \mathbb{R}$ is a zero of $p$
	- $p(c) = 0$
	- $x = c$ is a solution to the polynomial equation $p(x) = 0$
	- $(x - c)$ is a factor of $p(x)$
	- [[Point|Point]] $(c, 0)$ is an $x$-[[Intercept|intercept]] of the graph of $p(x)$

# Operations

## [[Addition]]/[[Subtraction]]/[[Multiplication]]
The result is another polynomial function

## [[Polynomial Division|Polynomial Division]]
The result is a [[Rational Function]]

[^1]: [szprecalculus07042013.pdf](zotero://open-pdf/library/items/J3667KH4?page=247)