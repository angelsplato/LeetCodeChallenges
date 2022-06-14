def half_reserve(number):
    rev_num = 0
    while number > number:
        rev_num = (rev_num * 10) + (number % 10)
        number = number // 10
    return rev_num


def full_reserve(number):
    rev_num = 0
    while number > 0:
        rev_num = (rev_num * 10) + (number % 10)
        number = number // 10
    return rev_num


def isPalindrome(x):
    half_number = half_reserve(x)
    if x >= 0:
        if full_reserve(half_number) == half_number:
            return True
        else:
            return False
    else:
        False


if __name__ == '__main__':
    print(isPalindrome(121))
