a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b
d = []
i = 0

while len(c) > 0:
    d.append(min(c))
    c.pop(c.index((min(c))))

print(*d)
