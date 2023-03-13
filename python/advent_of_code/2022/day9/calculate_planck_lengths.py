def move_or_stay(
    expected_head_coordinate, current_head_coordinate, current_tail_coordinate
):
    horizontal_planck_length = abs(expected_head_coordinate[0] - current_tail_coordinate[0])
    vertical_planck_length = abs(expected_head_coordinate[1] - current_tail_coordinate[1])
    planck_lengths = [horizontal_planck_length, vertical_planck_length]
    planck_lengths = set(sorted(planck_lengths))
    if planck_lengths in [{0, 2}, {1, 2}, (2, 2)]:
        return current_head_coordinate
    else:
        return current_tail_coordinate
