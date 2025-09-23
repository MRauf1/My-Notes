---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Generalized Linear Model Assumption)
> Dependent variable $Y_i$ predicted from independent variables $X_i = [x_{i1}, \dots, x_{ip}]$ with $p$ explanatory variables. Density of $Y_i$ is from the [[Natural Exponential Family]]
> $$
> \begin{align}
> f(y_i, \theta_i) = a(\theta_i) b(y_i) exp(y_i Q(\theta_i))
> \end{align}
> $$
> where $Q(\theta_i)$ is the [[Natural Parameter]].
> Since $Y_i$ comes from the [[Natural Exponential Family]], its distribution is determined by its mean $\mu_i$.

> [!info] Definition 2 (Generalized Linear Model)
> Given a dependent variable $Y_i$ with mean $\mu_i$, the generalized linear model applies the [[Link Function]] on the mean of $Y_i$ to generate the [[Systematic Component]] $\eta_i$.
> The [[Canonical Link]] satisfies $g(\mu_i) = Q(\theta_i)$.

# Types
- If $g()$ is the identity link, then the GLM is [[Linear Regression]].
- If $g()$ is the [[Logit]] link, then the GLM is [[Logistic Regression]].
- If $g()$ is the [[Logarithm]] link, then the GLM is [[Log Linear Regression]].