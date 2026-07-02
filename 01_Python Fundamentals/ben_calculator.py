def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

choice = ""
while choice != "5":  
    print("===== BEN'S CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    

    choice = input("Choose an option: ")

    if choice == "1":
       num1, num2 = get_numbers()

       answer = add(num1, num2)
       print("Answer:", answer)


    elif choice == "2":
        num1, num2 = get_numbers()

        answer = subtract(num1, num2)
        print("Answer:", answer)

    elif choice == "3":
        num1, num2 = get_numbers()

        answer = multiply(num1, num2)
        print("Answer:", answer)

    elif choice == "4":
        num1, num2 = get_numbers()

        answer = divide(num1, num2)
        print("Answer:", answer)
        if num2 == 0:
            print("Error: Cannot divide by zero")
       

    elif choice == "5":
        print("Goodbye!")

    else:
        print("Invalid choice")



