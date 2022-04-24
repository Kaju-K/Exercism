def flatten(iterable):
    result = []
    if iterable == []:
        return iterable
    for i in iterable:
        if i == [] or i == None:
            continue
        if type(i) == int:
            result.append(i)
        elif type(i) == list:
            sub_list = flatten(i)
            for j in sub_list:
                result.append(j)
    return result
