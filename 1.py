import numpy as np
import matplotlib.pyplot as plt

N = 10000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

R = np.sqrt(2 / np.pi)
h = x**2 + y**2 <= R**2

print(h.mean())
print(2 / 4)

plt.figure(figsize=(5,5))
plt.scatter(x[h], y[h], s=1)
plt.scatter(x[~h], y[~h], s=1)
plt.axis("equal")
plt.show()
