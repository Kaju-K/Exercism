import re

vowels = "aeiou"

def translate(text):
    translation = ""
    text = text.split()
    for word in text:
        i = 0
        if (bool(re.search(f"^[{vowels}]", word)) or
        bool(re.search(f"^xr", word)) or
        bool(re.search(f"^yt", word))):
            translation += word + "ay "
            break
        for index, letter in enumerate(word):
            if letter not in vowels:
                if letter == "q" and word[index+1] == "u":
                    i += 2
                    break
                if word[index + 1] == "y":
                    i += 1
                    break
                i += 1
            else:
                break
        translation += word[i:] + word[:i] + "ay "
    return translation.strip()
