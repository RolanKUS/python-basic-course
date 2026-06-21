# assignment 1
# example 1
print(5**2)
# example 2
number = int(input("Enter a number: ")) # 5
print(f"square of the number: {number**2}")
# assignment 2
# example 1
n1 = 2
n2 = 4
n3 = 6
result = (n1 + n2 + n3) / 3
print(result)
# example 2
n1 = int(input("Enter a number: ")) # 2
n2 = int(input("Enter a number: ")) # 4
n3 = int(input("Enter a number: ")) # 6
average_value = (n1 + n2 + n3) / 3
print(f"average_value: {average_value}")
# assignment 3
minutes = int(input("Enter the number of minutes: ")) # 135
hours = minutes // 60
rem_minutes = minutes % 60
print(f"{hours} hours {rem_minutes} minutes ")
# assignment 4
price = int(input("Enter the price: ")) # 1000
discount = int(input("Enter a discount (%): ")) # 15
discount = price * discount / 100
final_price = price - discount
print(f"final_price: {final_price:}")
# assignment 5
number = int(input("Enter your number: ")) # 347
last_digit = number % 10
print(f"last_digit: {last_digit:}")
# assignment 6
length = int(input("Enter length: ")) # 5
width = int(input("Enter width: ")) # 3
perimeter = length * 2 + width * 2
print(f"The perimeter of a rectangle: {perimeter}")
# assignment 7
number = int(input("Enter your number: ")) # 9234
n1 = number // 1000
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number % 10
print(n1)
print(n2)
print(n3)
print(n4)