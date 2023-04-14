import pygame, sys
from pygame.locals import *
import random, time
 
#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
 
#our fonts 
myfont = pygame.font.SysFont(None, 30)
font_small = pygame.font.SysFont("Verdana", 20)


#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINSPEED = 5
COINS = 0


#background
background = pygame.image.load("images\AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)    
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images\coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        global COINS
        self.rect.move_ip(0,COINSPEED)
        if (self.rect.bottom > 600): # if our coin will go under the screen it will be respawned
            #COINS += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(7, 0)
                  

 
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
Co = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(Co)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(Co)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.2
           
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, GREEN)
    DISPLAYSURF.blit(scores, (75,7))
    coin = font_small.render(str(COINS), True, GREEN)
    DISPLAYSURF.blit(coin, (360,7))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("sounds\crash.wav").play()
        time.sleep(0.5)
        
        DISPLAYSURF.fill(RED)
        text = myfont.render('GAME OVER', True, BLACK)
        DISPLAYSURF.blit(text, (10, 50))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()   
    
    if pygame.sprite.spritecollideany(P1, coins):
            COINS += 1
            for coin in coins:
                coin.kill()
        #   time.sleep(1)
            pygame.display.update() 
    if(len(coins) == 0): # if our coin was collected:
        COIN = Coin()   # new coin object will be created and added to the coins group
        coins.add(COIN)
        all_sprites.add(COIN)     
    
    text = myfont.render('Score: ', True, "RED")
    DISPLAYSURF.blit(text, (10, 10)) 
    text1 = myfont.render('Coins: ', True, "RED") 
    DISPLAYSURF.blit(text1, (295, 10))   
    pygame.display.update()
    FramePerSec.tick(FPS)
    