import numpy as np
from pdb import set_trace


def get_random_L(n, r, low=-10, high=10):
    # n is the dim of the data
    # r is the rank of the low rank matrix
    L1 = np.random.randint(low=low, high=high, size=(n,r))
    L2 = np.random.randint(low=low, high=high, size=(n,r))
    return L1.dot(L2.T), L1, L2


def get_random_S(n, s, low=-10, high=10):
    # n is the dim of the data
    # s is the sparsity of the sparse matrix
    S = np.random.randint(low=low, high=high, size=(n,n))
    for i in range(n):
        for j in range(n):
            if np.random.rand() < s: S[i,j] = 0
    return S

def trunc(x, k):
    n = x.size
    top_k = np.sort(x)[n-k]  # the k-th largest value
    result = np.zeros(n)
    for i in range(n):
        if x[i] >= top_k: result[i] = x[i]
        else: result[i] = 0
    return result

def trunc_power_method(A,k=3):
    (n,m) = A.shape
    assert(n==m)
    x = np.zeros(n)
    x[0] = 1
    for i in range(100):
        x = trunc(x, k)
        x = A.dot(x)
        x = x / np.linalg.norm(x)
    return x

L, L1, L2 = get_random_L(10, 3)
S = get_random_S(10, 0.9)
A = L + S
L_hat = trunc_power_method(A)
set_trace()
