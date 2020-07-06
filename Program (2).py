#Третє завдання третьої лекції Python

number = str (input ("Введіть чотирьохзначне число: "))

numb_list = list(number)
numb_list.reverse()
number1 = "".join(numb_list)

print("'Оберенене' число дорівнюватиме: ", number1)