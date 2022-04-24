def response(hey_bob):
    sentence = hey_bob.strip()
    if sentence == "":
        return "Fine. Be that way!"
    if sentence.endswith("?"):
        if sentence.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if sentence.isupper():
        return "Whoa, chill out!"
    return "Whatever."
