from check_height_from_directions import (
    is_visible_from_left,
    is_visible_from_bottom,
    is_visible_from_top,
    is_visible_from_right,
)

from scenic_score_count import (
    visible_distance_towards_top,
    visible_distance_on_left,
    visible_distance_on_right,
    visible_distance_towards_bottom,
)

with open("data.txt", "r") as f:
    data = f.readlines()

visible_tree_count = 0
tree_height_arr = []
for row in data:
    tree_height = row.strip("\n")
    tree_height_list = [int(i) for i in tree_height]
    tree_height_arr.append(tree_height_list)

print("Part 1.-----------------------------------------------")
for i in range(len(tree_height_arr)):
    for j in range(len(tree_height_arr[0])):
        if (
            is_visible_from_left(tree_height_arr, i, j)
            or is_visible_from_right(tree_height_arr, i, j)
            or is_visible_from_top(tree_height_arr, i, j)
            or is_visible_from_bottom(tree_height_arr, i, j)
        ):
            visible_tree_count += 1

print(f"There are {visible_tree_count} visible trees in total")

height = len(tree_height_arr)
width = len(tree_height_arr)
edge_trees = 2 * (height + width) - 4
print(f"There are {edge_trees} on the edges")

interior_visible_tree = visible_tree_count - edge_trees
print(f"There are {interior_visible_tree} trees in the interior that are visible")


print("Part 2. ----------------------------------------")
max_scenic_score = 0
for i in range(len(tree_height_arr)):
    for j in range(len(tree_height_arr[0])):
        scenic_score = (
            visible_distance_towards_top(tree_height_arr, i, j)
            * visible_distance_on_left(tree_height_arr, i, j)
            * visible_distance_on_right(tree_height_arr, i, j)
            * visible_distance_towards_bottom(tree_height_arr, i, j)
        )
        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
print(f"The scenic score is {max_scenic_score} points")
