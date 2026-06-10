from GameFrame import TextObject, Globals, RoomObject

class Score(TextObject):
    def __init__(self, room, x: int, y: int, text=None):
        TextObject.__init__(self, room, x, y, text)
        self.size = 60
        self.font = 'Arial Black'
        self.colour = (255,255,255)
        self.bold = False
        self.update_text()

    def update_score(self, change):
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()

class Lives(RoomObject):
    def __init__(self, room, x: int, y: int):
        RoomObject.__init__(self, room, x, y)
        self.lives_icon = []
        for index in range(6):
            self.lives_icon.append(self.load_image(f"Lives_frames/Lives_{index}.png"))
        self.update_image()

    def update_image(self):
        self.set_image(self.lives_icon[Globals.LIVES], 125, 23)

        Globals.next_level = 3
        