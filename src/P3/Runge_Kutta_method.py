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

K = []
a, b, alpha, N = input.split()
x0 = a, y0 = alpha, h = (b - a) / N
for n in range(1, N + 1):
    K[1] = h * f(x0, y0)
    K[2] = h * f(x0 + h / 2, y0 + K[1] / 2)
    K[3] = h * f(x0 + h / 2, y0 + K[2] / 2)
    K[4] = h * f(x0 + h, y0 + K[3])
    x1 = x0 + h
    y1 = y0 + (K[1] + 2 * K[2] + 2 * K[3] + K[4]) / 6
    print(str(x1) + " " + str(y1))
    x0 = x1, y0 = y1
