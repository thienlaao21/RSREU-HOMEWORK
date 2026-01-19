import numpy as np
import matplotlib.pyplot as pl
from scipy.stats import rv_continuous
from scipy.integrate import quad

class CustomDistribution(rv_continuous):
    def _pdf(self, x):
        return np.where((0 <= x) & (x <= 1), 3 * x**2, 0)

custom_dist = CustomDistribution(a=0, b=1)

norm, _ = quad(custom_dist.pdf, -np.inf, np.inf)
print(norm)

x = np.linspace(-0.2, 1.2, 500)

pdf_values = custom_dist.pdf(x)
cdf_values = custom_dist.cdf(x)

pl.figure()
pl.plot(x, pdf_values)
pl.show()

pl.figure()
pl.plot(x, cdf_values)
pl.show()

P1 = custom_dist.cdf(0.6) - custom_dist.cdf(0.2)
print(P1)

P2, _ = quad(custom_dist.pdf, 0.2, 0.6)
print(P2)

mean_theory = custom_dist.mean()
var_theory = custom_dist.var()
std_theory = custom_dist.std()

print(mean_theory)
print(var_theory)
print(std_theory)

rvs = custom_dist.rvs(size=10000)

mean_sample = np.mean(rvs)
var_sample = np.var(rvs)
std_sample = np.std(rvs)

print(mean_sample)
print(var_sample)
print(std_sample)

q1 = custom_dist.ppf(0.7)
q2 = custom_dist.ppf(0.9)

print(q1)
print(q2)

skew, kurt = custom_dist.stats(moments='sk')
print(skew)
print(kurt)

pl.figure()
pl.hist(rvs, bins=50, density=True)
pl.plot(x, pdf_values)
pl.show()