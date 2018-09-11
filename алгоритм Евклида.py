a = float(input())
b = float(input())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
print(int(gcd(a, b)))
