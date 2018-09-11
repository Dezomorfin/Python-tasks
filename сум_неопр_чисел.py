print("Введите STOP для получения результата")
summa = 0
while True:
	x = input("Введите число: ")
	if x == "STOP":
            break
	try:
            x = int(x)
	except ValueError:
	    print("Необходимо ввести целое число.")
	else:
	     summa += x
print("Сумма чисел равна:", summa)
