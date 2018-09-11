#неведомая ебаная хуйня
p = int(input())
c = 1
b = 0
while p != 0:
    v = int(input())
    p, v = v, p
    if v == p:
        c += 1
    if c > b:
        b = c
    if p != v:
        c = 1
print(b)

#более понятное решение

prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len) #сравнивает два числа =>
        # В результате она возвращает список, в котором попался бОльший элемент при сравнении
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)
