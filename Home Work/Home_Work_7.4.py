#
# Example_1
#
def common_elements():
    list3 = []
    for x in range(100):
        if x % 3 == 0:
            list3.append(x)

    list5 = []
    for x in range(100):
        if x % 5 == 0:
            list5.append(x)
    return set(list3) & set(list5)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Ok")
#
# Example_2
#
def common_elements():
    list3 = [x for x in range(100) if x % 3 == 0]
    list5 = [x for x in range(100) if x % 5 == 0]
    return set(list3) & set(list5)
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Ok")
