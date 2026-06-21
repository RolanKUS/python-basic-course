#
# Example_1
#
lst = [11,22,33,44,55,66]
print(lst, end = " -> ")

midle_nums = len(lst) // 2

lst_2 = lst[:midle_nums]
lst_3 = lst[midle_nums:]
new_lst = [lst_2] + [lst_3]

print(new_lst)
#
# Example_2
#
nums = [7,5,22,7,100]
print(nums, end = " -> ")

midle_nums_2 = len(nums) // 2
if len(nums) % 2 != 0:
    midle_nums_2 += 1

nums_2 = nums[:midle_nums_2]
nums_3 = nums[midle_nums_2:]
new_nums = [nums_2] + [nums_3]

print(new_nums)
#
# Example_3
#
x = []
print(x, end = " -> ")

a = len(x) // 2

x_1 = x[:a]
x_2 = x[a:]
new_x = [x_1] + [x_2]

print(new_x)