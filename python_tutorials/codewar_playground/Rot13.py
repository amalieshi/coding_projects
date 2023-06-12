import string

message = 'Test'

alphabets_lower = list(string.ascii_lowercase)*2
alphabets_cap = [i.upper() for i in alphabets_lower]

def rot13(message):
    output = ""
    for i in list(message):
        if i.isupper():
            output+=(alphabets_cap[alphabets_cap.index(i)+13])
        elif i.islower():
            output+=(alphabets_lower[alphabets_lower.index(i)+13])
        else:
            output+=i
    return output

print(rot13(message))

