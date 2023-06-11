def prime_seq(num):
    prime_seq_list = []
    for i in range(2, num):
        if prime(i):
            prime_seq_list.append(i)
        else:
            pass
    return prime_seq_list


prime = lambda num: all(num % i != 0 for i in range(2, int(num**0.5) + 1))
list = prime_seq(2000000)
print(list[10000])
