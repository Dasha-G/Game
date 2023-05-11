import pygame
from pygame import *



class ExitGate(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super(ExitGate, self).__init__()
		
		self.gate_open = pygame.image.load('pictures/strelk.png')
		self.image = pygame.image.load('pictures/strelk.png')
        #self.image2 = pygame.image.load('pictures/strelk2.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = self.image.get_width()
		self.height = self.image.get_height()

	def update(self, player):
		if hero.rect.colliderect(self.rect.x , self.rect.y, self.width, self.height):
			self.image = self.gate_open
            #self.image2 = self.gate_open

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed=player_x_speed
        self.y_speed=player_y_speed

    def fire(self):
        bullet=Bullet('kknife.png',self.rect.centerx,self.rect.top,15,20,15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed, start_x1, start_x2): 
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)        
        self.speed=player_speed
        self.start_x1=start_x1
        self.start_x2=start_x2
        
    def update(self):
        if self.rect.x <= self.start_x1: 
            self.side='right'
        if self.rect.x >= win_width - self.start_x2: 
            self.side='left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        


class Button(pygame.sprite.Sprite):
	def __init__(self, img, scale, x, y):
		super(Button, self).__init__()

		self.image = pygame.transform.scale(img, scale)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.clicked = False

	def draw(self, win):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] and not self.clicked:
				action = True
				self.clicked = True

			if not pygame.mouse.get_pressed()[0]:
				self.clicked = False

		win.blit(self.image, self.rect)
		return action

def menu():
    global back,clock,play,play_btn,exit,exit_btn,FPS

    back=transform.scale(image.load('fon/first_screen.jpg'), (1000, 700))
    clock = pygame.time.Clock()
    FPS = 30

    play= pygame.image.load('pictures/sttart.png')
    exit = pygame.image.load('pictures/exit.png')

    play_btn = Button(play, (128, 64), 430, 400)
    exit_btn  = Button(exit, (45,42), 950, 10)
win_width=1000
win_height=650
win = display.set_mode((win_width,win_height))