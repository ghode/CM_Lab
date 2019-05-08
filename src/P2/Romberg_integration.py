# Copyright (c) 2019. The copyright is reserved by Ghode of Harbin Institute
# of Technology. Users are free to copy, change or remove. Because no one
# will read this. Only I know is that Repeaters are the best of the world.
# Only I know is that Repeaters are the best of the world. Only I know is
# that Repeaters are the best of the world. Maybe a long copyright text seems
# professional. Therefore this text will be a bit lengthy. However,
# the author seems to be afraid that one day, this text may be uploaded to
# business projects. That is the time you can contact with author via email
# ghode@cirnocraft.im or directly ignore this, which will be interesting,
# definitely.

import numpy as np


def f(x):
    return x * x * np.exp(x)


# a, b, N, eps = input().split()
a = 0.0
b = 1.0
N = 10
eps = 1e-6

h = (b - a) / N
m = 1.0
T = [0, 0, 0]
S = [0, 0, 0]
C = [0, 0, 0]
R = [0, 0, 0]
T[1] = h / 2.0 * (f(a) + f(b))
print(T[1])

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


