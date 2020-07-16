#Задача 1. Знаходження середнього арифметичного

# def suma(*args):
#     """This function calculates the arithmetic mean of a non-empty
#     arbierary number of numerical values"""
#     return sum(args)/len(args)
#
# list = []
#
# print (suma(*list))

#Задача 2. Знаходження абсолютного значення числа

# nums=int(input("Enter a number: "))
# def abs(nums):
#     """This function returns the absolute value of the number"""
#     if nums>=0:
#         return nums
#     else:
#         return nums*(-1)
#
# print ("Абсолютне значення числа дорівнює", abs(nums))
#
# Задача 3. Знаходження максимального числа з двох чисел

# num1=int(input("Введіть перше число: "))
# num2=int(input("введіть друге число: "))
#
# def printMax(num1, num2):
#     """This function compares two numbers with each other"""
#     if num1>num2:
#         return (f"{num1} більше від {num2}")
#     elif num1 == num2:
#         return (f"{num1} рівне з {num2}")
#     else:
#         return (f"{num2} більше від {num1}")
#     pass
#
# print(printMax(num1, num2))

#Задача 4. Обчислення полощі трикутника, прямокутника та кола
#Перший варіант виконання задачі
#
# p=3.14
#
# def main():
#     """This function calculates the area of ​​a rectangle, triangle, and circle"""
#     while True:
#         what=input("What will we look for? (1-area_triangle,2-area_rectangle,3-area_circle): ")
#         if what == "1": side = float(input("Enter a side: ")); height = float(input("Enter a height: ")); print("Area triangle: ", (side/2)*height)
#         elif what == "2": side1 = float(input("Enter a side_1: ")); side2 = float(input("Enter a side_2: ")); print("Area rectangle: ", side1*side2)
#         elif what == "3": radius = float(input("Enter a radius_circle: ")); print("Area circle: ", p*(radius**2))
# if __name__ == "__main__":
#             main()

#Другий варіант виконання задачі

# def area_triangle(side, height):
#     """This function calculates the area of ​​a rectangle"""
#     return "Area triangle: ", (side/2)*height
#
# def area_rectangle(side1, side2):
#     """This function calculates the area of ​​a triangle"""
#     return "Area rectangle: ", side1*side2
#
# def area_circle(radius):
#     """This function calculates the area of ​​a circle"""
#     return "Area circle: ", p*(radius**2)
#
# what=input("What will we look for? (1-area_triangle,2-area_rectangle,3-area_circle): ")
# if what == "1": side = float(input("Enter a side: ")); height = float(input("Enter a height: ")); print(area_triangle(side, height))
# elif what == "2": side1 = float(input("Enter a side_1: ")); side2 = float(input("Enter a side_2: ")); print (area_rectangle(side1, side2))
# elif what == "3": radius = float(input("Enter a radius_circle: ")); print (area_circle(radius))

#Задача 5. Знаходження суми введених цифр

# def suma(sum):
#    """This function calculates the sum of the digits of the entered number"""
#     num = int(input("Enter a number: "))
#     sum = 0
#     while (num != 0):
#         sum = sum + num % 10
#         num = num // 10
#     return f'The sum of the number is equal: {sum}'
#
# print(suma(sum))

#Задача 6. Калькулятор


def addition(numb1, numb2):
    """This function adds numbers"""
    return f"Your result: {numb1+numb2}"
def subtraction(numb1, numb2):
    """This function subtracts numbers"""
    return f"Your result: {numb1-numb2}"
def multiplication(numb1, numb2):
    """This function multiply numbers"""
    return f"Your result: {numb1*numb2}"
def division(numb1, numb2):
    """This function divides numbers"""
    return f"Your result: {numb1/numb2}"
def elevation_to_a_degree(numb1, numb2):
    """This function raises the number to a degree"""
    return f"Your result: {numb1**numb2}"
def the_division_is_aimed(numb1, numb2):
    """This function is a whole number"""
    return f"Your result: {numb1//numb2}"
def the_remainder_of_the_division(numb1, numb2):
    """This function finds the remainder of the division"""
    return f"Your result: {numb1%numb2}"

what=input("What are we going to do? (+, -, *, /, **, //, %): ")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
if what == "+": print(addition(num1, num2))
elif what == "-": print(subtraction(num1, num2))
elif what == "*": print(multiplication(num1, num2))
elif what == "/": print(division(num1, num2))
elif what == "**": print(elevation_to_a_degree(num1, num2))
elif what == "//": print(the_division_is_aimed(num1, num2))
elif what == "%": print(the_remainder_of_the_division(num1, num2))

print("Thank you for using my software product!")