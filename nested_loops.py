for i in range(3):
    for f in range(5):
        print(i, end='')
    print()
# 'end=" - необязательный параметр "print()"
# используется если не нужно делать перевод строки или нужно указать специальноe окончание
# examples
# print('a', 'b', 'c', end='')
# print()
# print('a', 'b', 'c', end='*')
#
for a in range(1, 6):
    for b in range(1, 3):
        print(a, b)

from string import printable

print(printable)
#  содержит цифры, буквы в нижнем и верхнем регистре, все знаки пунктуации
for a_1 in printable:
    for a_2 in printable:
        for a_3 in printable:
            pass
            # print(a_1, a_2, a_3)
        # выводит всевозможные сочетания символов

# Таблица умножения
for h in range(1, 10):
    for i in range(1, 11):
        print(i, ' * ', h, ' = ', i * h, end='   ')
    print()
for d_1 in range(1, 7):
    for d in range(d_1):
        print("*", end='')
    print()  # перенос на новую строку

x = 5

while x < 10:
    print(f"{x} less than ten")
    x += 1
    while x > 2:
        print(f"{x} is not less than two")
        x += 1
        break

