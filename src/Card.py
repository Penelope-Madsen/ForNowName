import pygame
# import mouse
size = width, height = 470, 530
screen = pygame.display.set_mode(size)
pygame.init()
white = (255, 255, 255)
vis = False

class Card:
    def __init__(self, tcolor, text, font, bcolor, crewe, cargoe, fuele, lawe):
        self.tcolor = tcolor
        self.text = text
        self.font = font
        self.bcolor = bcolor
        self.crewe = crewe
        self.cargoe = cargoe
        self.fuele = fuele
        self.lawe = lawe

    # card = pygame.Rect(0, height / 2 - 200, 320, 320)
    # card.center = (width / 2, height / 2)

    def create(self):
        card = pygame.Rect(width/2, height/2, 320, 320)
        card.center = (width/2, height/2 + 70)
        pygame.draw.rect(screen, self.bcolor, card, 0, 30)
        for i, msg in enumerate(self.text):
            state = self.font.render(msg, True, self.tcolor)
            stateRect = state.get_rect()
            stateRect.center = (width / 2, height / 2 - 175 + 20 * i)
            screen.blit(state, stateRect)

    def hover(self, xpos, ypos):
        result = self.font.render(str(self.crewe), True, white)
        resultRect = result.get_rect()
        resultRect.center = (60, 200)
        while 20 < xpos < 100 and 165 < ypos < 490:
            screen.blit(result, resultRect)

    # def left(self):
    #     mouse.get_position()
    #     position = mouse.position()
    #     if mouse.click and position < 100:

