immutable_var = (12, True, "string123", 2.53, [5, 8, "trick"])
print(immutable_var)
# immutable_var[1] = 56 - ошибка
immutable_var[4][1] = 7
print(immutable_var)
mutable_list = [False, 2.5, "stroka"]
mutable_list[0] = 777
print(mutable_list) #все работает
