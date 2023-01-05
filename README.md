Logarithm Calculator
====================

## Overview
This is a small set of files which implements a method I accidentally stumbled upon that calculates the logarithms of real numbers via a continued fractions method.

## The Method
Whilst I derived the method myself, I am by no means the first person to do so. After finding it, I discovered that it was first published by Daniel Shanks in 1954[^1].

Suppose we wish to find $log_a(b)$ and that $a < b$. Let $n_0$ be the largest integer s.t $a^{n_0} \leq b$. The we can write that $$b = a^{n_0}a_1,$$ or alternatively $$log_a(b) = n_0 + log_a(a_1).$$ Now, by construction $a_1 < a$, as otherwise we would divide by $a$ again to increase $n_0$ by 1. But if we note the identity $log_a(b) = \frac{1}{log_b(a)}$ we find that $$log_a(b) = n_0 + \frac{1}{log_{a_1}(a)}$$ and importantly $a_1 < a$ i.e. the new base for division is smaller than the number being divided. Consequently we can define $n_1$ similarly to $n_0$ replacing $b$ with $a$ and $a$ with $a_1$. If we recursively do this process, in the limit we find the (unique) sequence $(n)_{i=0}^{\infty}$ such that:$$log_a(b) = n_0 + \frac{1}{n_1 + \frac{1}{n_2 + \frac{1}{n_3 + \cdot}}}.$$This is the _continued fraction_ representation of $log_a(b)$.

## The Implementation
There are 3 files in this project used to implement the above method:
### count_divisions.py

This file defines the function `nearest_power`. This computes $n_0$ for a given $a$ and $b$ as defined in the overview i.e the largest integer s.t $a^{n_0} \leq b$. The implementation uses recursion

### continued_fractions_calculator.py
This file defines the function `cont_frac_calculator` which takes in a sequence and recursively computes the continued fraction from the bottom up. For instance: $$\mathrm{cont\_frac\_calculator}((n_0, n_1, n_2)) = n_0 + \frac{1}{n_1 + \frac{1}{n_2}}$$

### log_calculator.py
This file uses the above two equations to implement the logarithm calculator. `calculate_sequence` calculates the sequence used to estimate the continued fraction, and `calculate_logarithm` takes in that sequence and estimates the log. `tolerance` refers to the number of terms one wishes to use in the sequence for the estimate. See the file for extra logic that takes care of special cases (such as if the input is negative)

## How To Use
To use the function, simply run `log_calculator.py` in your terminal and follow the prompts when they appear. You should be asked for a base $a$, number $b$ and sequence tolerance. An example of what to write in Git Bash:
```
winpty py -3.9 log_calculator.py
```
## Final note
It may be interesting to try and implement a method which can solve logarithms for complex numbers as well.

[^1]: Shanks, D. (1954), ‘A logarithm algorithm’, Mathematical Tables and Other Aids to Computation 8(46), 60–64. https://www.jstor.org/stable/2001992