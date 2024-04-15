import pygame
# import mouse
size = width, height = 470, 530
screen = pygame.display.set_mode(size)
pygame.init()

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

    def hover(self):
        if

    # def left(self):
    #     mouse.get_position()
    #     position = mouse.position()
    #     if mouse.click and position < 100:

