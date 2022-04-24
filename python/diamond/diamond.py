import string

alphabet = string.ascii_uppercase

def rows(letter):
    letter_index = alphabet.index(letter)
    diamond = ["" for i in range(letter_index*2 + 1)]
    for index, row in enumerate(diamond):
        if index == 0:
            diamond[index] = " "*(letter_index-index) + alphabet[index] +" "*(letter_index-index)
        elif index <= letter_index:
            diamond[index] = " "*(letter_index-index) + alphabet[index] + " "*(2*index-1) + alphabet[index] + " "*(letter_index-index)
        elif index == len(diamond) - 1:
            index_2 = len(diamond) - 1 - index
            diamond[index] = " "*(letter_index-index_2) + alphabet[index_2] +" "*(letter_index-index_2)
        else:
            index_2 = len(diamond) - 1 - index
            diamond[index] = " "*(letter_index-index_2) + alphabet[index_2] + " "*(2*index_2-1) + alphabet[index_2] + " "*(letter_index-index_2)
    return diamond
