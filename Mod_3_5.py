def get_multiplied_digits(number):
    str_number = str(number)
    first = str_number[0:1]
    i_first = int(first)
    str_number = str_number[1:]

    if len(str_number) == 0:
        return i_first
    else:
        return i_first * get_multiplied_digits(int(str_number))

print(get_multiplied_digits(40203))