array1 = ['live', 'arp', 'strong']

array2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def in_array(array1, array2):
    output =[]
    for i in array1:
        for j in array2:
            if j.find(i)!=-1 and i not in output:
                output.append(i)
    return sorted(output)

print(in_array(array1,array2))