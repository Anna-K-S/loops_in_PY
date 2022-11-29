# For
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print(number)

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print(str(number) + "HI!")

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(num)
    else:
        print(" ")

list_number_sum = 0
for number in number_list:
    list_number_sum = list_number_sum + number
print(list_number_sum)

greeting = 'Hello Python'
for letter in greeting:
    print(letter)

greeting = 'Hello Python'
for letter in greeting:
    if letter != "o":
        print(letter)

for letter in "Hello python":
    if letter != "l":
        print(letter)

for letter in "Some text":
    print("One more text") # 9 раз

tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for item in tuple_list:
    print(item)
for letter_one, letter_two in tuple_list:
    print(letter_one, letter_two)

tuple_list_1 = [('a', 'b', 1), ('c', 'd', 5), ('e', 'f', 77)]
for letter_one, letter_two, numbers in tuple_list_1:
    print(letter_one, letter_two, numbers)
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary:
    print(item) # Только ключи
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary.items(): # Ключ:значение (объекты tuples)
    print(item)

dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary.keys(): # Только ключи
    print(item)
dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary.values(): # Только значения
    print(item)


for x in range(5):  # Возвращает последовательность чисел от 0 до 4
    print(x)
    print("Hi")

for _ in range(3): # Если переменная не будет использована в дальнейшем => "_
    print("Loop")
# Используя цикл dor для вычисления суммы всех четных чисел в диапазоне от 10 до 30
# (включая крайние значения). Вывести результат
sum_numbers = 0
for even_numbers in range(10, 31):
    if even_numbers % 2 == 0:
        sum_numbers += even_numbers
print(sum_numbers)
# Получите от пользователя число на вводе и используйте цикл for
# для вывода на экран текста "Hello!" столько же раз
user_number = int(input("Enter any number"))
for _ in range(user_number):  # "range" - диапазон
    print("Hello!")

# The break Statement

tuples = ('a', 'b', 'd', 34, 22, 45.6, 'k', 'j')
for item in tuples:
    print(item)
    if item == 22:
        break

user_color: str = str(input("Enter any  color"))
for color in str(user_color):
    if user_color == int:
        break
    else:
        print("your color is" + " " + user_color)

# The continue Statement

a = [1, 2, 3, 4, 6]
for item in a:
    if item == 3:
        continue
    print(item)

some_words = ['apple', 'sky', 'computer', 'dog']
for c in some_words:
    if c == 'sky':
        continue
    print(c)

# The pass Statement
# pass позволяет обрабатывать условия без влияния на цикл; чтение кода будет продолжаться
# до появления выражения break или другого выражения. "Заглушка"


number_a = 2
for number_a in range(6):
    if number_a == 4:
        pass
    print('number is' + " " + str(number_a))
