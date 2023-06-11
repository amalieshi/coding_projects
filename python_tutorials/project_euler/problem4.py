max_multiple = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        multiple = str(i * j)
        if multiple == multiple[::-1]:
            if int(multiple) > max_multiple:
                max_multiple = int(multiple)

print(max_multiple)
