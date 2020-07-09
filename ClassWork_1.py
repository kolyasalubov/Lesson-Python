#Задача 1

# numb1 = int(input('Введітьперше число: '))
# numb2 = int(input('Введіть друге число: '))
# if numb1 > numb2:
#     print(f'Число {numb1} більше від числа {numb2}')
# else:
#     print(f'Число {numb2} більше від числа {numb1}')


#Задача 2

# numb = int(input('Введіть ціле число: '))
# if numb % 2 == 0:
#     print(f'Введене Вами число {numb} є парним')
# else:
#     print(f'Введене Вами число {numb} є не парним')

#Задача 3

numb = int(input('Введіть число: '))
fact = 1
for i in range(1,numb+1):
    fact*=i
print(f'Факторіал числа {numb}:', fact)

