import math
a = float(input())
b = float(input())
c = float(input())
a != 0
di = b ** 2 - 4 * a * c
if di > 0:
    x1 = (-b - math.sqrt(di)) / (2 * a)
    x2 = (-b + math.sqrt(di)) / (2 * a)
    if x1 > x2:
        if x1 == int(x1) and x2 == int(x2):
            print(int(x2), int(x1))
        else:
            print('{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
if not di:
    print(-b / (2 * a))
