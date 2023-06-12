import math

n = 30

def zeros(n):
    if n == 0:
        return 0
    kmax = math.floor(math.log(n, 5))
    Z = 0
    for i in range(1, kmax+1):
        Z += math.floor(n/5**i)
    return Z

print(zeros(n))


