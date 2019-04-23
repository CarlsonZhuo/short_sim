import numpy as np
import matplotlib.pyplot as plt
import pdb

p = 100
mean1 = [-p] * p
cov1 = np.eye(p)*1

mean2 = [p] * p
cov2 = np.eye(p)*1

Y = np.random.multivariate_normal(mean2, cov2, 2000).T
X = np.random.multivariate_normal(mean1, cov1, 2000).T

def XTX(X):
    XTX = X.T.dot(X)
    diag_XTX = np.diagonal(XTX)
    # plt.hist(diag_XTX, bins=30)
    # plt.show()

    off_diag_XTX = XTX - np.diag(diag_XTX)
    vecXTX = off_diag_XTX.reshape((1,-1))[0]
    plt.hist(vecXTX, bins=100)
    plt.show()

def XTY(X, Y):
    XTY = X.T.dot(Y)
    vecXTY = XTY.reshape((1,-1))[0]
    plt.hist(vecXTY, bins=100)
    plt.show()

XTX(X)
XTY(X, Y)