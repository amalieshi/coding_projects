lst = [1, 0, 1, 2, 0, 1, 3]

def move_zeros(lst):
    for i in lst:
        if i == 0:
            lst.remove(0)
            lst.append(0)
        else:
            pass
    return lst

print(move_zeros(lst))