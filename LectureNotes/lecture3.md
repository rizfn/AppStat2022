## Errors and uncertainities:

Either:
1. Theory is not deterministic: QM
2. Random measurement errors
3. Things we can't evaluate enough to know cause of limitations in cost, time, etc

**Numbers without stated uncertainities are meaningless!**

## Why Statistics?

Experimental measurements are only samples of reality, and they can't represent the entire set of people. Statistics is about *hypothesis testing*, wich is quantifying the answer to "Which theory matches the data best?"

To do hypothesis testing, you find a test statistic (quantity) which is *different* between the two hypotheses. Then see what data matches it.

You also have to consider **biases**. Slides have two example of leading questions.

Sometimes, try something new, step outside your comfort zone. If it doesn't work, it doesn't work. Perfect time to hone coding skills.

## Chi Square fitting

If you have data, how do you fit stuff? If you have a straight line and you have data with uncertainity in $y$, you can do it aanlytically.

Least squares is the standard approach to approximate an *overdetermined system*: more equations than unknowns. The least squares minimizes the sum of squared residuals, where the residuals are the difference between the actual and fitten values.

In the chi-squared test, it's pretty much the same but we include the uncertainities.

$$ \chi^2(\theta) = \sum_i^N \frac{(y_i-f(x_i,\theta))^2}{{\sigma_i}^2} $$

$\theta$ represents the fit parameters, we tweak them to minimize $\chi^2$. How far away, in units of the uncertainity, are we? We don't care about whether it's positive or negative, just how far away you are. You're also punished very heavily for being far away.

The best thing is it provides a measure for goodness of fit.

How many degrees of freedom do you have in a fit? It's the number of datapoints minus the number of fit parameters (since you have an overdetermined system, it'll be $>1$). If you want to test a particular curve (with fixed parameters, say you get them from theory) you have no fit parameters and so DOF = number of datapoints.

The smaller your errors, the better chi square is at telling you which model (or fit) is correct.

When you're sitting without a computer, a good rule of thumb is that your chi-square should be similar to the number of degrees of freedom.


### Weighted mean and chi-square
The weighted mean is actually a chi-square minimization on a constant function

### Chi square distribution

If you take the difference from the points to the fit line in units of the standard deviation, you would typically get 1. Furthermore, the distribution of all of them will be gaussian. 38% of your points should be outside 1$\sigma$, 5% outside $2\sigma$, etc. This is true only *if* your fit function is correct.

There is a chi-square distribution, read more about it cause idk what it means. It shows the probabiliy of getting a certain $\chi^2$ value if you have a certain number of degrees of freedom (again, assuming you're fitting with the right function).

Using the chi-square distribution, you can answer "what is the probability of getting this ch-square value or worse, assuming this is the correct fit function?"

If the probability is too small, maybe you're using the wrong fitting function. Thus, we can obtain a "goodness of fit". It's basically $1 - \mathcal{P}_{\chi^2}$, where $\mathcal{P}_{\chi^2}$ is the CDF of the chi-square distribution. It's called the *survival function*.

Compare $\chi^2$ and $N_{DOF}$:
* $=1$, you're good
* $<<1$, fit is bad, and hypothesis is incorrect
* $<<1$, fit is toogood, and you've overestimated the errors

If you have a lot of data, it's hard to find a model with a good chi-square probability because it's hard to find an accurate description as accurate as the data.

### Chi square for binned data

Using Poisson statistics,
$$\chi^2 = \sum_{i\in\text{bin}} \frac{O_i-E_i}{E_i}$$

You can use observed somewhere else (I think the denominator?) but something about empty bins.

If you plot chi-square vs parameters, if everything is nice and gaussian, you get a parabola (why? who knows)

### Why Chi-square is near magic

How do you get the uncertainities out from chi-square

The minimum is reported as best chi-square, and the values are central. Now, it wanders about and looks for when the chisquare value is 1 above the minima (There's a math proof). Since it's a parabola, it'll be symmetric, and that is the error (standard deviation). Uncertainities can be assymmetric, in which case you'd like to report two errors.

The chi-square assumes gaussian errors.

What if you have uncertainities on $x$? First, do a normal fit, with the mean x-values. Now, you say 
$$ \sigma_{y_i}^{new} =\sqrt{\left( \sigma_{y_i}^{old}\right)^2 \cdot\left(\frac{\partial y}{\partial x}\vert_{x_i}\sigma_{x_i} \right)^2}$$
And keep doing this iteratively. It converges very fast though.