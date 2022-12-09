## Mean and Width

$$\hat{\mu} = \frac1N \sum_i x_i = \bar{x}$$

We use a hat ($\hat{\mu}$ instead of $\mu$) in order to show thatthis is our estimate for the mean, and not the true mean

Standard deviation, width, RMSE is the same. It needs us to know the real true mean, $\mu$.

$$\sigma = \sqrt{\frac1N \sum_i (x_i - \mu)} = \bar{x}$$

We only know the approximate mean, so we subtract 1 cause it's a degree of freedom that we end up using.

$$\hat{\sigma} = \sqrt{\frac1{N-1} \sum_i (x_i - \hat{\mu})} = \bar{x}$$

This makes the width **larger**. For large $N$, it doesn't make a difference, but for small $N$ you should subtract 1.

What about the uncertainity in the mean? How does it improve with data?

$$\hat{\sigma}_\mu = \hat{\sigma}/\sqrt{N} $$

There's a difference between uncertainity in a single measurement and the uncertainity in the mean.

**Weighted mean**: 
$$ \hat{\mu} = \frac{\sum x_i/{\sigma_i}^2}{\sum1/{\sigma_i}^2} $$

There is no SD on the data, because they each have their own uncertainity. However, there is an uncertainity in the mean.

You can use a chi-square to see if the diffferent measurements are in agreement with each other.

Mean is the first moment, variance is the second. Skew is the third, and 4th is Kurtosis

## Correlations

Covariance:

$$ V_{xy} =\frac1N \sum_i^n (x_i-\mu_x)(y_i-\mu_y) $$

When both are below the mean, you get a positive term. Likewise for when both are above the mean. If one is below and the other is above, you get a negative term. The sum is the covariance.

**Pearson's corellation coeff**

$$ \rho_{xy} = \frac{V_{xy}}{\sigma_x \sigma_y} $$

Between -1 (anticorrelated) and +1 (correlated)

**Always plot your data!!!** The linear correlation coefficient being zero does not mean that there isn't any pattern in your data.

If you have multiple variables, you can store the information in a covariance matrix.

Correlations can be more than linear correlations, etc: Rank correlation. Regardless of the size, if $x_i>x$ implies $y_i>y$. This is *Spearman's Correlation Coefficient*.

You can measure non-linear corrrelations too, MIC, MI and DC. See slides for links.

**Correlation does not imply causation:** Random shit can be correlated.

### Law of Large Numbers
As you keep taking random samples, it approaches the mean.

Even with a sum of 3 uniforms, you get more or less a gaussian. Even with an exponential districution, they look close to a gaussian. 75% of times, things are gaussian, correlations are linear, etc.

$\pm1\sigma \approx 68.2\%$, $\pm2\sigma \approx 95\%$, $\pm3\sigma \approx 99.7\%$ 