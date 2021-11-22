import os
import sys
import pygame as pg
import textadventure.app as app
import textadventure.constants as constants


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(constants.CAPTION)
    pg.display.set_mode(constants.SCREEN_SIZE)
    app.App().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
