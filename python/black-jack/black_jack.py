"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    if card in ["K", "Q", "J"]:
        return 10
    elif card == "A":
        return 1
    elif int(card) in [i+2 for i in range(9)]:
        return int(card)

    


def higher_card(card_one, card_two):
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    if one > two:
        return card_one
    elif one < two:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A":
        return 1
    one = value_of_card(card_one)
    two = value_of_card(card_two)
    if (one + two) > 10:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    list_of_cards = ["K", "Q", "J", "10"]
    return ((card_one == "A") or (card_two == "A")) and ((card_one in list_of_cards) or card_two in list_of_cards)



def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    return 9 <= (value_of_card(card_one) + value_of_card(card_two)) <= 11