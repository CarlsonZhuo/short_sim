import numpy as np
import matplotlib.pyplot as plt
import pdb

p = 200
mean = [0] * p
cov = np.eye(p)*1

X = np.random.multivariate_normal(mean, cov, 500).T
XTX = X.T.dot(X)
diag_XTX = np.diagonal(XTX)
plt.plot(np.sort(diag_XTX))
plt.show()

off_diag_XTX = XTX - np.diag(diag_XTX)
vecXTX = off_diag_XTX.reshape((1,-1))[0]
vecXTX = np.sort(vecXTX)
plt.plot(vecXTX)
plt.show()
pdb.set_trace()
