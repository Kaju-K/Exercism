from math import sqrt


def factors(value):
    i = 2
    list_of_primes = []
    while value != 1:
        if i > sqrt(value):
            list_of_primes.append(value)
            return list_of_primes
        if value % i == 0:
            value = value/i
            list_of_primes.append(i)
        else:
            i += 1
    return list_of_primes