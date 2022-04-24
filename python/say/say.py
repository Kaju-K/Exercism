def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    list_of_magnitude = [" billion ", " million ", " thousand ", ""]
    transcripted = ""
    if number == 0:
        return "zero"
    string_number = str(number)
    number_of_magnitude = ((len(string_number)-1) // 3) + 1
    list_of_magnitude = list_of_magnitude[-1:-number_of_magnitude-1:-1]
    list_of_magnitude.reverse()
    string_number = string_number[::-1]
    listed = [string_number[3*j:(3+3*j)][::-1] for j in range(number_of_magnitude)]
    listed.reverse()
    for index_n, n in enumerate(listed):
        if n == "000":
            continue
        if len(n) == 2:
            n = "0" + n
        if len(n) == 1:
            n = "00" + n
        for index_m, m in enumerate(n):
            if index_m == 0:
                if m == "0":
                    continue
                transcripted += number_transcription(m) + " hundred "
            if index_m == 1:
                transcripted += dozens(m, n, index_m)
                if m == "1":
                    break
            if index_m == 2:
                transcripted += number_transcription(m)
        transcripted += list_of_magnitude[index_n]
    return transcripted.strip()

def number_transcription(number_string):
    storage = {"0": "", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six",
                 "7": "seven", "8": "eight", "9": "nine"}
    return storage.get(number_string)

def dozens(m, n, index_m):
    text = ""
    if m == "0":
        return text
    if m == "1":
        a = {"0": "ten", "1": "eleven", "2": "twelve", "3": "thirteen", "5": "fifteen", "8": "eighteen"}
        if n[index_m + 1] in a:
            return a.get(n[index_m + 1])
        else:
            text += number_transcription(n[index_m+1]) + "teen"
            return text
    b = {"2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "8": "eighty"}
    if m in b:
        text += b.get(m)
    else:
        text += number_transcription(m) + "ty"
    if n[index_m+1] != "0":
        text += "-"
    return text