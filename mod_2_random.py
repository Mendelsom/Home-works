import random
number = random.randint(1, 100)
n = 0
num_ = 101
min = 0
max = 100
while num_ != number:
    # num_ = int(input("Введите число  "))
    n += 1
    num_ = (random.randint(min, max))
    if num_ > number:
        print(f'Загаданное число меньше {num_}')

    elif num_ < number:
        print(f'Загаданное число больше {num_}')

print(f"Программа угадала {number} c {n}-й попытки")