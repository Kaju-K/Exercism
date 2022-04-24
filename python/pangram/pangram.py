import string
alphabet = string.ascii_lowercase

def is_pangram(sentence):
    sentence = sentence.lower()
    all_characters = set(sentence)
    for letter in alphabet:
        if letter not in all_characters:
            return False
    return True
