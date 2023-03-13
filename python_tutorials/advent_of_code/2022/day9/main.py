from typing import Set, Tuple
from calculate_planck_lengths import move_or_stay

with open("data.txt", "r") as f:
    data = f.read().splitlines()

horizontal_position = 0
vertical_position = 0
starting_coordinate = (horizontal_position, vertical_position)
all_head_coordinates = [starting_coordinate]
all_tail_coordinates = [starting_coordinate]
head_coordinate = starting_coordinate
for loop, directive in enumerate(data):
    direction = directive[0]
    steps: int = int(directive[2])
    for step in range(steps):
        if direction == "R":
            horizontal_position += 1
        elif direction == "L":
            horizontal_position -= 1
        elif direction == "U":
            vertical_position += 1
        elif direction == "D":
            vertical_position -= 1
        head_coordinate = (horizontal_position, vertical_position)
        all_head_coordinates.append(head_coordinate)

counter = 0
for loop, directive in enumerate(data):
    direction = directive[0]
    steps: int = int(directive[2])
    for step in range(steps):
        expected_head_coordinate = all_head_coordinates[counter + 1]
        current_head_coordinate = all_head_coordinates[counter]
        current_tail_coordinate = all_tail_coordinates[-1]
        if counter < len(all_head_coordinates) - 2 and counter != 0:
            expected_tail_coordinate = move_or_stay(
                expected_head_coordinate, current_head_coordinate, current_tail_coordinate
            )
        else:
            expected_tail_coordinate = current_tail_coordinate
        all_tail_coordinates.append(expected_tail_coordinate)
        counter += 1

tail_tuple = tuple(all_tail_coordinates)
print(len(tail_tuple))

matched_solution_tail = [(item[1], item[0]) for item in all_tail_coordinates]

with open('my_answer.txt', 'w') as f:
    f.writelines(str(matched_solution_tail))

# print(f"There are {len(all_head_coordinates)} positions that the head has visited.")
# print(
#     f"There are {len(set(all_head_coordinates))} positions that the head has visited at least once."
# )
# print(f"There are {len(all_tail_coordinates)} positions that the tail has visited.")
set_tail = set(all_tail_coordinates)
print(
    f"There are {len(set_tail)} positions that the tail has visited at least once."
)

