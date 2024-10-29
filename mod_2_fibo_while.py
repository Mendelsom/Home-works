fibo_ = [0, 1]
i = 2
number_ = int(input('Введите число n '))
while 1 < i < number_:
    fibo_.append(fibo_[i - 1] + fibo_[i - 2])
    i += 1
print(f' Fibo({number_}) = {fibo_[number_ - 1]}')