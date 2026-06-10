from GameFrame import RoomObject, Globals
import random

class Asteroid(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("asteroid.png")
        size = random.randint(20, 80)
        self.set_image(image, size, size)
        angle = random.randint(135, 225)
        self.set_direction(angle, 10)
        self.register_collision_object("Ship")

    def step(self):
        self.keep_in_room()
        self.outside_of_room()

    def keep_in_room(self):
        if self.y < 0:
            self.y = 0
            self.y_speed *= -1
        elif self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y = Globals.SCREEN_HEIGHT - self.height
            self.y_speed *= -1

    def outside_of_room(self):
        if self.x + self.width < 0:
            self.room.delete_object(self)

    def handle_collision(self, other, other_type):
        if other_type == "Ship":
            self.room.delete_object(self)
            Globals.LIVES -= 1
            if Globals.LIVES > 0:
                self.room.lives.update_image()
            else:
                Globals.won = False
                Globals.next_level = 3
                self.room.running = False