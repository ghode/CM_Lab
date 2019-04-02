def fun(x1):
    return 1.0 / (1.0 + x1 * x1)


n = 80
h = 10.0 / n
x = []
f = open("in.txt", mode='w')
f.write(str(n) + " 4.75\n")
for k in range(0, n + 1):
    x.append(-5.0 + k * h)
    f.write(str(x[k]) + " " + str(fun(x[k])) + "\n")
