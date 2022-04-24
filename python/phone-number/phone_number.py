import re

class PhoneNumber:
    def __init__(self, input):
        self.input = input
        self.number = self.cleaning()
        self.area_code = self.cleaning()[0:3]
    def cleaning(self):
        if re.search("[!@#$:]", self.input):
            raise ValueError("punctuations not permitted")
        if re.search("[a-zA-Z]", self.input):
            raise ValueError("letters not permitted")
        self.input = "".join(re.findall('[0-9]+', self.input))
        if len(self.input) > 11:
            raise ValueError("more than 11 digits")
        elif len(self.input) == 11:
            if self.input[0] != "1":
                raise ValueError("11 digits must start with 1")
            self.input = self.input[1:]
        if len(self.input) == 10:
            if self.input[3] == "0":
                raise ValueError("exchange code cannot start with zero")
            if self.input[3] == "1":
                raise ValueError("exchange code cannot start with one")
            if self.input[0] == "0":
                raise ValueError("area code cannot start with zero")
            if self.input[0] == "1":
                raise ValueError("area code cannot start with one")
            return self.input
        elif len(self.input) < 10:
            raise ValueError("incorrect number of digits")
    def pretty(self):
        return "(" + self.number[:3] + ")-" + self.number[3:6] + "-" + self.number[6:]
