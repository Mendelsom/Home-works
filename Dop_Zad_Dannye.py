students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

#Convert set to list and sort
list_o_st = []
for i in range(len(students)):
    st_1 = [students.pop()]
    list_o_st = list_o_st + st_1
list_sort = sorted(list_o_st)

#calculate average grades ans create dictionary
aver = []
dict_ = dict()
for i in range(0,(len(grades))):
    sum_ = 0
    for n in range (0,(len(grades[i]))):
        sum_ = sum_ + grades[i][n]
    aver.append(sum_ / (len(grades[i])))
    dict_[list_sort[i]] = aver[i]
print(dict_)
