---
tags: mathematics, abstract_algebra
---

# Definition

> [!info] Definition 1 (2D [[Rotation|Rotation]] [[Matrix|Matrix]])
> $$
> \begin{align}
> R_{\theta} = \begin{bmatrix}
> cos(\theta) & -sin(\theta) \\
> sin(\theta) & cos(\theta)
> \end{bmatrix} \in M_2(\mathbb{R})
> \end{align}
> $$

Matrix rotating a [[Plane|plane]] by $\theta$ [[Degree|degrees]] counterclockwise.

$R_{\theta, u}$, where $u$ is a unit vector = matrix of [[Rotation|rotation]] around [[Axis|axis]] through $u$ by $\theta$ angle, counterclockwise viewed from the head/tip of $u$ 

# Properties

Let $u$ be a unit vector

- $R_0 = I$
- $R_{\theta_1} + R_{\theta_2} = R_{\theta_1 + \theta_2}$
- $R^{-1}_{\theta} = R_{- \theta}$
- $R_{\theta + 2\pi n} = R_{\theta}, \forall n \in \mathbb{Z}$
- $(\{R_{\theta} | \theta \in \mathbb{R}\}, \cdot)$ is a [[Group|group]]
- $R_{0, u} = I$
- $R_{\theta + 2\pi, u} = R_{\theta, u}$
- $R_{\theta, u} = R_{-\theta, -u}$
- $R_{\theta, u}^{-1} = R_{-\theta, u} = R_{\theta, -u}$
- $R_{\alpha, u} R_{\beta, v} = $ a rotation matrix
- $R_{\alpha, u} R_{\beta, u} = R_{\alpha + \beta, u}$
- For a [[Unit Vector|unit vector]] $u$, [[Orthogonal Matrix|orthogonal matrix]] $P$, $\theta \in \mathbb{R}$, $R_{\theta} P u = P R_{\theta} u P^{-1}$ ([[Change of Basis|Change of Basis]])