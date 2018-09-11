k = 0  #общее количество
while True:  #бесконечный цикл
    n = int(input())
    k += 1
    if n == 0:  #нашли ноль
        break  #выходим из цикла
print(k - 1)
