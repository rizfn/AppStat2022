## Review of previous lectures

If you have errors on your measurements, instead of considering residuals you can look at the pull, defined by
$$\text{pull} = \frac{y_i - y_{mean}}{\sigma_y} = z $$
Take a look at that to see if your errors are underestimated or overestimated, pull should be ~1.

## Minuit Tips

Don't set limits, it causes the minimization to do a lot of extra work for some reason. Try to get it to work by just passing in a better starting value.

Minos error helps you find asymmetric errors (left and right): the minima of your function is not parabolic but very skewed.

For good convergence, you need

* **Good initial values**: The most important thing
* Minimizing correlations between fit parameters: Not easy, but in a simple case, consider that you've got the sum of two gaussian variables.
    $$N_1 G(\mu_1, \sigma_1) + N_2 G(\mu_2, \sigma_2)$$
    What we can do is look at the total number of observations $N$ and the fraction of points from one distribution $f$
    $$N \left(f\cdot G(\mu, \sigma) + (1-f)\cdot G(\mu, \sigma)\right)$$
    and $N$ and $f$ are now uncorrelated.
* Low number of fit parameters (at least initially)
* Good binning 
* Using a chi-square fit (as a start)

## Peaks on a background: 

The *local significance* of a peak can be seen by looking how far away from zero is the normalization.

When you're searching for peaks, the first thing to do is establish a good (non-peaking) background. If you have the resolution of a peak, you can use a fixed width (but you usually don't).

The second thing is evaluating if peaks are real or just fluctuations. Fitting peaks will tell you the local significance. Calculate a *global significance* by
$$p_{global} =1 - (1-p_{local})^N \approx N \cdot p_{local}$$
where $N$ is the number of places you can try to put a peak. When you try to move a peak, you shouldn't move it infinitesimally but move it in units of $\sigma$ (cause otherwise you'd get tons of peaks near the actual peak).

Test whether using multiple peaks improves your result (calibration channels). If the significance goes up, it's better.

How many fit parameters? As many as necessary, and not a single one moree. Putting in too many parameetrs "dilutes" your model strength.

## Simpson's Paradox

A classic pitfall in statistics. How to avoid?

Subdivide data, and plot the data. For example. because of ages you may get different results and so you should subdivide by them.
