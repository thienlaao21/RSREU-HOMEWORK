import numpy as np
import matplotlib.pyplot as pl

trials = range(100, 10001, 100)
freq = []

for n in trials:
    dice = np.random.randint(1, 7, (n, 2))
    freq.append(np.mean(dice.sum(axis=1) == 7))

pl.plot(trials, freq)
pl.axhline(1/6)
pl.show()