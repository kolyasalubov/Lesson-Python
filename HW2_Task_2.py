
# Перетворення в оберенне число
# number = str (input ("Введіть чотирьохзначне число: "))

# numb_list = list(number)
# numb_list.reverse()
# number1 = "".join(numb_list)
#
# print("'Оберенене' число дорівнюватиме: ", number1)

# Відсортування числа
# number = str (input ("Введіть чотирьохзначне число: "))
# numb_list = list(number)
# numb_list.sort()
#
# print("Відсортовані цифри дорівнюють: ", numb_list)

# Добуток цифр числа
number = int (input ("Введіть чотирьохзначне число: "))
d1 = number % 10
number = number // 10
d2 = number % 10
number = number // 10
d3 = number % 10
number = number // 10

print("Добуток цифр числа:", number * d1 * d2 * d3)