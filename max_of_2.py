a = int(input())
b = int(input())
w = (abs(a - b) + (a + b)) // 2
if a > b:
    print(a)
if b > a:
    print(b)
if a == b:
    print(a)
