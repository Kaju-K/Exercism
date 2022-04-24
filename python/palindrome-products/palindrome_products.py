def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    products_values = {min_factor**2-1: 0}                              #here we create a dictionary because we want to associate the palindrome with the pairs of products
    for item in range(max_factor, min_factor- 1, -1):                   #the value of min_factor**2 - 1 is because all the numbers tested are ging to be higher then this
        for second_number in range(item, min_factor - 1, -1):           #this goes from item to min_factor because otherwise we would checking the same products again since a*b = b*a
            palindrome = item*second_number
            if palindrome < list(products_values)[0]:                   #in case the product is lower than the number that we have, we should skip this for because all the next numbers are necessarily going to be lower
                break
            if str(palindrome) == str(palindrome)[::-1]:
                if palindrome > list(products_values)[0]:
                    products_values = {}                                    #in case we find a higher palindrome we erase the previous one
                    products_values[palindrome] = [[item, second_number]]   #and add the numbers that generate it 
                    break
                products_values[palindrome].append([item, second_number])   #if the product has the same value, we add the new combination that generates the palindrome
        if item**2 < list(products_values)[0]:
            break
    if products_values[list(products_values)[0]] != 0:                      #this tests if we added something to the dictionary
        largest_palindrome = list(products_values)[0]
        return (largest_palindrome, products_values[largest_palindrome])    #if yes, return the result
    return (None, [])                                                       #if no, (None, [])


def smallest(min_factor, max_factor):                   #Same things for this function, but instead of highest we take the lowest
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    products_values = {max_factor**2+1: 0}
    for item in range(min_factor, max_factor + 1):
        for second_number in range(item, max_factor + 1):
            palindrome = item*second_number
            if palindrome > list(products_values)[0]:
                break
            if str(palindrome) == str(palindrome)[::-1]:
                if palindrome < list(products_values)[0]:
                    products_values = {}
                    products_values[palindrome] = [[item, second_number]]
                    break
                products_values[palindrome].append([item, second_number])
        if item**2 > list(products_values)[0]:
            break
    if products_values[list(products_values)[0]] != 0:
        smallest_palindrome = list(products_values)[0]
        return (smallest_palindrome, products_values[smallest_palindrome])
    return (None, [])