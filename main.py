#
numbers = [0,3,7,9,10,28,2]
if len(numbers) == 0:
    result: 0
else:
    sum_numbers = 0
    for number in range (0, (len(numbers)), 2):
        sum_numbers += numbers[number]
    result = sum_numbers * numbers[-1]
print(result)
#
