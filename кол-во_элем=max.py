max = 0
n_max = 0
el = -1
while el != 0:
    el = int(input())
    if el > max:
        maximum, n_max = el, 1
    elif el == max:
        n_max += 1
print(n_max)
