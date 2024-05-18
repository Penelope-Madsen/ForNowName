import pygame
from Player import p1
size = width, height = 470, 530
screen = pygame.display.set_mode(size)
pygame.init()
white = (255, 255, 255)
black = 0, 0, 0
blue = 12, 11, 43
background = 69, 73, 87
yellow = 247, 246, 200
green = 74, 112, 100
font2 = pygame.font.Font('freesansbold.ttf', 18)


def printtext(sample):
    text = sample.split()
    i = 0
    x = 1
    sentence = ''
    for word in text:
        if i < 5:
            sentence += word + " "
            i += 1
        else:
            choice = font2.render(sentence, True, yellow)
            choicerect = choice.get_rect()
            choicerect.center = (width / 2, height / 2 + 20 * x)
            screen.blit(choice, choicerect)
            sentence = word + " "
            i = 0
            x += 1
    choice = font2.render(sentence, True, yellow)
    choicerect = choice.get_rect()
    choicerect.center = (width / 2, height / 2 + 20 * x)
    screen.blit(choice, choicerect)


class Card:
    def __init__(self, tcolor, toptext, ctext, font, bcolor, lcrew, lcargo, lfuel, llaw, rcrew, rcargo, rfuel, rlaw,
                 left, right, lnext, rnext):
        self.tcolor = tcolor
        self.toptext = toptext
        self.ctext = ctext
        # self.design = design
        self.font = font
        self.bcolor = bcolor
        self.lcrew = lcrew
        self.lcargo = lcargo
        self.lfuel = lfuel
        self.llaw = llaw
        self.rcrew = rcrew
        self.rcargo = rcargo
        self.rfuel = rfuel
        self.rlaw = rlaw
        self.left = left
        self.right = right
        self.rect = pygame.Rect(width/2, height/2, 320, 320)
        self.rect.center = (width / 2, height / 2 + 70)
        self.lnext = lnext
        self.rnext = rnext

    def create(self):
        # card = pygame.Rect(width/2, height/2, 320, 320)
        # card.center = (width/2, height/2 + 70)
        # 65 is the height of the top bar, 265 is height/2, 175 top of the card
        back = pygame.Rect(width/2, 120, width, 110)
        back.center = (width/2, 120)
        pygame.draw.rect(screen, background, back, 0, 0)
        pygame.draw.rect(screen, self.bcolor, self.rect, 0, 30)
        # for i, msg in enumerate(self.toptext):
        #     state = self.font.render(msg, True, self.tcolor)
        #     staterect = state.get_rect()
        #     staterect.center = (width / 2, height / 2 - 175 + 20 * i)
        #     screen.blit(state, staterect)
        text = self.toptext.split()
        i = 0
        x = 1
        sentence = ''
        for word in text:
            if i < 5:
                sentence += word + " "
                i += 1
            else:
                choice = font2.render(sentence, True, self.tcolor)
                choicerect = choice.get_rect()
                choicerect.center = (width / 2, height / 2 - 190 + 20 * x)
                screen.blit(choice, choicerect)
                sentence = word + " "
                i = 0
                x += 1
        choice = font2.render(sentence, True, self.tcolor)
        choicerect = choice.get_rect()
        choicerect.center = (width / 2, height / 2 - 190 + 20 * x)
        screen.blit(choice, choicerect)
        for i, msg in enumerate(self.ctext):
            state = self.font.render(msg, True, self.tcolor)
            staterect = state.get_rect()
            staterect.center = (width / 2, height / 2 - 50 + 20 * i)
            screen.blit(state, staterect)

    def hover(self, xpos, ypos):
        if 20 < xpos < 100 and 165 < ypos < 490:
            printtext(self.left)
            pygame.draw.lines(screen, black, False, [(40, 310), (30, 320), (40, 330)], 2)
        elif 370 < xpos < 450 and 165 < ypos < 490:
            printtext(self.right)
            pygame.draw.lines(screen, black, False, [(430, 310), (440, 320), (430, 330)], 2)
        else:
            pygame.draw.rect(screen, self.bcolor, self.rect, 0, 30)
            pygame.draw.rect(screen, background, (25, 305, 20, 40), 0)
            pygame.draw.rect(screen, background, (425, 305, 20, 40), 0)
            for i, msg in enumerate(self.ctext):
                state = self.font.render(msg, True, self.tcolor)
                staterect = state.get_rect()
                staterect.center = (width / 2, height / 2 - 50 + 20 * i)
                screen.blit(state, staterect)

    def choose(self, xpos, ypos):
        pygame.event.get()
        # effects: update levels, others
        # if 20 < xpos < 100 and 165 < ypos < 490 and pygame.mouse.get_pressed():
        if 20 < xpos < 100 and 165 < ypos < 490:
            p1.cargo += self.lcargo
            p1.crew += self.lcrew
            p1.fuel += self.lfuel
            p1.law += self.llaw
            if p1.crew < 45:
                pygame.draw.rect(screen, blue, pygame.Rect(100, 8, 18, 45))
                pygame.draw.rect(screen, green, pygame.Rect(100, 8, 18, p1.crew))
                pygame.draw.rect(screen, blue, pygame.Rect(100, 8, 18, 45), 1)
            if p1.fuel < 45:
                pygame.draw.rect(screen, blue, pygame.Rect(210, 8, 18, 45))
                pygame.draw.rect(screen, green, pygame.Rect(210, 8, 18, p1.fuel))
                pygame.draw.rect(screen, blue, pygame.Rect(210, 8, 18, 45), 1)
            if p1.cargo < 45:
                pygame.draw.rect(screen, blue, pygame.Rect(310, 8, 18, 45))
                pygame.draw.rect(screen, green, pygame.Rect(310, 8, 18, p1.cargo))
                pygame.draw.rect(screen, blue, pygame.Rect(310, 8, 18, 45), 1)
            if p1.law < 45:
                pygame.draw.rect(screen, blue, pygame.Rect(410, 8, 18, 45))
                pygame.draw.rect(screen, green, pygame.Rect(410, 8, 18, p1.law))
                pygame.draw.rect(screen, blue, pygame.Rect(410, 8, 18, 45), 1)
            p1.nextCard = self.lnext

        elif 370 < xpos < 450 and 165 < ypos < 490:
            p1.cargo += self.rcargo
            p1.crew += self.rcrew
            p1.fuel += self.rfuel
            p1.law += self.rlaw
            if p1.crew < 45:
                pygame.draw.rect(screen, blue, pygame.Rect(100, 8, 18, 45))
                pygame.draw.rect(screen, green, pygame.Rect(100, 8, 18, p1.crew))
                pygame.draw.rect(screen, blue, pygame.Rect(100, 8, 18, 45), 1)
            if p1.fuel < 45:
                pygame.draw.rect(screen, blue, pygame.Rect(210, 8, 18, 45))
                pygame.draw.rect(screen, green, pygame.Rect(210, 8, 18, p1.fuel))
                pygame.draw.rect(screen, blue, pygame.Rect(210, 8, 18, 45), 1)
            if p1.cargo < 45:
                pygame.draw.rect(screen, blue, pygame.Rect(310, 8, 18, 45))
                pygame.draw.rect(screen, green, pygame.Rect(310, 8, 18, p1.cargo))
                pygame.draw.rect(screen, blue, pygame.Rect(310, 8, 18, 45), 1)
            if p1.law < 45:
                pygame.draw.rect(screen, blue, pygame.Rect(410, 8, 18, 45))
                pygame.draw.rect(screen, green, pygame.Rect(410, 8, 18, p1.law))
                pygame.draw.rect(screen, blue, pygame.Rect(410, 8, 18, 45), 1)
        # new card
            p1.nextCard = self.rnext
