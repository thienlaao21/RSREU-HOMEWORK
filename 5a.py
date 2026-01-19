import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 15
p = 0.7
x = np.arange(0, n+1)
pmf = binom.pmf(x, n, p)

pl.figure()
pl.plot(x, pmf, marker='o')
pl.title('Биномиальное распределение')
pl.xlabel('Количество сотрудников вовремя')
pl.ylabel('P(X=k)')
pl.show()

mean = binom.mean(n, p)
var = binom.var(n, p)
std = binom.std(n, p)
mode = np.floor((n+1)*p)

mean, var, std, mode