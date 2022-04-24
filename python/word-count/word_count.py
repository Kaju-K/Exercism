from collections import Counter

def count_words(sentence):
    sentence = sentence.lower()
    pontuation = "!&@$%^&,.:;_-"
    empty_spaces = ""
    for character in pontuation:
        empty_spaces += " "
    map_of_pontuation = str.maketrans(pontuation, empty_spaces)
    sentence = sentence.translate(map_of_pontuation)
    sentence = sentence.split()
    for words in range(len(sentence)):
        sentence[words] = sentence[words].strip("'")
        sentence[words] = sentence[words].strip('"')
    return Counter(sentence)
