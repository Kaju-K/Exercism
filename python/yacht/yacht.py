from collections import Counter
from sre_constants import BIGCHARSET

# Score categories.
# Change the values as you see fit.
YACHT = "Yacht"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "Full House"
FOUR_OF_A_KIND = "Four of a Kind"
LITTLE_STRAIGHT = "Little S"
BIG_STRAIGHT = "Big S"
CHOICE = "Choice"

def one_to_six(number, category):
    return category * number.get(category, 0)

def score(dice, category):
    numbers = Counter(dice)
    numbers_list = list(numbers)
    numbers_values = list(numbers.values())
    if category == YACHT:
        if len(numbers) == 1:
            return 50
        return 0
    if category in [1, 2, 3, 4, 5, 6]:
        return one_to_six(numbers, category)
    if category == FULL_HOUSE:
        if (len(numbers) == 2) and (2 in numbers.values()):
            return sum(dice)
        return 0
    if category == FOUR_OF_A_KIND:
        if 4 in numbers.values():
            return 4*numbers_list[numbers_values.index(4)]
        if 5 in numbers.values():
            return 4*numbers_list[0]
        return 0
    if category == LITTLE_STRAIGHT:
        if len(numbers) == 5 and (6 not in numbers):
            return 30
        return 0
    if category == BIG_STRAIGHT:
        if len(numbers) == 5 and (1 not in numbers):
            return 30
        return 0
    if category == CHOICE:
        return sum(dice)