from scipy.stats import hypergeom

M = 20
n = 5
N = 4
x = np.arange(0, N+1)
pmf = hypergeom.pmf(x, M, n, N)

pl.figure()
pl.plot(x, pmf, marker='o')
pl.title('Гипергеометрическое распределение')
pl.xlabel('Количество бракованных ламп')
pl.ylabel('P(X=k)')
pl.show()

mean = hypergeom.mean(M, n, N)
var = hypergeom.var(M, n, N)
std = np.sqrt(var)
mode = (N+1)*(n+1)/(M+2)
mean, var, std, mode