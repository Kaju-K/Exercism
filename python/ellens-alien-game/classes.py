class Alien:
    total_aliens_created = 0
    health = 3
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1
    def hit(self):
        self.health -= 1
        return self.health
    def is_alive(self):
        return self.health > 0
    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate += x_coordinate
        self.y_coordinate += y_coordinate
    def collision_detection(self, other_alien):
        pass



def new_aliens_collection(positions):
   return [Alien(aliens[0], aliens[1]) for aliens in positions]
