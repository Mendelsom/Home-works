number = int(input('number '))
posled = []  # list returning encripted number
j = 0  # j is a counter of cases when the  number is dividable for smaller number
for i in range(1, number):
    x_ = number - i
    y_ = number - x_
    if y_ >= x_:  # check if a number is
        break
        if number % (i + 2) == 0:  # check if a number is dividable for smaller numbers
            j += 2
            x_1 = (i + 2) - 1
            y_1 = (i + 2) - x_1
            posled.insert(j - 2, x_1)
            posled.insert(j - 2, y_1)
            posled.append(y_)
            posled.append(x_)
    else:
        posled.append(y_)
        posled.append(x_)
print(''.join(map(str, posled)))  # converting list to string




