number = int(input("Enter a number: "))
while number > 9:
    result = 1
    temp = number
    while temp > 0:
        digit = temp % 10
        result *= digit
        temp //= 10
    number = result
print(number)