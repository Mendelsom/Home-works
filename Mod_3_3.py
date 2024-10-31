def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(False) #output False строка True
print_params(1, 2, 3) #output 1,2,3
print_params('text', True) #output text True True
print_params(b=25) #output 1 25 True
print_params(c=[1,2,3]) # output 1 строка [1, 2, 3]
values_list = [True, 'text', 3]
values_dict = {'a': False, 'b': 123, 'c': 'text'}
print_params(*values_list) #output True text 3
print_params(**values_dict) #output False 123 text
values_list_2 = [[1,2,3], 'text']
print_params(values_list_2, 42) #output [[1, 2, 3], 'text'] 42 True