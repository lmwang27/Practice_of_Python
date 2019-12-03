# tuple , is fixed length and immutable

tuple_1 = (1, 2, 15.6, True, [1, -1])
tuple_2 = tuple('hello')
tuple_4 = (20,)

# read only
for x in tuple_1:
    print(x)


tuple_1[1], tuple_1[3]
tuple_1[0:3]


tuple_1.index(2)

tuple_1.count(2)

len(tuple_1)

tuple([1, 2, 3])
list((1, 2, 3))