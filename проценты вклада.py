p = float(input())  # rub
x = float(input())  # kop
y = float(input())  # %
s = (x * 100 + y) * (100 + p)
x_final = int(s * 0.0001)
y_final = int(s * 0.01 - x_final * 100)
print(x_final, y_final, sep=" ")
