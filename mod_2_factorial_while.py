i = 1
fact_ = 1
number_ = int(input('Введите число n '))
while i < number_:
    fact_ = fact_ * (i + 1)
    i += 1
print(f' n! = {fact_}')