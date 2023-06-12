s =  'aabb'

def first_non_repeating_letter(s):
    string_lower = s.lower()
    if s == "":
        return ""
    is_unique = False
    for i in string_lower:
        if string_lower.count(i) == 1:
            output_index = string_lower.index(i)
            is_unique = True
            return s[output_index]
        elif string_lower.count(i)==len(string_lower):
            return ""
    if not is_unique:
        return ""




print(first_non_repeating_letter(s))