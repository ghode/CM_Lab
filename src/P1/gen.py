def fun(x1):
    return 1.0 / (1.0 + x1 * x1)


n = 20
h = 10.0 / n
xS = []
f = open("in.txt", mode='w')
f.write("when n = " + str(n) + "\n")
f.write(str(n) + "\n")

for k in range(0, n + 1):
    xS.append(-5.0 + k * h)
    f.write(str(xS[k]) + " " + str(fun(xS[k])) + "\n")

x = 0.75
f.write(str(x) + "\n")
x = 1.75
f.write(str(x) + "\n")
x = 2.75
f.write(str(x) + "\n")
x = 3.75
f.write(str(x) + "\n")
x = 4.75
f.write(str(x) + "\n")
