from scipy.stats import poisson

lambda_ = 4
x = np.arange(0, 15)
pmf = poisson.pmf(x, lambda_)

pl.figure()
pl.plot(x, pmf, marker='o')
pl.title('Распределение Пуассона')
pl.xlabel('Количество посетителей')
pl.ylabel('P(X=k)')
pl.show()

mean = poisson.mean(lambda_)
var = poisson.var(lambda_)
std = poisson.std(lambda_)
mode = int(np.floor(lambda_))

mean, var, std, mode
