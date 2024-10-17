#словари
my_dict = {'john':12, 'mary':15, 'ann': 20}
print ("Dictionary: ", my_dict)
print (my_dict["john"])
print(my_dict.get("kate"))
my_dict.update({'sue':67, 'boris': 90})
a = my_dict.pop('john')
print(a)
print ("Amended Dictionary: ", my_dict)
#множества
my_set = {True, True, 'exit', 'exit', 34, 34}
print(my_set)
my_set.update([4, 5], {1, 6, 8})
print(my_set)

