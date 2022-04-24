def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    sum = 0
    for index, number in enumerate(isbn):
        if number == "X" and index == 9:
            sum += 10*(10-index)
        elif number in "0123456789":
            sum += int(number)*(10-index)
        else:
            return False
    return sum % 11 == 0
