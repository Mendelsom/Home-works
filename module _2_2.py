first = int(input('1st = '))
second = int(input('2nd = '))
third = int(input('3rd = '))
if first == second and first == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')