import pygame
# import mouse
size = width, height = 470, 530
screen = pygame.display.set_mode(size)
pygame.init()
white = (255, 255, 255)
vis = False

class Card:
    def __init__(self, tcolor, text, font, bcolor, crewe, cargoe, fuele, lawe, left, right):
        self.tcolor = tcolor
        self.text = text
        self.font = font
        self.bcolor = bcolor
        self.crewe = crewe
        self.cargoe = cargoe
        self.fuele = fuele
        self.lawe = lawe
        self.left = left
        self.right = right

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
        if 20 < xpos < 100 and 165 < ypos < 490:
            choice = self.font.render(self.left, True, white)
            # choiceRect = choice.get_rect()
            # choiceRect.center = (width/2, height/2 + 70)
            screen.blit(choice, (width/2-len(self.left)*7, height/2))
            pygame.display.flip()
        elif 370 < xpos < 450 and 165 < ypos < 490:
            choice = self.font.render(self.right, True, white)
            # choiceRect = choice.get_rect()
            # choiceRect.center = (width/2, height/2 + 70)
            screen.blit(choice, (width / 2 + len(self.right)*2, height / 2))
            pygame.display.flip()

    # def choose(self, xpos, ypos):
    #     if 20 < xpos < 100 and 165 < ypos < 490 and pygame.MOUSEBUTTONDOWN:
    #         # effects: update levels, others
    #         # new card
    #         cargo += self.cargoe

