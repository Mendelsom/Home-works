students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

#Convert set to list and sort
list_stud = list(students)
list_stud.sort()
#calculate average grades ans create dictionary
aver = []
dict_ = dict()
for i in range(0,(len(grades))):
    sum_ = 0
    for n in range (0,(len(grades[i]))):
        sum_ = sum_ + grades[i][n]
    aver.append(sum_ / (len(grades[i])))
    dict_[list_stud[i]] = aver[i]
print(dict_)