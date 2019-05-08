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

import os

os.system("python gen.py")

file = open("in.txt", "r")
print(file.readline())
n = int(file.readline())
x1 = []
y1 = []
for i in range(0, n + 1):
    x1.append(0)
    y1.append(0)
    x1S, y1S = file.readline().split()
    x1[i] = float(x1S)
    y1[i] = float(y1S)

xS = file.read().split()
for tS in xS:
    x = float(tS)
    y = 0.0
    k = 0
    while k <= n:
        L = 1.0
        for j in range(0, k):
            L *= (x - x1[j]) / (x1[k] - x1[j])
        for j in range(k + 1, n + 1):
            L *= (x - x1[j]) / (x1[k] - x1[j])
        y += L * y1[k]
        k += 1
    print(str(x) + " " + str(y))

