---
tags: [statistics, time_series_analysis]
---

# Definition

[[Discrete]] or [[Continuous]] [[Stochastic Process]] where the index is [[Time]].

# Properties
- Data collected over time
- Data cannot be assumed [[Independent Random Variable]]
	- Time series models incorporate time dependence

# Acronyms
Auto means comparing a time series with its lagged version.
Cross means comparing 2 different time series.

- ACVF is [[Auto Covariance]] [[Function]]
- ACF is [[Auto Correlation]] [[Function]]
- CVF is [[Cross-Covariance]] [[Function]]
- CCF is [[Cross-Correlation]] [[Function]]

# Approaches
- [[Time]] domain:
	- Modeling future value as a [[Parametric Function]] of current and past (in time) values
- [[Frequency]] domain:
	- Assumes primary feature of time series is its periodical/systematic [[Sinusoidal Function]] variations

# Patterns
- Trend:
	- Pattern exists when there is a long-term increase/decrease in the data
- Seasonal:
	- Pattern exists when a series is influenced by seasonal factors
- Cyclic:
	- Pattern exists when data exhibits rises and falls that are not of fixed period

# Types
- [[Stationary Stochastic Process]]
- [[Joint Stationary Stochastic Process]]

# Models
- [[White Noise Process]]
- [[Moving Average Process]]
- [[Autoregressive Process]]
- [[Random Walk with Drift Model]]
- [[Signal Plus Noise Model]]