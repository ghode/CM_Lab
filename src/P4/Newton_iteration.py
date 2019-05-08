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

alpha = 0x5f3759df


def f(x):
    return np.sqrt(x)


def df(x):
    return np.sqrt(x) / x / 2


def __main__():
    eps1, eps2, cnt = input().split()
    n = 1
    x0 = alpha
    while n < cnt:
        f_res = f(x0)
        df_res = df(x0)
        if np.abs(f_res) < eps1:
            return x0
        elif np.abs(df_res) < eps2:
            return -1
        x1 = x0 - f_res / df_res
        tol = np.abs(x1 - x0)
        if np.abs(tol) < eps1:
            return x1
        n += 1
        x0 = x1
    return -1
