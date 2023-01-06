## Atlas test beam data:

Electrons are light, and so they're very easy to make relatavistic, other particles not so.

There are 5 detectors, of which you have *3 independent detectors*.

### Detectors:

1. **Cherenkov detector:** In a medium, a particle can move faster than the speed of light (in a vacuum), which causes a 'sonicboom' of light, which is called cherenkov light.
2. **Transition radiation tracker (TRT):** charged particles moving through air ionize it. If you set up a field, you can set it so can record the passage of the particles. You do it in layers: drifting between a layer sends another light emission of a much higher size. You need to be relativistic though. Two numbers: Low threshold hits (going through one layer) and high threshold hits (going through).
3. **EM calorimeter:** The first two were built to not interact wih the particles, so as to not disturb them. The calorimeter is the opposite. Electrons shower fast, heavier particles shower slower andmore irregularly. 4 columns from this (and 3 from another calorimeter that we ignore).

### What to do:

Use the fact that we have *independent* data in order to characterize things initially. You want to group stuff so you have 1 independent variable per detector: try a lot of alternatives, and choose the one with the best ROC curve.

You can use Fisher's discriminant (or something)