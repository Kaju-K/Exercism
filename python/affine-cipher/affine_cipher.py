import string
from math import gcd

alphabet = string.ascii_lowercase

def coding(a,b):
    new_alphabet = ""
    for index, letter in enumerate(alphabet):
        coding = (a*index + b) % 26
        new_alphabet += alphabet[coding]
    return new_alphabet

def encode(plain_text, a, b):
    if gcd(a, 26) >= 2:
        raise ValueError("a and m must be coprime.")
    plain_text = plain_text.lower()
    plain_text = "".join(filter(str.isalnum, plain_text))
    new_alphabet = coding(a,b)
    code = ""
    for index, letter in enumerate(plain_text):
        if letter in alphabet:
            code += new_alphabet[alphabet.index(letter)]
        else:
            code += letter
        if (index+1) % 5 == 0:
            if index == len(plain_text) - 1:
                break
            code += " "
    return code


def decode(ciphered_text, a, b):
    new_alphabet = coding(a,b)
    if gcd(a, 26) >= 2:
        raise ValueError("a and m must be coprime.")
    ciphered_text = ciphered_text.replace(" ", "")
    rule = str.maketrans(new_alphabet, alphabet)
    return ciphered_text.translate(rule)
