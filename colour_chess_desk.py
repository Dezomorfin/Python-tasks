r1 = int(input())
c1 = int(input())
r2 = int(input())
c2 = int(input())
s1 = r1 + c1
s2 = r2 + c2
if s1 % 2 == 0:
    b = (s2 % 2 == 0)
else:
    b = (s2 % 2 != 0)
if b:
    print("YES")
else:
    print("NO")
