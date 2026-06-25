#
while True:
    a = int(input("Enter first number: "))
    action = input("Enter action: ")
    b = int(input("Enter second number: "))
    if action == "+":
        print(a + b)
    elif action == "-":
        print(a - b)
    elif action == "*":
        print(a * b)
    elif action == "/":
        if b == 0:
            print("Error: Division by 0 is not allowed!")
        else:
            print(a / b)
    else:
        print("Error: Invalid action!")
    while True:
        again = input("Do you want to continue? (y/n): ").lower()
        if again == "y":
            break
        elif again == "n":
            print("Goodbye!")
            exit()
        else:
            print("Please enter 'y' or 'n'.")
#