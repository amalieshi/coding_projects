def count_visible_trees(check_previous_elements, matrix, i, j):
    check_element = matrix[i][j]
    for count, previous_element in enumerate(check_previous_elements):
        if previous_element >= check_element:
            return count + 1
    return len(check_previous_elements)


def visible_distance_on_left(matrix, i, j):
    check_previous_elements = matrix[i][:j]
    check_previous_elements.reverse()
    return count_visible_trees(check_previous_elements, matrix, i, j)


def visible_distance_on_right(matrix, i, j):
    check_previous_elements = matrix[i][j + 1 :]
    return count_visible_trees(check_previous_elements, matrix, i, j)


def visible_distance_towards_top(matrix, i, j):
    check_previous_elements = [value[j] for value in matrix]
    check_previous_elements = check_previous_elements[:i]
    check_previous_elements.reverse()
    return count_visible_trees(check_previous_elements, matrix, i, j)


def visible_distance_towards_bottom(matrix, i, j):
    check_previous_elements = [value[j] for value in matrix]
    check_previous_elements = check_previous_elements[i + 1 :]
    return count_visible_trees(check_previous_elements, matrix, i, j)
