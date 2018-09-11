a = list(input().split())
min = 1000
for i in range(len(a)):
    s = int(a[i])
    if s < min and s > 0:
        min = s
print(min)
