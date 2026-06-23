#
# Example_1
#
numbers = []
if len(numbers) == 0:
    result = 0
else:
    sum_numbers = 0
    for number in range (0, (len(numbers)), 2):
        sum_numbers += numbers[number]
    result = sum_numbers * numbers[-1]
print(result)
#
# Example_2
#
numbers_1 = [0,3,7,9,10,28,2]
if len(numbers_1) == 0:
    result_1= 0
else:
    sum_numbers_1 = 0
    for number_1 in range (0, (len(numbers_1)), 2):
        sum_numbers_1 += numbers_1[number_1]
    result_1 = sum_numbers_1 * numbers_1[-1]
print(result_1)
#
# Example_3
#
numbers_2 = [5]
if len(numbers_2) == 0:
    result_2 = 0
else:
    sum_numbers_2  = 0
    for number_2 in range (0, (len(numbers_2)), 2):
        sum_numbers_2 += numbers_2[number_2]
    result_2 = sum_numbers_2 * numbers_2[-1]
print(result_2)