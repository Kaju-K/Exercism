"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "Sublist"
SUPERLIST = "Superlist"
EQUAL = "Equal"
UNEQUAL = "Unequal"

def inside(list_one, list_two):             #list_one is the smaller list and here we check if one is a sublist of two
    for i in range(len(list_two) - len(list_one) + 1):
        if list_one == list_two[i: (i + len(list_one))]: 
            return True
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return "Equal"
    if inside(list_one, list_two):
        return "Sublist"
    if inside(list_two, list_one):
        return "Superlist"
    return "Unequal"