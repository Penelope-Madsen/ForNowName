import pygame
on = True


class Action:
    def __init__(self, which):
        self.which = which

    def happen(self, xpos, ypos):
        while self.which.on:
            self.which.create()
            self.which.hover(xpos, ypos)
            if pygame.MOUSEBUTTONDOWN:
                self.which.choose(xpos, ypos)
                # self.which.on = False
