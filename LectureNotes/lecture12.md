## Recap

Integrating from $-\infty$ to $x$ is CDF
Integrating from $x$ to $\infty$ is survival function

## Multiple P values

Use Fisher's method, assuming the p-values are independent. See formula.

You can also plot them if they're numerous (?).

If you have a large value, ~1, you've overestimated your errors or something.

You can also get a bimodal (two peaked) distribution of p-values.

Sparse, where only a few values are represented, even if you have statistics to fill ou everything. This happens when the outcomes of a test is limited.

The p-value distribution should look flat (?) for the null hypothesis case.

## Confidence intervals

They're a range of values which act as good estimates of the unknown parameter

$$P(x_- \leq x \leq x_+) = \int_{x_-}^{x_+}  P(x) dx = C$$

Typically, C=95%, so ~2$\sigma$.

There's a choice:
1. Require a symmetric interval
2. Require a shortest interval
3. (see slides)

The confidence interval does not always include the true value! Higher statistics also does not help, because it shrinks the confidence interval so we feel more 'confident'.

You also have 2d confidence intervals.

## Confidence limits

If you do an experiment and find nothing, you should report the effect with *what you would have discovered, had it been there*.

With Poisson cases: ask yourself, "how much can I increase $\lambda$ to still have a 5% chance of hitting 0" (or whatever you measure). If you observe 0 red cards on belgdamsveh, you can say with 95% confidence that there are less than 3 per day (because at $\lambda=3$, there's a 5% chance of seeing 0 red cars).

## How to test if a sequence of numbers is random?

If you plot the digit distribution, you can check for $\chi^2$

You can count the number of 'chains' of recurring numbers, where a number occurs multiple times in a row. Should look poisson.

You can also count the differences between subsequent digits. For random numbers, it should look like a triangle. You can also do a Runs test, checking the difference from the mean.

Distance between the same digit: you'd expect a geometric distribution (i.e, a discrete exponential).

In all these cases, you know what you would expect for a random sequence, which is the most important thing. Keep in mind, though, that even if you don't, just simulate it! Take some random numbers, and calculate what the null hypothesis should be.

If you do a test and it passes, does that prove they're random? No, cause you can never prove a hypothesis. If you do multiple tests, and even 1 fails, it's not random (or not random enough).

Binary rank test: you take the leftmost 31 bits of 31 random integers from the squence to for ma 31x31 binary matrix. Take the rank of matrix, and see what it is.

You can combine several independent RNGs (eg: bitwise XOR) and then you can get an RNG as good as the best one used. This is called software whitewashing.
