
# update
list_1 = [1, 2, 3, 4, 5, 6]
list_1[2] = 100

list_1[1:3] = []
list_1[1:3] = [20, 30, 40, 1, 2, 3, 4]

print(list_1)

# delete

# given index ,remove the element
list_1.pop(1)
print(list_1)

# delete the last element
list_1.pop()


# given the value of the element ,remove the first element of that value
list_1.remove(4)

# del given the index , remove the element
del list_1[1]
print(list_1)

del list_1[2:3]
print(list_1)

# cal the len of list
len(list_1)

list_1.sort()
list_1.reverse()

# list generator
result = [i for i in range(101) if i % 5 == 0]
print(result)

result_2 = [i**2 for i in range(10)]
print(result_2)
# all about list

list_2 = [12, 2, 1, True, 'Hello', ['a', 'b']]
list_3 = list('hello')
list_4 = []

print(list_3)

# create + *. append , insert, extend

# equals to extend
list_5 = list_2 + list_3
print(list_5)

# repeat the list many times
list_2 * 3

print(list_2)

# append a element at the end of the list
list_2.append('jiuzhang')
print(list_2)

# insert an element at the specific index  of the list
list_2.insert(2, 'abc')
print(list_2)
# concate another list to the end  the list
list_2.extend(list_3)
print(list_2)
# read , iteration, index , slice, in , count
list_2[-1]
print(list_2)
list_2[1:3]
print(list_2)
list_2[:3]
print(list_2)
list_2[1:]
print(list_2)
list_2[:-2]
print(list_2)

# in
2 in list_2

# find the index of specific value
if 2 in list_2:
    print(list_2.index(2))

# see how many elements in the list of the value
print(list_2.count(2))