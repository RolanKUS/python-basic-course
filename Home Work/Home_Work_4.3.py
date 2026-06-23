#
# Example_1
#
import random

my_list =[]
for new_nums in range(random.randint(3,10)):
    my_list.append(random.randint(1,100))
print(my_list, end=" -> ")
my_list_2 = [my_list[0], my_list[1], my_list[-2]]
print(my_list_2)
#
# Example_2
#
qwerty = [random.randint(1,100) for i in range(random.randint(3,10))]
print(qwerty, end=" -> ")
result =[qwerty[0], qwerty[1], qwerty[-2]]
print(result)
#
