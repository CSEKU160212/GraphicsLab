#!/usr/bin/env python
import matplotlib.pylab as plt

x1, y1 = map(int, input("Enter initial point (x1,y1) with comma between them: ").split(","))
x2, y2 = map(int, input("Enter end point (x2,y2) with comma between them: ").split(","))

x = x1
y = y1

dx = x2 - x1
dy = y2 - y1
dT = 2 * (dy - dx)
dS = 2 * dy
d = dS - dx

m = dy / dx

X = [x]
Y = [y]

if m < 1:
    while x < x2:
        x += 1
        if d < 0:
            d += dS
        else:
            y += 1
            d += dT
        X.append(x)
        Y.append(y)
else:
    while y < y2:
        y += 1
        if d < 0:
            d = d + 2 * dx
        else:
            x += 1
            d = d + (2 * (dx - dy))
        X.append(x)
        Y.append(y)

plt.figure("Bresenham Line Drawing Algorithm")
plt.plot(X, Y, '-ro')

for a, b in zip(X, Y):
    plt.text(a, b, str((a,b)))

plt.xlabel('X co-ordinate')
plt.ylabel('Y  co-ordinate')
plt.show()
