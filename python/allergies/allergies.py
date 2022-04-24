class Allergies:

    allergies = {1: "eggs", 2: "peanuts", 4: "shellfish", 8: "strawberries", 16: "tomatoes", 32: "chocolate", 64: "pollen", 128: "cats"}
    ratings = list(allergies.keys())
    ratings.sort(reverse=True)

    def __init__(self, score):
        self.score = score % 256

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        alergic = []
        for i in self.ratings:
            if i <= self.score:
                self.score -= i
                alergic.append(self.allergies[i])
        return alergic