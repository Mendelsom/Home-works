number_ = int(input('Введите число n '))
fibo_ = [0, 1]
for i in range(2, number_ + 1):
    fibo_.append(fibo_[i - 1] + fibo_[i - 2])
print(f' Fibo({number_}) = {fibo_[number_ - 1]}')