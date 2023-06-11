num =4822309
def descending_order(num):
    num_list = list(str(num))
    new_list = [str(i) for i in num_list]
    new_list = sorted(new_list,reverse=True)
    ans = int("".join(new_list))
    return ans
print(descending_order(num))