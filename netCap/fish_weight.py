import functools


def multiplier(x, y):
    return x * y


double = functools.partial(multiplier, y=2)
triple = functools.partial(multiplier, y=3)

print('Double of 2 is {}'.format(double(5)))

multiplier_partials = []
for i in range(1, 11):
    function = functools.partial(multiplier, i)
    multiplier_partials.append(function)

print('Product of 1 and 2 is {}'.format(multiplier_partials[0](2)))
print('Product of 3 and 2 is {}'.format(multiplier_partials[2](2)))
print('Product of 9 and 2 is {}'.format(multiplier_partials[8](2)))

# python code to demonstrate working of reduce()

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

