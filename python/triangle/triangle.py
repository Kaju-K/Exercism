def triangle(sides):
    if 0 in sides:
        return False
    elif max(sides) <= sum(sides) - max(sides):
        return True 

def equilateral(sides):
    if triangle(sides):
        if sides[0] == sides[1] == sides[2]:
            return True
    return False


def isosceles(sides):
    if triangle(sides):
        if (sides[0] == sides[1]) or (sides[1] == sides[2]) or (sides[0] == sides[2]) or equilateral(sides):
            return True
    return False


def scalene(sides):
    if triangle(sides):
        if (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[2] != sides[1]):
            return True
    return False
