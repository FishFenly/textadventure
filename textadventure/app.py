import pygame as pg
import pygame_textinput as pgi

import textadventure.ui as ui
import textadventure.constants as constants


class App():
    """
    Handle game loop, event loop and overall program flow.
    """
    def __init__(self):
        pg.key.set_repeat(200, 25)
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.keys = pg.key.get_pressed()
        self.ui = ui.UI()
        self.input_box = ui.InputBox()
        self.font = pg.font.Font(constants.FONT, constants.FONT_SIZE)
        self.manager = pgi.TextInputManager(validator = lambda input: len(input) <= 5)
        self.input_handler = pgi.TextInputVisualizer(
                manager=self.manager, font_object = self.font)
        self.input_handler.font_color = pg.Color("white")

    def event_loop(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                self.done = True
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pass
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
                pass
            elif event.type in (pg.KEYUP, pg.KEYDOWN):
                self.keys = pg.key.get_pressed()
                print({self.input_handler.value})
                print(self.input_handler.surface)
       
        self.input_handler.update(events)
    
    def draw(self):
        self.screen.fill(pg.Color("black"))
        self.ui.draw_border(self.screen)
        self.ui.draw_console_border(self.screen)
        self.input_box.draw_input_box(self.screen)
        pg.display.update()
        self.screen.blit(self.input_handler.surface, (100, 100))

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.draw()
            self.clock.tick(self.fps)
