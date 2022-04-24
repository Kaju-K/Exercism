numbers = "0123456789"

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        size = len(self.card_num)
        sum = 0
        if size <= 1:
            return False
        if not(set(self.card_num).issubset(numbers)):
            return False
        for i in range(-1, -size-1, -1):
            number = int(self.card_num[i])
            if i % 2 == 1:
                sum += number
            else:
                number = number*2
                if number > 9:
                    number -= 9
                sum += number
        return sum % 10 == 0
