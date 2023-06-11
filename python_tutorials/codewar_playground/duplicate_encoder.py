word = "dinn"

def duplicate_encoder(word):
    word = word.lower()
    encoded_output = []
    for i in word:
        if word.count(i) > 1:
            encoded_output.append(")")
        else:
            encoded_output.append("(")
    print("".join(encoded_output))
duplicate_encoder(word)