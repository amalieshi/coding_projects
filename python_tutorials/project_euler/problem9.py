MAX_VAL = 400

def pythagorean_triplet(MAX_VAL):
    for i in range(1, MAX_VAL):
        for j in range(1, MAX_VAL):
            k = 1000 - i - j
            if i**2 + j**2 == k**2:
                return i*j*k

print(pythagorean_triplet(MAX_VAL))