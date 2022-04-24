def sum_of_multiples(limit, multiples):
    all_numbers = set()
    for number in multiples:
        if number == 0:
            continue
        for multiplier in range(number, limit, number):
            all_numbers.add(multiplier)
    return sum(all_numbers)