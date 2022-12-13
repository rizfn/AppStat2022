# Hypothesis Testing

Sometimes, you can have multiple hypothesis and you can't reject any of them, you can accept multiple. The question about hypothesis testing is *deciding which hypothesis to reject*.

The null hypothesis is being compared to an alternate hypothesis. A type 1 error $\alpha$ is where you get a false positive, a type 2 error $\beta$ is a false negative.

* Null hypothesis: Noise / Background
* Alternate hypothesis: Background + Signal
* $\alpha$: False positive *rate*
* $\beta$: False negative *rate*

Where you decide to reject hypotheses depends on what you want. Minimizing the false positive rate typically increases the false negative rate. 

You want a good test statistic, which separates the null and alternate hypothesis as much as possible.

## Measuring separation

We use a ROC curve. Imagine the two distributions for each hypothesis overlap completely, then you can't tell the difference between them. In a ROC curve, you plot the false positive rate vs the true positive rate.

It always starts from (0,0) and goes to (1,1), and the curves always lie above the diagonal (45 degree line). This is the **Reciever Operating Characteristic**, hence ROC.

How do you make it? Scan over your x-axis, and at each point integrte the PDFs from $-\infty$ to the point. It'll start at (0,0), and eventually get to (1,1).

Where to select? The ROC curve doesn't tell you where to make your selection. Often, you optimize $S/\sqrt(B)$, where $S$ is signal and $B$ is background.

There are multiple metrics for hypothesis testing, see wikipedia. Weird one is $F_1$ score: You look at the rate of getting both things correct (prevents you from saying that you have a 99% accurate test if you call everything negative because you know 99% of the data is negative)

The more the hypotheses are separated by the test statistic, the further towards the corner the ROC curve will be.

You can try different test statistics, and draw the ROC curve for each. Choose the one that goes furthest to the corner.

## Testing Procedure

1. Consider a null hupothesis
2. State alt hypothesis
3. Consider assumptions
4. Create test statistic
5. Find distribution under both hypotheses for the statistic
6. Select a significance level (where you say if it's one or the other): the probability threshold below which the null hypothesis will be rejected
7. Compute from data
8. check p value
9. Accept/reject

You can never prove a hypothesis, you can only accept them. However, you can reject hypotheses on the basis that the probability of it being correct is too small.

**Neyman-Pearson Lemma:** if you have a likelihood ratio between a null and alternative model (and neither of them have any parameters), the most powerful test you can do is
$$D = -2 \ln \frac{likelihood_{null}}{likelihood_{alt}}$$

Wilk's Theorem can be seen as an extension of this for more complicated cases.

## Common Tests:

* **One sample test:** Compare a number to a constant, and see if it's consistent. eg: the $z$ test: measure the distance in units of $\sigma$.
* **Two sample test:** Compares two samples with each other
* **Paired test:** special case of two-sample test: where you compare paired member differences (in order to control imporant variables). eg: testing twins as opposed to random people
* **Chi-squared test:** Evaluates adequacy of data as compared to model
* **Kolmogorov Smirnov test:** Evaluates if two distributions are compatible.
* **Wald-Wolfowitz runs test:** Binary check for independence
* **Fisher's exact test:** Calculates p-value for contingency tables
* **F-test:** Compares 2 sample variances to see if grouping is useful
* **Andersen Darling:** test to see if something is gaussian

## Which test to use?

One metric is the *power of a test*, $(1-\beta)$. In reality you want to choose something specific to the situation.

At low statistics, you might want to consider the Student's t-distribution. It's like a gaussian with longer ails. Rule on thumb: if $N > 10-20$ or $\sigma$ is known use the $z$ test, else T-test 

One-sided vs two-sided tests: if you're testing for the difference, use two-sided tests. Otherwise, use one-sided.

The Kuiper test is anotehr test used to detect shifts in distributions. Not used often but smart(?)

Wald-Wolfowitz: you have data, and fit a line. You can then measure the number of "runs", defined as sequences of the same outcome (only two types). In the example, it's the number of points above or below the line. If the points are randomly distributed, you know the mean and variance, and can compare the number of runs to what you'd see if it was approx. Gaussian. Chi-square doesn't care on what side you are, only on what side you are, however Wald-Wolfowitz doesn't care about the distance from the points but only on what side you are.

A contingency table is a table with numbers everywhere (think 2x2). Now you can ask if there's a correlation of being in row1 or row2 with being in column1 or column2. It's like combinatorics, you can predict the chance of being in each place. See wikipedia article for an example. Things often boil down to this.

Look up f-test as well.

Andersen-Darling is for testing distributions, there's also Shapiro Wilks test.

## How many sigmas?

Really depends on the case, but in general, the wilder the claim, the stronger the evidence needed.
