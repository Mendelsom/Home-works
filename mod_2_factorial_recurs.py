number_ = int(input('Введите число n '))
def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
print(f' n! = {factorial(number_)}')

