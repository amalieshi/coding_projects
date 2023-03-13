def check_tree_height(check_previous_elements, matrix, i, j):
    check_element = matrix[i][j]
    for previous_element in check_previous_elements:
        if previous_element >= check_element:
            return False
    return True


def is_visible_from_left(matrix, i, j):
    check_previous_elements = matrix[i][:j]
    return check_tree_height(check_previous_elements, matrix, i, j)
    # return check_element > max(check_previous_elements, default = -1)


def is_visible_from_right(matrix, i, j):
    check_previous_elements = matrix[i][j + 1 :]
    return check_tree_height(check_previous_elements, matrix, i, j)


def is_visible_from_top(matrix, i, j):
    check_previous_elements = [value[j] for value in matrix]
    check_previous_elements = check_previous_elements[:i]
    return check_tree_height(check_previous_elements, matrix, i, j)


def is_visible_from_bottom(matrix, i, j):
    check_previous_elements = [value[j] for value in matrix]
    check_previous_elements = check_previous_elements[i + 1 :]
    return check_tree_height(check_previous_elements, matrix, i, j)
