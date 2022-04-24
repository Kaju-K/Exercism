def is_paired(input_string):
    open = ["(", "[", "{"]
    close = [")", "]", "}"]
    testing = []
    for bracket in input_string:
        if bracket in open:
            testing.insert(0, close[open.index(bracket)])
        elif bracket in close:
            if (testing) and (bracket == testing[0]):
                testing.remove(bracket)
            else:
                return False
    return testing == []