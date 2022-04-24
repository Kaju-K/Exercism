def find_anagrams(word, candidates):
    anagrams = []
    word = word.lower()
    sorted_word = sorted(word)
    for name in candidates:
        if name.lower() == word:
            continue
        if sorted(name.lower()) == sorted_word:
            anagrams.append(name)
    return anagrams
