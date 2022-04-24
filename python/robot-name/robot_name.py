import random
import string

alphabet = string.ascii_uppercase
robot_names = set()

class Robot:
    def __init__(self):
        self.reset()

    def create_name(self):
        self.test_name = "".join(random.sample(alphabet, 2)) + str(random.randint(100, 999))
        if self.test_name in robot_names:
            self.test_name = self.create_name()
        return self.test_name

    def reset(self):
        self.name = self.create_name()
        robot_names.add(self.name)