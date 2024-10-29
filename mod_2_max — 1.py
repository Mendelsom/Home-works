def max(var_):
    var_.sort()
    return var_[len(var_) -1]

str_ = input('Вводите цифры через пробел, по окончании - Enter ')

list_ = str_.split(' ')
list_1 = []
for i in range (len(list_)):
    x_ = int(list_[i])
    list_1.append(x_)
print('max = ', max(list_1))