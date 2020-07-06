#Друге завдання третьої лекції Python

number = int (input ("Введіть чотирьохзначне число: "))

d1 = number % 10
number = number // 10
d2 = number % 10
number = number // 10
d3 = number % 10
number = number // 10

print("Добуток цифр числа:", number * d1 * d2 * d3)
