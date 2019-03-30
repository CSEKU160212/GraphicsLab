#!/usr/bin/env python
import matplotlib.pylab as plt

x1, y1 = map(int, input("Enter initial point (x1,y1) with comma between them: ").split(","))

x2, y2 = map(int, input("Enter end point (x2,y2) with comma between them: ").split(","))

dx = x2 - x1
dy = y2 - y1

m = dy / dx

X = [x1]
Y = [y1]

if m <= 1:
    while x1 < x2:
        x1 += 1
        y1 = y1 + m

        X.append(x1)
        Y.append(round(y1))

else:
    while y1 < y2:
        x1 = x1 + 1 / m
        y1 += 1
        X.append(round(x1))
        Y.append(y1)


plt.figure("DDA Algorithm")
plt.plot(X, Y, '-ro')

for a, b in zip(X, Y):
    plt.text(a, b, str((a,b)))

plt.xlabel('X co-ordinate')
plt.ylabel('Y  co-ordinate')
plt.show()
