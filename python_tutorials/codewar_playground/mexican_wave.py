word = "this is a few words"

def wave(word):
    word_list = list(word)
    space_count = word_list.count(" ")
    ans = []
    for i in range(len(word)):
        element = word_list[i]
        if element == " ":
            continue
        else:
            new_word_list = word_list.copy()
            new_word_list[i] = new_word_list[i].upper()
            new_word = "".join(new_word_list)
            ans.append(new_word)
    return ans
print(wave(word))


