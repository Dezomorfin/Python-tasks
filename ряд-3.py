n = int(input())
mn = 10 ** (n - 1)
mx = mn ** 10 - 1
for i in range(mx, mn, -2):
    print(i)
