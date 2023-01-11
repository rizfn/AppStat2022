## Advanced Fitting

### Chi-square good

Under the assumption that the errors are gaussianly distributed, you have a best fit *and* a goodness of fit measure.

Based on the $\chi^2$ and the degrees of freedom, you have a probability. If it's between 0.01 and 0.99, it's good.

If you have very high statistics (>$10^6$) it might be hard to find a model because there are a ton of small effects, and so you won't get a good $\chi^2$ probability. You should not worry too much, unless a very high precision is wanted.

It also allows you to try different models and compare which one is better.

Remember the minimizer (basically scicomp): a good starting value is pretty important.

Also remember that the error from chi-square is basically calculated from the curvature of the function.

### Fitting complex stuff

You can try to fit the background, and then subtract that. You can then fit the interior effects on the residuals, and you can put those straight back into your main fit as initial guesses.

You can also try to do it analytically, by using an analytical fourier series, but subtracting the background is better.

### When to use what fit?

* Fitting a set of points: chi-square
* Fitting a histogram: if high statistics, chi-square but bin smartly
* If statistics is small, likelihood fit, Prefer the unbinned likelihood fit, only use the unbinned if
  * no unbinned data available
  * data is not continuous or categorical

### Tricks in fitting

Typically you might have a combination of multiple functions, and you can limit the degrees of freedom by thinking a little.

A simple example is a linear combination: instead of doing 
$$N_1 f_1(x) + N_2 f_2(x)$$
you can do a 
$$ N \left(F f_1(x) + (1-F)f_2(x)\right)$$
now $N$ is the total number of data points, which is known: thus, we reduce the DOF by 1, since we only nede to find the fraction $F$.

At times, you may have to do a global fit of all your data: in that case, you need to take care to account for the background and other effects. However, it's a more robust result than only fitting in the domain of interest. What you can do is first fit in a local fit, and use that to get initial values for the global fit, and it converges efficiently.

### Chi-square penalty terms

What if you know that the parameter $\theta_N = X$ very well, how can you include that in a chi-square?

You just penalize it by trying to not let it get further away

$$\chi^2(\theta) = \sum_i^N \left( \text{usual chi-square stuff} \right) + \frac{(\theta_n-X)^2}{\sigma_X^2}$$

This comes from Bayersian analysis, in particular the Maximum a Posteriori estimation.

### Very advanced fitting

You typically have complicated fits with many parameters (high dimensional fits).

* Start with simple function and expand from there
* Start with chi-square or likelihood
* Reduce correlations on parameters
* Draw it on your data to see if it makes sense
* Chwck the correlations between the parameters
* Try to fix one or more parameters to a value you find reasonable

### Why curvature predicts uncertainity?

See slides.
