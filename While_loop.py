x = 5
while x >= 1:
    print(x)
    x = x - 1

while x < 10:
    print(x)
    x += 1
while x < 10:
    print(x)
    x += 2
print("next code")

z = 0
while z < 10:
    print(str(z) + " z Is less than ten")  # Однократное выполнение блока инструкций цикла называется итерацией.
    z += 1
else:
    print(str(z) + " z now is not less than ten")

for x in range(10):
    print(str(x) + ' x is less than ten')
else:
    x += 1
    print(str(x) + " x now is not less than ten" + str(x))

# break, continue, pass
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    pass
print('Another code')

for item in my_list:
    if item == 2:
        break  # выход из цикла
    print(item)
print("Some text")
# Continue
for item in my_list:
    if item == 2:
        continue
    print(item)
print("Some text")
