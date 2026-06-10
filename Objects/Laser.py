from GameFrame import RoomObject, Globals

class Laser(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Laser.png")
        self.set_image(image, 33, 9)
        self.set_direction(0, 20)
        self.register_collision_object("Asteroid")
        self.register_collision_object("Astronaut")
        self.register_collision_object("Zork")

    def step(self):
        self.outside_of_room()

    def outside_of_room(self):
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)

    def handle_collision(self, other, other_type):
        if other_type == "Asteroid":
            self.room.delete_object(other)
            self.room.score.update_score(500)
        elif other_type == "Astronaut":
            self.room.delete_object(other)
            self.room.score.update_score(-100)