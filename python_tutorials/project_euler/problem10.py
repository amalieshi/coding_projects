MAX_VALUE = 2000001

prime_list = []
is_prime = lambda num: all(num%x != 0 for x in range(2,int(num**.5)+1))
for i in range(2, MAX_VALUE):
    if is_prime(i):
        prime_list.append(i)

print(sum(prime_list))




