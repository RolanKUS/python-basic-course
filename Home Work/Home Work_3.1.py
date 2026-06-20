a = int(input("Enter first number: "))
action = input("Enter action: ")
b = int(input("Enter second number: "))
if action == "+":
    result = a + b
    print("result: ", result)
elif action == "-":
    result = a - b
    print("result: ", result)
elif action == "*":
    result = a * b
    print("result: ", result)
elif action == "/":
    if b == 0:
        print("Error: Division by 0 is not allowed!")
    else:
        result = a / b
        print("result: ", result)
else:
    print("Error: Invalid action!")