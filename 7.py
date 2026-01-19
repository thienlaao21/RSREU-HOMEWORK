import numpy as np
import matplotlib.pyplot as pl
from scipy.stats import uniform, expon, norm, lognorm

x = np.linspace(-1, 6, 500)
for a, b in [(0, 1), (0, 3), (1, 5)]:
    pl.plot(x, uniform.pdf(x, loc=a, scale=b - a))
pl.show()

rvs_uniform = uniform.rvs(loc=0, scale=3, size=10000)
print(np.mean(rvs_uniform))
print(np.var(rvs_uniform))
print((0 + 3) / 2)
print((3 - 0) ** 2 / 12)

x = np.linspace(0, 6, 500)
for l in [0.5, 1, 2]:
    pl.plot(x, expon.pdf(x, scale=1 / l))
pl.show()

rvs_expon = expon.rvs(scale=1, size=10000)
print(np.mean(rvs_expon))
print(np.var(rvs_expon))
print(1)
print(1)

x = np.linspace(-6, 6, 500)
for mu, sigma in [(0, 1), (0, 2), (1, 1)]:
    pl.plot(x, norm.pdf(x, mu, sigma))
pl.show()

rvs_norm = norm.rvs(loc=0, scale=1, size=10000)
print(np.mean(rvs_norm))
print(np.var(rvs_norm))
print(0)
print(1)

x = np.linspace(0.01, 6, 500)
for s in [0.5, 1, 1.5]:
    pl.plot(x, lognorm.pdf(x, s))
pl.show()

s = 0.8
mu = 0
rvs_lognorm = lognorm.rvs(s=s, scale=np.exp(mu), size=10000)

mean_sample = np.mean(rvs_lognorm)
var_sample = np.var(rvs_lognorm)

mean_theory = np.exp(mu + s ** 2 / 2)
var_theory = (np.exp(s ** 2) - 1) * np.exp(2 * mu + s ** 2)

print(mean_sample)
print(var_sample)
print(mean_theory)
print(var_theory)

pl.hist(rvs_lognorm, bins=50, density=True)
pl.plot(x, lognorm.pdf(x, s, scale=np.exp(mu)))
pl.show()