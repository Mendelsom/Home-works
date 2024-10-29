number_ = int(input('Введите число n '))
def fibo_(n):
    if (n == 1):
        return 0
    if (n == 2):
        return 1
    else:
        return fibo_(n - 1) + fibo_(n - 2)
print(f' Fibo(N) = {fibo_(number_)}')