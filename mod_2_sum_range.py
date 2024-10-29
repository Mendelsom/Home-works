def sum_range(a, n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n == a:
        return a

    return sum_range(a,n-1) + n
a = int(input('start = '))
n = int(input('finish = '))
print(sum_range(a, n))