list_1 = [12, 56, True, 'hello', ['a', 'b']]
list_2 = list_1

# get their memory id
print(id(list_1), id(list_2), list_1 is list_2)

list_1[1] = -3
print(id(list_1), id(list_2), list_1 is list_2)

list_2 = list_1[:]

# == 判断值是否一样？
# is判断是否是同一个对象

print(id(list_1), id(list_2), list_1 is list_2, list_1 == list_2)

# only modify the object , not the address is ok
my_tuple = 12, 34, 'abc', [6, 7], 45, 67
my_tuple[3].append(20)
print(my_tuple)



