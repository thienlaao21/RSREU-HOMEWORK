from scipy.stats import geom

p = 0.5
x = np.arange(1, 11)
pmf = geom.pmf(x, p)

pl.figure()
pl.plot(x, pmf, marker='o')
pl.title('Геометрическое распределение')
pl.xlabel('Подбрасывания до первого орла')
pl.ylabel('P(X=k)')
pl.show()

mean = geom.mean(p)
var = geom.var(p)
std = geom.std(p)
mode = 1

mean, var, std, mode
