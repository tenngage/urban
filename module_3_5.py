def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if str(number).__len__() > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    return first
print(get_multiplied_digits(130902))
