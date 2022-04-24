class BowlingGame:
    def __init__(self):
        self.points = 0
        self.pins = []
        self.frame = 0
        self.time = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Value should be between 0 and 10")
        if pins == 10:
            if self.frame == 10 and (self.pins[-1] == 10 or sum(self.pins[-2:]) == 10):
                self.frame -= 1
            self.frame += 1
        if self.time == 0 and pins != 10:
            if self.frame == 10 and (self.pins[-1] != 10 and sum(self.pins[-2:]) != 10):
                raise ValueError("Game already has 10 frames")
            self.time += 1
        elif self.time == 1:
            if pins + self.pins[-1] > 10:
                raise ValueError("Two throws in a frame cannot score more than 10")
            self.time = 0
            if self.frame == 10 and self.pins[-2] == 10:
                self.frame -= 1
            self.frame +=1
        if self.frame > 10:
            raise ValueError("Game already has 10 frames")
        self.pins.append(pins)

    def score(self):
        if self.pins == []:
            raise ValueError("Unstarted game cannot be scored")
        time_2 = 0
        frame_2 = 0
        for index, throw in enumerate(self.pins):
            if throw == 10:
                self.points += sum(self.pins[index:index+3])
                frame_2 += 1
            if time_2 == 0 and throw != 10:
                self.points += throw
                time_2 += 1
                continue
            if time_2 == 1:
                if throw + self.pins[index - 1] == 10:
                    self.points += sum(self.pins[index:index+2])
                elif throw + self.pins[index - 1] < 10:
                    self.points += throw
                time_2 = 0
                frame_2 += 1
            if frame_2 == 10:
                if throw == 10 and (len(self.pins) - index != 3):
                    raise ValueError("Cannot calculate score before the bonus rows")
                if sum(self.pins[index-1:index+1]) == 10 and (index + 1 == len(self.pins)):
                    raise ValueError("Cannot calculate score before the bonus rows")
                break
        if frame_2 < 10:
            raise ValueError("Incomplete game cannot be scored")
        return self.points