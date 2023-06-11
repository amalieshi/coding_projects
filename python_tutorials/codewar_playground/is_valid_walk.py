walk =['w','e','w','e','w','e','w','e','w','e','w','e']
def is_valid_walk(walk):
    total_walk_time = len(walk)
    if total_walk_time == 10:
        is_on_time = True
    else:
        is_on_time = False
    horizontal_walk = 0
    vertical_walk = 0
    for i in walk:
        if i == "n":
            vertical_walk += 1
        elif i == "s":
            vertical_walk -= 1
        elif i == "e":
            horizontal_walk += 1
        elif i =="w":
            horizontal_walk -= 1
    position_to_origin = (abs(horizontal_walk)+abs(vertical_walk))
    if position_to_origin == 0:
        return_to_origin = True
    else:
        return_to_origin =  False
    if return_to_origin and is_on_time:
        return True
    else:
        return False
print(is_valid_walk(walk))

