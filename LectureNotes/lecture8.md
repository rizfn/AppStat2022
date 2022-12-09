# Random number generation

## Monte Carlo Simulations

Monte-Carlo is solving a problem with random numbers, typically a problem with an unknown analytic solution and/or high dimensionality.

How to produce random numbers from a given PDF? There are two methods.

1. **Transformation method**: *Inverse Transform Sampling*. It requires that we can find the CDF (i.e, we can integrate the PDF
    $$F(x) = \int_{-\infty}^x f(x')dx'$$
    and that the CDF is invertible. Even if you can't do it analytically, you can always do it numerically.
2. **Accept-reject method**: *Rejection sampling*: You need a PDF that's bounded in $x$. We generate random $x$ and $y$ values from a uniform distribution. If $y<f(x)$, accept the random number, else reject.

You can combine the two methods to solve pretty much everything. Let's say you have

$$f(x) = e^x \cdot \cos^2(x)$$

You can generate exponential numbers with the transformation method, and afterwards throw them into the accept/reject sampling.

Why do we use Monte-Carlo? It's because of the complexity. For integration,
$$\text{Monte-carlo:  }  \frac{1}{\sqrt{N}}$$
$$\text{Trapezoidal:  } \frac{1}{N^{2/d}}$$

In dimensions >4, monte-carlo is a better choice.

### Binning:

See slide, it's gto a lot of points about binning
