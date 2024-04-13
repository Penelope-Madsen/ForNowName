import sys
import pygame
import random
from Card import Card

pygame.init()

size = width, height = 470, 530
blue = 12, 11, 43
white = (255, 255, 255)
green = 74, 112, 100
background = 69, 73, 87
star = pygame.image.load("Star.png")
sparkle = pygame.image.load("Sparkle.png")
csym = pygame.image.load("crew.drawio.png")
DEFAULT_IMAGE_SIZE = (40, 30)
csym = pygame.transform.scale(csym, DEFAULT_IMAGE_SIZE)
screen = pygame.display.set_mode(size)
screen.fill(blue)

pygame.display.set_caption('StarGazers')
font1 = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 18)
font3 = pygame.font.Font('freesansbold.ttf', 20)

# controls neg space of stats - inverse
moral = 20
fuel = 20
cargo = 20

title = font1.render('Welcome to Star Gazers!', True, white)
titleRect = title.get_rect()
titleRect.center = (width/2, height/2-100)
sub = font3.render('Click to begin', True, white)
subRect = sub.get_rect()
subRect.center = (width/2, height/2)
ships = ["the Andromeda", "the Argo", "Starbuster"]
welcomeMessage = [
    "Congratulations, Captain!",
    "After working in space shipping for years,",
    "at long last you’ve been promoted high",
    "enough to have your own ship.",
    "",
    "",
    "Welcome to " + ships[random.randint(0, len(ships)-1)]]


welc = Card(white, welcomeMessage, font2, blue)

for x in range(40):
    screen.blit(star, (random.randint(0, width),random.randint(0, height)))
    x+=1
for x in range(15):
    screen.blit(sparkle, (random.randint(0, width),random.randint(0, height)))
    x+=1
screen.blit(title, titleRect)
screen.blit(sub, subRect)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill(background)
            pygame.draw.rect(screen, green, pygame.Rect(0, 0, width, 65))
            screen.blit(csym, (70, 14))
            pygame.draw.rect(screen, blue, pygame.Rect(125, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(125, 8, 18, moral))
            pygame.draw.rect(screen, blue, pygame.Rect(125, 8, 18, 45), 1)
            pygame.draw.rect(screen, blue, pygame.Rect(245, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(245, 8, 18, fuel))
            pygame.draw.rect(screen, blue, pygame.Rect(245, 8, 18, 45), 1)
            pygame.draw.rect(screen, blue, pygame.Rect(365, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(365, 8, 18, cargo))
            pygame.draw.rect(screen, blue, pygame.Rect(365, 8, 18, 45), 1)
            welc.create()

    pygame.display.flip()
