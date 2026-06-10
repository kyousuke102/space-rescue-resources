import pygame
import importlib
from GameFrame import Globals

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pygame.font.init()
pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for joystick in joysticks:
    joystick.init()

pygame.display.set_caption(Globals.window_name)
window_size = (Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT)
screen = pygame.display.set_mode(window_size,
                                  pygame.DOUBLEBUF, 32)

Globals.next_level = Globals.start_level
levels = Globals.levels

while Globals.running:
    curr_level = Globals.next_level
    mod_name = f"Rooms.{levels[curr_level]}"
    mod = importlib.import_module(mod_name)
    importlib.reload(mod)
    class_name = getattr(mod, levels[curr_level])
    room = class_name(screen, joysticks)
    Globals.next_level = curr_level + 1
    if Globals.next_level >= len(levels):
        Globals.next_level = 0
    exit_val = room.run()

    if exit_val is True or Globals.running is False:
        break

pygame.quit()