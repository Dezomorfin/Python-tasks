x = str(input())
y = x.find('f')
z = x.rfind('f')
if y == -1:
    print()
elif y == z:
    print(y)
else:
    print(y, z)
