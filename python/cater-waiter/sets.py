from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return drink_name + " Mocktail"
    return drink_name + " Cocktail"


def categorize_dish(dish_name, dish_ingredients):
    if set(dish_ingredients).issubset(VEGAN):
        return dish_name + ": VEGAN"
    if set(dish_ingredients).issubset(VEGETARIAN):
        return dish_name + ": VEGETARIAN"
    if set(dish_ingredients).issubset(PALEO):
        return dish_name + ": PALEO"
    if set(dish_ingredients).issubset(KETO):
        return dish_name + ": KETO"
    if set(dish_ingredients).issubset(OMNIVORE):
        return dish_name + ": OMNIVORE"


def tag_special_ingredients(dish):
    return (dish[0], set(dish[1]).intersection(SPECIAL_INGREDIENTS))


def compile_ingredients(dishes):
    all_ingredients = set()
    for ingredients in dishes:
        all_ingredients = all_ingredients.union(ingredients)
    return all_ingredients


def separate_appetizers(dishes, appetizers):
    return list(set(dishes).difference(appetizers))


def singleton_ingredients(dishes, intersection):
    all_ingredients = set()
    for ingredients in dishes:
        all_ingredients = all_ingredients.symmetric_difference(ingredients)
    return (all_ingredients.symmetric_difference(intersection)).difference(intersection)
