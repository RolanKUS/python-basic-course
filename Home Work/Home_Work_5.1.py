#
import string
import keyword

name = input("Enter your name: ")
result = True

if name in keyword.kwlist:
    result = False
elif name[0].isdigit():
    result = False
elif "__" in name:
    result = False
for char in name:
    if char in string.punctuation and char != "_":
        result = False
        break
    elif char == " ":
        result = False
        break
    elif char.isupper():
        result = False
print(result)
#