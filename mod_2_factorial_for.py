number_ = int(input('Введите число n '))
fact_ = 1
for i in range(2, number_ + 1):
    fact_ *= i
print(f' n! = {fact_}')