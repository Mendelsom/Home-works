def max(var_):
    var_.sort()
    return var_[len(var_) -1]

i = 1
list_ = []
while i != 0:
    num_ = int(input('введите число --- '))
    print(f'введено {num_} ')
    list_.append(num_)
    i = int(input("если будете вводить еще, введите 1, если нет, введите 0 --- "))
print('max = ', max(list_))