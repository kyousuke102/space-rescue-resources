from GameFrame import Level, Globals, TextObject
import pygame

class TitleText(TextObject):
    def __init__(self, room, x, y):
        TextObject.__init__(self, room, x, y, "LOSER!")
        self.size = 100
        self.font = 'Arial Black'
        self.colour = (255, 0, 0)
        self.bold = True
        self.update_text()

class ScoreText(TextObject):
    def __init__(self, room, x, y):
        TextObject.__init__(self, room, x, y, f"Final Score: {Globals.SCORE}")
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255, 255, 255)
        self.bold = False
        self.update_text()

class RestartText(TextObject):
    def __init__(self, room, x, y):
        TextObject.__init__(self, room, x, y, "Press R to restart")
        self.size = 40
        self.font = 'Arial Black'
        self.colour = (255, 255, 255)
        self.bold = False
        self.update_text()

class GameOver(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        self.set_background_image("Background.png")
        self.add_room_object(TitleText(self, Globals.SCREEN_WIDTH/2 - 200, Globals.SCREEN_HEIGHT/2 - 100))
        self.add_room_object(ScoreText(self, Globals.SCREEN_WIDTH/2 - 200, Globals.SCREEN_HEIGHT/2 + 50))
        self.add_room_object(RestartText(self, Globals.SCREEN_WIDTH/2 - 200, Globals.SCREEN_HEIGHT/2 + 150))

    def catch_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    Globals.next_level = 1
                    Globals.SCORE = 0
                    Globals.LIVES = 3
                    self.running = False