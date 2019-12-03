
# fixed length and immutable
str_1 = 'Hello world!'

str_2 = " jiuzhang "

# python does not support char type
# normal character and special character

# \n , '\'', '\\','\t',
# -- store in '01'
# -- ord() & chr()
# -- ord calculator the integer
# -- chr calculatopr the character

# ASCII 128
# Unicode 65535

# lowercase to uppercase
lower_char = 'z'
upper_char = chr(ord(lower_char) - ord('a') + ord('A'))
print(upper_char)
print(lower_char.upper())

# + , *
print(str_1 + str_2)
print(str_1 * 3)

# iteration , index , slice , \find , replace

for c in str_2:
    print(c, end=" ")

print(str_2[0], str_2[1:5])

print(str_2.find('h'))

print(str_2.replace('h', 'ww'))
print(str_2)

# format
"I am {} , and my score is {}".format('zhang', 100)
"I am %s , and my score is %d" %('zhang', 100)

str(100), str(10.5), float('123.4')

# len

# reverse a string
print(str_2[6:1:-1])

# join the string
strs = ['Zhang', 'is', 'nice']

result = ' '.join(strs)
print(result)





