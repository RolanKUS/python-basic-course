#
# Example_1
#
first_list = [12,3,4,10,45,7,9]
print(first_list)
x_1 = first_list.pop(6)
first_list.insert(0,x_1)
print(first_list)
#
# Example_2
#
lst = [3,5,26,7,8]
print(lst)
if len(lst) > 0:
    lst.insert(0, lst.pop())
print(lst)
#
# Example_3
#
nums = [0,5,7,2,2,5,9,321]
print(nums)
if len(nums) > 0:
    nums.insert(0, nums[-1])
    del nums[-1]
print(nums)
#
# Example_4
#
nums_2 = [11,12,13,22,33,44]
print(nums_2)
if len(nums_2) > 0:
    nums_2.insert(0, nums_2[-1])
    nums_2.pop()
print(nums_2)
#
# Example_5
#
lst_2 = [9,9,9,4,55,20]
print(lst_2)
lst_2.remove(20)
lst_2.insert(0,20)
print(lst_2)
#
# Example_6
#
lst_3 = [100,90,80,70,60]
print(lst_3)
print(lst_3[-1:] + lst_3[:-1])
#
