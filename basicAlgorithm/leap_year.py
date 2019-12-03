year = 2000
is_leap_year = False

if year % 4 == 0 and year % 100 != 0:
    is_leap_year = True
elif year % 400 == 0:
    is_leap_year = True
else:
    is_leap_year = False

print(is_leap_year)
