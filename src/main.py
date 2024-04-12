import sys
import pygame
import random
from Card import Card

pygame.init()

size = width, height = 440, 500
blue = 12, 11, 43
white = (255, 255, 255)
background = 69, 73, 87
star = pygame.image.load("Star.png")
sparkle = pygame.image.load("Sparkle.png")
screen = pygame.display.set_mode(size)
screen.fill(blue)

pygame.display.set_caption('StarGazers')
font1 = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 20)

title = font1.render('Welcome to Star Gazers!', True, white)
titleRect = title.get_rect()
titleRect.center = (width/2, height/2-100)
sub = font2.render('Click to begin', True, white)
subRect = sub.get_rect()
subRect.center = (width/2, height/2)

card = pygame.Rect(width/2, height/2+100, 320, 320)
card.center = (width/2, height/2+40)

welcomeMessage = [
    "Congratulations, Captain!",
    "You’ve been in the ship trade",
    "business for years",
    "and at long last you’ve been",
    "promoted high enough to",
    "have your own ship.",
    "Do you feel ready?"]

welc = Card(white, welcomeMessage, font2)

for x in range(40):
    screen.blit(star, (random.randint(0, 380),random.randint(0, 410)))
    x+=1
for x in range(15):
    screen.blit(sparkle, (random.randint(0, 380),random.randint(0, 410)))
    x+=1
screen.blit(title, titleRect)
screen.blit(sub, subRect)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(background)
            pygame.draw.rect(screen, blue, card, 0, 30)
            welc.create()

    pygame.display.flip()
