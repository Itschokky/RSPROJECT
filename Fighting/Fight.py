import pygame
from pygame.constants import K_RIGHT
from pygame.image import load
#set Caption
pygame.init()
screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Realm Soul")
icon = pygame.image.load('icon12.png')
pygame.display.set_icon(icon)
#background 
bg = pygame.image.load("bg.png")
def draw_bg():
    screen.blit(bg,(0,0))
panel = pygame.image.load("bg5.png")
def draw_panel():
    screen.blit(panel,(0,1200-700))
red = (255, 0, 0)
green = (0, 255, 0)
#player
load_player = pygame.image.load("soul1.png")
player = pygame.transform.scale(load_player,(100,100))
#In fight
class fighter():
    def __init__(self,x,y,name,max_hp,strength,img):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        img = pygame.image.load(img)
        self.image = pygame.transform.scale(img,(150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def draw(self):
        screen.blit(self.image, self.rect)
class healbar():    
    def __init__(self, x ,y, hp, max_hp):
        self.x = x
        self.y = y 
        self.hp = hp
        self.max_hp = max_hp
    def draw(self, hp):
        #update with new health
        self.hp = hp
        #calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))

knight = fighter(300,420, 'knight',30,10,3,"Ghost1.gif")
bandit1 = fighter(700,460, 'bandit',20,6,1,"soul2.png")
bandit2 = fighter(900,460, 'bandit',20,6,1,"soul2.png")
bandit_list =[]
bandit_list.append(bandit1)
bandit_list.append(bandit2)
knight_healt_bar = healbar(200,1200-700+40,knight.hp, knight.max_hp)
bandit1_health_bar = healbar(650, 1200 - 700 + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = healbar(900, 1200 - 700 + 40, bandit2.hp, bandit2.max_hp)
run = True
while run:
    draw_bg()
    draw_panel()
    knight.draw()
    for bandit in bandit_list:
        bandit.draw()
    knight_healt_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)
    pygame.time.delay(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()