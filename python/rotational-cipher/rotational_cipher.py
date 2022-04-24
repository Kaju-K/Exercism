alphabet = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    key = key % 26
    cipher = alphabet[key:] + alphabet[:key]
    rules = str.maketrans(alphabet + alphabet.upper(), cipher + cipher.upper())
    return text.translate(rules)