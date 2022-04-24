def primes(limit):
    list_of_primes = []
    marked_numbers = set()
    if limit < 2:
        return []
    for number in range(2, limit + 1):
        if number not in marked_numbers:
            list_of_primes.append(number)
        for multiple in range(number, limit+1, number):
            marked_numbers.add(multiple)
    return list_of_primes
