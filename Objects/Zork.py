from GameFrame import RoomObject, Globals
from Objects.Asteroid import Asteroid
from Objects.Astronaut import Astronaut
import random

class Zork(RoomObject):
    def __init__(self, room, x, y, health=10, speed=10, asteroid_rate=(5, 50)):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Zork.png")
        self.set_image(image, 135, 165)
        self.y_speed = random.choice([-speed, speed])
        self.health = health
        self.asteroid_rate = asteroid_rate
        self.register_collision_object("Laser")
        asteroid_spawn_time = random.randint(*asteroid_rate)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)

    def keep_in_room(self):
        if self.y < 0 or self.y > Globals.SCREEN_HEIGHT - self.height:
            self.y_speed *= -1

    def step(self):
        self.keep_in_room()

    def spawn_asteroid(self):
        new_asteroid = Asteroid(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_asteroid)
        asteroid_spawn_time = random.randint(*self.asteroid_rate)
        self.set_timer(asteroid_spawn_time, self.spawn_asteroid)

    def spawn_astronaut(self):
        new_astronaut = Astronaut(self.room, self.x, self.y + self.height/2)
        self.room.add_room_object(new_astronaut)
        astronaut_spawn_time = random.randint(30, 200)
        self.set_timer(astronaut_spawn_time, self.spawn_astronaut)

    def handle_collision(self, other, other_type):
        if other_type == "Laser":
            self.room.delete_object(other)
            self.health -= 1
            if self.health <= 0:
                self.room.delete_object(self)
                self.room.score.update_score(5000)
                if Globals.next_level == 2:
                    self.room.running = False
                else:
                    Globals.next_level = 4
                    self.room.running = False