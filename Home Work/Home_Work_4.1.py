#
# Example_1
#
lst = [0,1,0,12,3]
print(lst, end =" -> ")
x_1 = lst.pop(0)
x_2 = lst.pop(1)
lst.extend([x_1,x_2])
print(lst)
#
# Example_2
#
lst_1 = [1, 0, 13, 0, 0, 0, 5]
new_lst = []
for x in lst_1:
    if x != 0:
        new_lst.append(x)
for x in lst_1:
    if x == 0:
        new_lst.append(0)
print(lst_1, end = " -> ")
print(new_lst)
#
#
#