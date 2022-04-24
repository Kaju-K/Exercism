def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 1
    for i in range(2, int(pow(number, 0.5)+1)):
        if number % i == 0:
            sum += i
            if i**2 != number:
                sum += number/i
    if sum == number and number != 1:
        return "perfect"
    elif sum > number:
        return "abundant"
    else:
        return "deficient"