# Globals for the directions
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.x_coordinate = x_pos
        self.y_coordinate = y_pos
        self.direction = direction
        self.coordinates = (self.x_coordinate, self.y_coordinate)
    def move(self, movement):
        for letter in movement:
            if letter == "A":
                self.x_coordinate += self.direction[0]
                self.y_coordinate += self.direction[1]

            #in linear algebra, if we want to rotate a vector, we use the rotation matrix, given by:
            #R = [[cos(theta), -sen(theta)], [sen(theta), cos(theta)]]; where theta is the angle of rotation in the counter clockwise
            #so if we want to move to the right, we are rotating -90º:
            #R_r = [[0, 1], [-1, 0]]
            #new_direction_to_the_right = R_r * direction
            #new_direction_to_the_right = [[0, 1], [-1, 0]] * [x, y]
            #new_direction_to_the_right = [y, -x]
            #the same thought is made if we are rotation to the left, but instead we use 90º:
            #R_l = [[0, 1], [-1, 0]]
            #new_direction_to_the_left = R_l * direction = [-y, x]

            if letter == "R":
                self.direction = (self.direction[1], -self.direction[0])
            if letter == "L":
                self.direction = (-self.direction[1], self.direction[0])
            self.coordinates = (self.x_coordinate, self.y_coordinate)
