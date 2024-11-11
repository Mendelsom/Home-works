def calculate_structure_sum(*obj_, sum_ = 0):

    for i in obj_:
        if isinstance(i, (int, float)):
            sum_+= i
        elif isinstance(i, str):
            sum_+= len(i)
        elif isinstance(i, dict):
            i = list(i.items())
            sum_ = calculate_structure_sum(*i, sum_)
        else:
            sum_= calculate_structure_sum(*i, sum_)
    return sum_


obj_ = [  [1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),  "Hello",  ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(calculate_structure_sum(obj_))