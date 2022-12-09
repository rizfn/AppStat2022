## Revisions

Giving the same argument for why it's a uniform distribution (see the chi-square excercise).

Binomial, poisson, gaussian excercise: if we generate numbers from a binomial dist and fit it with other distributions, it's always good for a binomial fit, it's good for poisson is p is small and N is big, and it doesn't fit a gaussian unless N*p ~ 6.

There are parts where it can fit any combinations.

## Principle of Maximum Likelihood

In histograms, you can have problems if you have a histogram with <5 entries per bin, and you need to fit it. When in that problem, take a step back and stick to the principle of maximum likelihood.

How likely is it that we get certain samples from a particular PDF?
$$ L(\theta) = \prod_i f(x_i,\theta) \;dx_i $$
Where $f$ is the pdf.

You can compare PDFs in this way, by tweaking the parameters to create two distinct pdfs, and comparing the samples from them.

If you have a ton of values, when you multiply them together it gets too small for a computer. Thus, we use the log instead.

If stuff is gaussian

$$ \ln(L) = \sum \ln\left( ``something"  \cdot \exp(\frac{x_i - \mu}{\sigma^2}) \right) $$

$$ \ln(L) = \sum c\cdot \frac{x_i - \mu}{\sigma^2} $$

$$ \ln(L) = c\cdot \chi^2 $$

It reduces to chisquare

The likelihod is
* Consistet (converges to the right value)
* Asymptotically normal (converges for gaussian errors)
* Efficient: Reaches the minimum variance bound for large $N$

Everything from chi-square to the rest of statistics comes from this. To go back to the bad histogram problem, you want to first do a chi-square initially (cause it's robust) and then do a likelihood fit.

Normally, when you do chisquare, you do it only for bins that contain something. In a low-statistics case, that might not be ideal. How do you do a likelihood fit?

$$ L(\theta) = \prod_i^{N_{bins}} Poisson(N_i^{expected}, N_i^{observed}) $$

You can also do it without bins:

$$ L(\theta) = \prod_i^{N_{data}} PDF(x_i^{observed}) $$

Of course, there's a $-2\ln$ on both of  these.

Ideally, the unbinned version is better, but sometimes you may only have binned data, or it may take a very long time to compute if you have lots of data points (but in that case, just  chi-square).

The trump card for chi-square is that it has a goodness-of-fit measurement. Can the likelihood do that too?

You can get a p-value in the following way: take the pdf that you fit, and draw many different sample sets from it, and plot their likelihoods. You'd get a gaussian, and then you can see how likely it is that your pdf gives you the particular likelihood for the data points. It's called "Taking the asymptotics".

If you have some data and two different hypothesis (essentially, two PDFs). The ratio of likelihoods is a good test-statistic:

$$ D = -2\ln\left(\frac{\text{likelihood for null model}}{\text{likelihood for alternate model}}\right) $$

$$ D = -2\ln\left(\text{likelihood for null model}\right) + 2\ln\left({\text{likelihood for alternate model}}\right) $$

If the two models are both simple (i.e., they have no free parameers, this is the best test you can make).

Typically, you'll have a simple hypothesis and one which is a minor complication on that (i.e, it has more degrees of freedom). If you have a simple model and a complicated one which builds on it (i.e, the original is nested inside it), the $D$ value ccomes from the chi-square distribution with the difference in degrees of freedom of the two models (Wilk's Theoerm).


