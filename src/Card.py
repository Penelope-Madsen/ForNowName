import pygame
# import mouse
size = width, height = 440, 500
screen = pygame.display.set_mode(size)
pygame.init()

class Card:
    def __init__(self, color, text, font):
        self.color = color
        self.text = text
        self.font = font

    card = pygame.Rect(width / 2, height / 2 + 100, 320, 320)
    card.center = (width / 2, height / 2 + 40)

    def create(self):
        for i, msg in enumerate(self.text):
            state = self.font.render(msg, True, self.color)
            stateRect = state.get_rect()
            stateRect.center = (width / 2, height / 2 - 50 + 30 * i)
            screen.blit(state, stateRect)

    # def left(self):
    #     mouse.get_position()
    #     position = mouse.position()
    #     if mouse.click and position < 100:

