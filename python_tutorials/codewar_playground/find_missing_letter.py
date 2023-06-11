import string
from typing import Any

chars = ['a','b','c','d','f']

def find_missing_letter(chars):
    is_upper = chars[0].isupper()
    english_alphabets =list(string.ascii_lowercase)
    lower_chars = [i.lower() for i in chars]
    start_index = english_alphabets.index(lower_chars[0])
    total_elements = len(chars) + 1
    correct_chars = english_alphabets[start_index:start_index+total_elements]
    for v in correct_chars:
        if v not in lower_chars:
            missing_letter = v
            if is_upper:
                ans = missing_letter.upper()
            else:
                ans = missing_letter
    return ans


print(find_missing_letter(chars))

