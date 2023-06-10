MAX_VAL = 4000000
fibonacci_num_list = [1,2]
fibonacci_num_list.append(sum(fibonacci_num_list[-2:]))
while fibonacci_num_list[-1] < MAX_VAL:
    fibonacci_num_list.append(sum(fibonacci_num_list[-2:]))
# print(fibonacci_num_list)
sum_even_num = 0
for i in fibonacci_num_list:
    if i % 2 == 0:
        sum_even_num += i
print(sum_even_num)

