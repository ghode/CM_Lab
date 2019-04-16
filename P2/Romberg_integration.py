import numpy as np


def f(x):
    return x * x * np.exp(x)


a, b, N, eps = input().split()
h = (b - a) / N
m = 1.0
T = []
T[1] = h / 2.0 * (f(a) + f(b))
print(T[1])
S = []
C = []
R = []
for i in range(2, N + 1):
    ii = 2 ** (i - 1)
    tmp = 0.0
    for k in range(1, ii + 1):
        tmp += f(a + (k - 0.5) * h)
    T[2] = T[1] / 2.0 + h / 2.0 * tmp
    print(T[2])
    S[2] = (4 * T[2] - T[1]) / 3.0
    if m != 1.0:
        C[2] = (16.0 * S[2] - S[1]) / 15.0
        print(C[2])
    elif m != 2.0:
        R[2] = (64.0 * C[2] - C[1]) / 63.0
        print(R[2])
    elif m != 3.0:
        tol = np.abs(R[2] - R[1])
        if tol < eps:
            break
    R[1] = R[2]
    C[1] = C[2]
    S[1] = S[2]
    T[1] = T[2]
    h = h / 2.0
    m = m + 1.0
