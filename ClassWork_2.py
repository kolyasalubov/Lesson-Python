#Перша задача рішення 1
# list_1 = [input ("Ведіть елементи списку: ") for i in range(int(input('Скільки елементів списку ви хочете?: ')))]
# print(f"Найменше число,{min(list_1)}", '\n' f"Найбільше число,{max(list_1)}")

#Перша задачі рішення 2
# num = int(input('Скільки елементів списку ви хочете?: '))
# list_1 = [input ("Ведіть елементи списку: ") for i in range(num)]
# myMax = list_1[0]
# myMin = list_1[0]
# for i in range(num):
#     if list_1[i] > myMax : myMax=list_1[i]
#     if list_1[i] < myMin : myMin=list_1[i]
# print(f"Найменше число,{myMin}", '\n' f"Найбільше число,{myMax}")


#Друга задача
# evens = []
# dividable_on_3 = []
# other = []
#
# for i in range(1, 11):
#     if i % 2 == 0: evens.append(i)
#     elif i % 3 == 0: dividable_on_3.append(i)
#     else: other.append(i)
#
# print(evens)
# print(dividable_on_3)
# print(other)


#Третя задача
# num = int(input("Введіть число для обчислення факторіала: "))
# fact=1
# for i in range(1, num+1):
#     fact*=i
# print(f"Факторіал числа {num}: ", fact)



#Четверта задача
login = input("Enter you login: ")
while True:
    if login=="First":
        print (f"Helov {login}!")
        break
    else:
        print ("Login error!")
        break

#П'ята задача
# list_1 = [input ("Ведіть елементи списку: ") for i in range(int(input('Скільки елементів списку ви хочете?: ')))]
# while list_1 != 0:
#     if list_1 < 0:
#         print('Negative numbers met', list_1)
#         break
#     else:
#         print('There are no negative numbers')
#         break