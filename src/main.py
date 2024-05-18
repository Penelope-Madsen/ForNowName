import sys
import pygame
import random
from Card import Card
from Player import p1

pygame.init()

start = True
size = width, height = 470, 530
blue = 12, 11, 43
white = (255, 255, 255)
green = 74, 112, 100
background = 69, 73, 87
position = (0, 0)
star = pygame.image.load("Star.png")
sparkle = pygame.image.load("Sparkle.png")
crew = pygame.image.load("crew.drawio.png")
DEFAULT_IMAGE_SIZE = (40, 30)
crew = pygame.transform.scale(crew, DEFAULT_IMAGE_SIZE)
fuelsym = pygame.image.load("fuel.png")
carsym = pygame.image.load("cargo.png")
badge = pygame.image.load("badge.png")
screen = pygame.display.set_mode(size)
screen.fill(blue)

pygame.display.set_caption('StarGazers')
font1 = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 18)
font3 = pygame.font.Font('freesansbold.ttf', 20)

title = font1.render('Welcome to Star Gazers!', True, white)
titleRect = title.get_rect()
titleRect.center = (width / 2, height / 2 - 100)
sub = font3.render('Click to begin', True, white)
subRect = sub.get_rect()
subRect.center = (width / 2, height / 2)

welcomeMessage = ("Congratulations, Captain! After working in space shipping for years at long last you’ve been promoted "
                  "high enough to have your own ship.")
welcomeMessage2 = ["Welcome to ..",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "",
                   "the " + p1.name]

# controls neg space of stats - inverse
moral = 20
fuel = 20
cargo = 20
lawful = 20


cards = {'card1': Card(white, "Will you take 50 crates from Livestock & Co for 20 star?", "", font2,
                       blue, 2, -5, -5, 0, -2, 5, 5, 0, "Fine",
                       "Sounds stinky", 'L&Co', 'stranger'),
         'stranger': Card(white, "Hey kid. Heard you're a captain now. Need someone to show you the ropes?", "", font2, blue, -10, 0, 0,
                       0, 2, 0, 0, 0, "My hero! I'd be honored", "Scram. I can run my own ship", 'card4',
                       'smuggle'),
         'welc': Card(white, welcomeMessage, welcomeMessage2, font2, blue, 0, 0, 0, 0, 0,
             0, 0, 0, "What am I doing here???", "I'm so ready", 'instru', 'card1'),
         'asteroid': Card(white, "5 asteroids are hurtling towards you", "", font2, blue, 0, 0, 0,
                0, 0, 0, 0, 0, "5 asteroids eh? That doesn't sound so bad",
                "Veer off course", 'card1', 'card4'),
         'card4': Card(white, "I brought along this giant clunky robot. Hope you don't mind", "", font2, blue, -5, 0,
                       -2, 0, 5, 0, 2, 0, "I do actually",
                       "Uhhhh", 'asteroid', 'asteroid'),
         'instru': Card(white, "Make important leadership decisions and don't let your controls get too high or too low", "", font2, blue, 0, 10,
                       0, 0, 0, 0, 0, 0, "What controls?",
                       "Let me at it!", 'instru2', 'card1'),
         'instru2': Card(white, "Far left is your crew moral, then there's trade, fuel, and your law abidingness", "", font2, blue, 0, 0,
                       0, 0, 0, 0, 0, 0, "I'm ready",
                       "I'll never understand", 'card1', 'card1'),
         'L&Co': Card(white, "Uh oh. You spent too long at a port and now won't deliver on time. "
                             "How fast are you wlling to go?", "", font2, blue, 0, 0, 5, 10, 0, 5, 0, -10, "As fast as I need to",
                       "The extremely lawful galactic speed limit", 'asteroid', 'asteroid'),
         'smuggle': Card(white, "Pssst .. hey. Will you smuggle these lizards to Neptune for me?", "", font2,
                       blue, 0, 2, 0, -10, 2, 0, 0, 10, "Hell no",
                       "How much?", 'L&Co', 'haggle'),
         'haggle': Card(white, "30 grand + 30 barrels of star?", "", font2,
                       blue, 0, -10, 0, 15, 0, 0, 0, 0, "Sure thing!",
                       "Try again", 'asteroid', 'haggle2'),
         'haggle2' : Card(white, "50 grand + 40 barrels of star?", "", font2,
                       blue, 0, 5, 2, -5, 0, -10, -7, 10, "Forget it",
                       "Shake on it", 'card1', 'asteroid'),
         }

for x in range(40):
    screen.blit(star, (random.randint(0, width), random.randint(0, height)))
    x += 1
for x in range(15):
    screen.blit(sparkle, (random.randint(0, width), random.randint(0, height)))
    x += 1
screen.blit(title, titleRect)
screen.blit(sub, subRect)


def action(which, xp, yp):
    which.create()
    which.hover(xp, yp)
    if event.type == pygame.MOUSEBUTTONDOWN and p1.up:
        p1.up = False
        which.choose(xp, yp)
    if event.type == pygame.MOUSEBUTTONUP:
        p1.up = True


while True:
    position = pygame.mouse.get_pos()
    xpos = position[0]
    ypos = position[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and start:
            screen.fill(background)
            pygame.draw.rect(screen, green, pygame.Rect(0, 0, width, 65))
            screen.blit(crew, (40, 14))
            pygame.draw.rect(screen, blue, pygame.Rect(100, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(100, 8, 18, p1.crew))
            pygame.draw.rect(screen, blue, pygame.Rect(100, 8, 18, 45), 1)
            screen.blit(carsym, (150, 14))
            pygame.draw.rect(screen, blue, pygame.Rect(210, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(210, 8, 18, p1.fuel))
            pygame.draw.rect(screen, blue, pygame.Rect(210, 8, 18, 45), 1)
            screen.blit(fuelsym, (250, 14))
            pygame.draw.rect(screen, blue, pygame.Rect(310, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(310, 8, 18, p1.cargo))
            pygame.draw.rect(screen, blue, pygame.Rect(310, 8, 18, 45), 1)
            screen.blit(badge, (350, 14))
            pygame.draw.rect(screen, blue, pygame.Rect(410, 8, 18, 45))
            pygame.draw.rect(screen, green, pygame.Rect(410, 8, 18, p1.law))
            pygame.draw.rect(screen, blue, pygame.Rect(410, 8, 18, 45), 1)
            start = False
    if not start:
        action(cards[p1.nextCard], xpos, ypos)

    pygame.display.flip()
