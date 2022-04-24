from itertools import permutations

def drinks_water():
    return solving()[1]

def owns_zebra():
    return solving()[0]

def solving():
    for nationality in permutations(["Englishman", "Norwegian", "Spaniard", "Japanese", "Ukrainian"]):
        if nationality.index("Norwegian") == 0:
            for drinks in permutations(["coffee", "tea", "milk", "orange", "water"]):
                if (drinks.index("milk")) == 2 and (drinks.index("tea") == nationality.index("Ukrainian")):
                    for animals in permutations(["fox", "snails", "horse", "dog", "zebra"]):
                        if (animals.index("dog") == nationality.index("Spaniard")):
                            for cigars in permutations(["lucky", "old", "chesterfields", "kools", "parliaments"]):
                                if (cigars.index("old") == animals.index("snails")) and (abs(cigars.index("chesterfields") - animals.index("fox")) == 1) and (abs(cigars.index("kools") - animals.index("horse")) == 1) and (cigars.index("lucky") == drinks.index("orange")) and (cigars.index("parliaments") == nationality.index("Japanese")):
                                    for colors in permutations(["red", "ivory", "yellow", "green", "blue"]):
                                        if (colors.index("red") == nationality.index("Englishman")) and (colors.index("green") == drinks.index("coffee")) and (colors.index("green") - colors.index("ivory") == 1) and (colors.index("yellow") == cigars.index("kools")) and (abs(colors.index("blue")-nationality.index("Norwegian")) == 1):
                                            return (nationality[animals.index("zebra")], nationality[drinks.index("water")])