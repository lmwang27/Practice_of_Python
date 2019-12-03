num = 123
digit1 = num % 10
digit2 = num // 10 % 10
digit3 = num // 100

num_reverse = digit1*100 + digit2*10 + digit3
print("reverse of num is " + str(num_reverse))