#
# Example_1
#

import string

ALL_LETTERS = string.ascii_letters

user_input = input("Enter letters in format: 'a-Z' ").strip()

first_letter = user_input[0]
second_letter = user_input[2]

start_index = ALL_LETTERS.index(first_letter)
end_index = ALL_LETTERS.index(second_letter)

print(ALL_LETTERS[start_index:end_index +1])
#
# Example_2
#

# import string
#
# letters = string.ascii_letters
#
# start, end = input("Enter letters in format: 'a-Z' ").strip().split("-")
#
# print(letters[letters.index(start):letters.index(end) + 1])
#