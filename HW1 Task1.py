def main():
    while True:
        what=input("Що будем робити? (+, -, /, *, **, //, %): ")

        first_number=float (input("Ведіть перше чило: "))
        second_number=float (input("Ведіть друге чило: "))

        if what == "+":
            resultat = first_number+second_number
            print("Результат: ", resultat)
        elif what == "-":
            print("Результат: ", first_number-second_number)
        elif what == "/":
            print("Результат: ", first_number/second_number)
        elif what == "*":
            print("Результат: ", first_number*second_number)
        elif what == "**":
            print("Результат: ", first_number**second_number)
        elif what == "//":
            print("Результат: ", first_number//second_number)
        elif what == "%":
            print("Результат: ", first_number%second_number)
        else:
            print("Введено невірний символ")

if __name__ == "__main__":
            main()



