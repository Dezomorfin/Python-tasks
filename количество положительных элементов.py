a = input().split()  # список
b = 0 # количество
for i in a:
    if int(i) > 0:
        b += 1
print(b)
