import os

os.system("python gen.py")

file = open("in.txt", "r")
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
