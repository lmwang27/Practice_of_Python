def find_number(nums, target):
    for num in nums:
        if num == target:
            return True
    return False

# python could return  not only one value#


def swap(a, b):
    a, b = b, a
    return a, b


def get_grade(score1):
    if score1 >= 85:
        return 'A'
    elif score1 >= 75:
        return 'B'
    elif score1 >= 65:
        return 'C'
    else:
        return 'D'


if __name__ == '__main__':
    score = 78
    print(get_grade(score))

    num1 = 10
    num2 = 20
    num1, num2 = swap(num1, num2)
    print(num1, num2)
