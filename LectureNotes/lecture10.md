## Aud A table

If you want to be crude about data cleaning, take 4 standard deviations away. Arbitrary, like everything else in stats. Poor man's Chauvenet's  Criteria: What's the probability (considering you have $N$ measurements) that a measurement will be at least that far out?

Chauvenet's criterion isn't _the_ criterion, but at least it's a quantification.

After that rejection, you can do some more: take the pulls (what you need for a weighted average), and once again reject points (this time on the basis of their uncertainity as well, instead of just their values).

Two schools of thought: 

1. **Reject** bad datapoints and get an answer
2. **Fit** with all data, your model can't just ignore datapoints.

Earlier we went through 1, in 2 you want to make a good choice about what function to fit. If there's low statistics (few points in a couple of bins) you want to use a likelihood fit: In case every point has it's own uncertainity and the uncertainities have some sort of meaning behind them, you can try an *unbinned likelihood fit*.
