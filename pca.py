import numpy as np

X = np.matrix('1 2; 3 4; 5 6')
print(X)
m = np.mean(X, axis=0)
X = X-np.mean(X, axis=0)

V = np.cov(X.T)

values, vecotrs = np.linalg.eig(V)

map = {}
for i in range(values.shape[0]):
    map[values[i]] = vecotrs[i]
values.sort()

for i in range(values.shape[0]):
    vecotrs[i] = map[values[i]]

X = vecotrs*X.T
print(X.T)
