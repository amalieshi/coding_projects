input = 100


def sum_square_difference(input):
    sum_of_square = 0
    square_of_sum = 0
    for i in range(1, input + 1):
        sum_of_square += i**2
        square_of_sum += i
    square_of_sum = square_of_sum**2
    diff = square_of_sum - sum_of_square
    return diff


print(sum_square_difference(input))
