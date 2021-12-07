import pygame
import random
#set Caption
pygame.init()
screen = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Realm Soul")
icon = pygame.image.load('icon12.png')
pygame.display.set_icon(icon)
#background 
bg = pygame.image.load("123.jpg")
pygame.display.set_caption('Battle')
sword_img = pygame.image.load('sword.png')  
#define game variables
current_fighter = 1
total_fighters = 2
action_cooldown = 0
action_wait_time = 90
attack = False
clicked = False
#bg
def draw_bg():
    screen.blit(bg,(0,0))
#panel
panel = pygame.image.load("bg5.png")
def draw_panel():
    screen.blit(panel,(0,1200-700))
#Healbar color
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
        self.action = 0
    def attack(self, target):
        #deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        if target.hp < 1:
            target.hp = 0
            target.alive = False
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
#ประกาศใช้
knight = fighter(300,420, 'knight',30,10,"Ghost1.gif")
bandit1 = fighter(700,460, 'bandit',20,6,"soul2.png")
bandit_list =[]
bandit_list.append(bandit1)
knight_healt_bar = healbar(200,1200-700+40,knight.hp, knight.max_hp)
bandit1_health_bar = healbar(650, 1200 - 700 + 40, bandit1.hp, bandit1.max_hp)
run = True
while run:
    draw_bg()
    draw_panel()
    knight.draw()
    for bandit in bandit_list:
        bandit1.draw()
    knight_healt_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    #action
    attack = False
    potion = False
    target = None
    #mouse
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for count, bandit in enumerate(bandit_list):
         if bandit1.rect.collidepoint(pos):
            #hide mouse
            pygame.mouse.set_visible(False)
            #show sword in place of mouse cursor
            screen.blit(sword_img, pos)
            if clicked == True:
                attack = True
                target = bandit_list[count]
    #player action
            if knight.alive == True:
                if current_fighter == 1:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                    #attack
                        if attack == True and target != None:
                            bandit1.attack(target)
                            current_fighter += 1
                            action_cooldown = 0
    #enemy action
    for count, bandit in enumerate(bandit_list):
        if current_fighter == 2 + count:
            if bandit1.alive == True:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #attack
                    bandit1.attack(knight)
                    current_fighter += 1
                    action_cooldown = 0
            else:
                current_fighter += 1
    if current_fighter > total_fighters:
        current_fighter = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False
    pygame.display.update()