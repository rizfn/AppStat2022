## Recap

Why can't you get a gaussian through CLT from Cauchy? That's because a Cauchy distribution has an undefined mean and variance, and the CLT assumes the dists you add have a defined variance and mean.

## Error Propagation

We know the uncertainity on $x$, $\sigma(x_i)$. We want theh uncertainity on $y(x)$. In the simplest way, you take a gaussian and multiply by the slope of $y(x)$. In terms of simulation, you pick values of x randomly from your $\sigma(x)$, and calculate the $y$s accordingly, and find their spread.

Note that this assumes that $y(x)$ is a smooth function. It also assumes that the derivative is relatively constant across a length scale $\approx \sigma_x$.

Math, done in lecture slides. Check.

If we have an independent error in x, $x_1$, and one in $y$, $x_2$, then one jitters horizontally and one vertically. We add the derivatives and errors in quadrature, because it's like pythagoras.

If we add two things, we add the error in quadrature

In multiplication, the relative errors add in quadrature:

$$ \frac{{\sigma_y}^2}{y^2} = \frac{{\sigma_{x_1}}^2}{{x_1}^2} + \frac{{\sigma_{x_2}}^2}{{x_2}^2} + V_{xy} terms $$

The thing that increases bt $1/\sqrt{N}$ when you take more measurements is the _statistical error_. However, the other errors that don't contribute are the _systematic error_. In the table example, systematic error would be something like the table shrinking due to temperature that we haven't accounted for.

If you're writing a paper and the errors are not gaussian, make sure to tell the reader. Maybe even show the distribution in the appendix.
