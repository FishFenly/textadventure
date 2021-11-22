import pygame as pg
import textadventure.constants as constants

class UI:
    """
    functions to draw the game UI
    """
    def __init__(self):
        self.border_width = 5
        self.white = pg.Color("white")
        self.red = pg.Color("red")
        
    def draw_border(self, surface):
        top = pg.Rect(0, 0, constants.SCREEN_SIZE[0], self.border_width)
        left = pg.Rect(0, 0, self.border_width, constants.SCREEN_SIZE[1])
        bottom = pg.Rect(0, constants.SCREEN_SIZE[1] - self.border_width,
                constants.SCREEN_SIZE[0], self.border_width)
        right = pg.Rect(constants.SCREEN_SIZE[0] - self.border_width, 0,
                self.border_width, constants.SCREEN_SIZE[1])
        
        pg.draw.rect(surface, self.white, top, 0)
        pg.draw.rect(surface, self.white, left, 0)
        pg.draw.rect(surface, self.white, bottom, 0)
        pg.draw.rect(surface, self.white, right, 0)

    def draw_console_border(self, surface):
        top = pg.Rect(0, constants.SCREEN_SIZE[1] / 1.75, 
                constants.SCREEN_SIZE[0], self.border_width)
        pg.draw.rect(surface, self.red, top, 0)

class InputBox:
    """
    functions to draw input UI box elements and handle input
    """
    def __init__(self):
        self.border_width = 5
        self.console_size = 40
        self.console_prompt_size = constants.FONT_SIZE
        self.font = pg.font.Font(constants.FONT, constants.FONT_SIZE)
        self.white = pg.Color("white")
        self.red = pg.Color("red")
        self.input_box = pg.Rect(self.border_width + self.console_prompt_size, 
                constants.SCREEN_SIZE[1] - (self.border_width + self.console_size),
                constants.SCREEN_SIZE[0] - (self.border_width * 2 + self.console_prompt_size),
                self.console_size)
        
    def draw_input_box(self, surface):
        pg.draw.rect(surface, self.red, self.input_box)

        text = self.font.render(">", 1, self.white)
        text_position = pg.Rect(self.border_width * 2,
                constants.SCREEN_SIZE[1] - (self.border_width + self.console_prompt_size),
                self.console_prompt_size,
                self.console_prompt_size)
        surface.blit(text, text_position)    
