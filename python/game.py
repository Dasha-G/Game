import pygame
from pygame import *
init()

class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), [w, h])
        self.rect = self.image.get_rect()
        self.picture = picture
        self.w = w
        self.h = h
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.image, self.rect)

class Player(sprite.Sprite):
    def __init__(self, pictures, w, h, x, y, x_speed, y_speed, position):
        self.pictures = pictures
        self.image = transform.scale(image.load(pictures), [w, h])
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.w = w
        self.h = h
        self.position = position


    def update(self, barriers):
        if self.rect.x <= 1500-78 and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if self.rect.y <= 900-103 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.y_speed = 0              
                if p.rect.top - 100 < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
        
        self.x_speed = 0
        self.y_speed = 0

    def rect_x(self):
        return self.rect.x
    
    def rect_y(self):
        return self.rect.y
    def level_update(self, level):
        if level == 2:
            self.rect.y = 770
        if level == 1:
            self.rect.y = 20

    def draw(self):
        if self.position == 0:
            mw.blit(self.image,(self.rect.x,self.rect.y))
        elif self.position == 1:
            mw.blit(transform.flip(self.image,True,False),(self.rect.x,self.rect.y))
    def fire(self):
        bullet=Bullet('pictures/kknife.png',self.rect.centerx,self.rect.top,15,20,20)
        bullets.add(bullet)
    
class Colide(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        self.x_speed = 0
        self.y_speed = 0

class Bullet(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.speed=player_speed

    def update(self):
        self.rect.x +=self.speed
        if self.rect.x > 1500+10:
            self.kill()

class Button(GameSprite):
    def __init__(self, picture, w, h, x, y):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x = x
        self.y = y

    def colidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

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
        if self.rect.x >= 1500 - self.start_x2: 
            self.side='left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
   
'''class Enemy(Player):
    def __init__(self, pictures, w, h, x, y, x_speed, y_speed, position, move):
        Player.__init__(self, picture, w, h, x, y, x_speed, y_speed, position, move)
        self.pictures = pictures
        self.image = transform.scale(image.load(pictures[move]), [w, h])
        self.move = move
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.w = w
        self.h = h
        self.position = position'''

mw = display.set_mode((1500, 900))
display.set_caption(("Cave"))

#test_level:
picture = image.load("fon/ground.jpg").convert()
picture = transform.scale(picture, [3000, 2700])

barriers = sprite.Group()

lights = sprite.Group()
light_1 = GameSprite('fon/back.jpg', 525, 235, 380, 240)
light_2 = GameSprite('fon/back.jpg', 179, 250, 560, 470)
lights.add(light_1)
lights.add(light_2)
bullets=sprite.Group()
#level_1:
fon_1 = image.load("fon/back2.jpg").convert()
fon_1 = transform.scale(fon_1, [750, 450])

#групки спрайтів 1:
barriers_1 = sprite.Group()
stones= sprite.Group()
objects = sprite.Group()
monster=sprite.Group()
#дерева:
stone1 = GameSprite("pictures/stone.png", 186, 272, -10, -10)
stone2 = GameSprite("pictures/sstone.png", 238, 238, 10, 100)
stone3 = GameSprite("pictures/ssstone.png", 172, 248, 30, 210)
stone4 = GameSprite("pictures/stone.png", 196, 250, 170, -30)
stone5 = GameSprite("pictures/sstone.png", 172, 272, 210, 150)
stone6 = GameSprite("pictures/ssstone.png", 190, 254, 500, 400)
stone7 = GameSprite("pictures/stone.png", 168, 238, 600, 450)
stone8 = GameSprite("pictures/sstone.png", 176, 246, 430, 520)
stone9 = GameSprite("pictures/ssstone.png", 166, 274, 510, 570)
stone10 = GameSprite("pictures/stone.png", 180, 270, 600, 620)
stone11 = GameSprite("pictures/sstone.png", 186, 272, 620, 360)
stone12 = GameSprite("pictures/ssstone.png", 238, 238, 350, 650)
stone13 = GameSprite("pictures/stone.png", 172, 248, 750, 350)
stone14 = GameSprite("pictures/sstone.png", 196, 250, 700, -50)
stone15 = GameSprite("pictures/ssstone.png", 172, 272, 650, 0)
stone16 = GameSprite("pictures/stone.png", 190, 254, 750, 50)
stone17 = GameSprite("pictures/sstone.png", 168, 238, 1350, -100)
stone18 = GameSprite("pictures/ssstone.png", 176, 246, 1250, -80)
stone19 = GameSprite("pictures/stone.png", 166, 274, 1320, 50)
stone20 = GameSprite("pictures/sstone.png", 180, 270, 1350, 230)
stone21 = GameSprite("pictures/ssstone.png", 186, 272, 850, -80)

stones.add(stone1)
stones.add(stone2)
stones.add(stone3)
stones.add(stone4)
stones.add(stone5)
stones.add(stone6)
stones.add(stone7)
stones.add(stone8)
stones.add(stone9)
stones.add(stone10)
stones.add(stone11)
stones.add(stone12)
stones.add(stone13)
stones.add(stone14)
stones.add(stone15)
stones.add(stone16)
stones.add(stone17)
stones.add(stone18)
stones.add(stone19)
stones.add(stone20)

enemy=Enemy('pictures/enemy_brrr.png',100,100,700,300,15,350,800)
enemy5=Enemy('pictures/zub.png',100,100,850,100,20, 850, 200)
enemy6=Enemy('pictures/zub.png',100,100,870,500,20, 870, 50)
enemy7=Enemy('pictures/zub.png',100,100,870,500,20, 870, 30)
enemy8=Enemy('pictures/zub.png',100,100,700,300,20, 700, 200)



monster.add(enemy)
monster.add(enemy5)
monster.add(enemy6)
monster.add(enemy7)
monster.add(enemy8)

listt=GameSprite('pictures/spysook.png', 50,50,1000,40)
listt1=GameSprite('pictures/spysook.png', 50,50,1100,700)
#невидимі барєри:
nevidimka_1 = GameSprite("pictures/Colide.jpg", 380, 150, 0, 0)
nevidimka_2 = GameSprite("pictures/Colide.jpg", 330, 420, 0, 0)
nevidimka_3 = GameSprite("pictures/Colide.jpg", 160, 460, 0, 0)
nevidimka_4 = GameSprite("pictures/Colide.jpg", 380, 10, 450, 600)
nevidimka_13 = GameSprite("pictures/Colide.jpg", 10, 300, 450, 600)
nevidimka_5 = GameSprite("pictures/Colide.jpg", 30, 30, 830, 570)
nevidimka_6 = GameSprite("pictures/Colide.jpg", 190, 280, 670, 0)
nevidimka_7 = GameSprite("pictures/Colide.jpg", 280, 200, 670, 0)
nevidimka_8 = GameSprite("pictures/Colide.jpg", 10, 10, 840, 300)
nevidimka_9 = GameSprite("pictures/Colide.jpg", 150, 350, 1380, 0)
nevidimka_10 = GameSprite("pictures/Colide.jpg", 200, 60, 1140, 220)
nevidimka_11 = GameSprite("pictures/Colide.jpg", 200, 200, 1330, 0)
nevidimka_12 = GameSprite("pictures/Colide.jpg", 20, 20, 1425, 480)
nevidimka_level_2 = GameSprite("pictures/Colide.jpg", 50, 10, 540, 0)
nevidimka_level_1 = GameSprite("pictures/Colide.jpg", 50, 10, 540, 899)
barriers_1.add(nevidimka_1)
barriers_1.add(nevidimka_2)
barriers_1.add(nevidimka_3)
barriers_1.add(nevidimka_4)
barriers_1.add(nevidimka_5)
barriers_1.add(nevidimka_6)
barriers_1.add(nevidimka_7)
barriers_1.add(nevidimka_8)
barriers_1.add(nevidimka_9)
barriers_1.add(nevidimka_10)
barriers_1.add(nevidimka_11)
barriers_1.add(nevidimka_12)





strilka_lvl_1 = GameSprite("pictures/strelk.png", 50, 50, 550, 20)


#level_2:
#грпки спрайтів:
barriers_2 = sprite.Group()
stones_2 = sprite.Group()
objects_2 = sprite.Group()
monster_2=sprite.Group()

#дерева:
stone1 = GameSprite("pictures/stone.png", 186, 272, -50, -10)
stone2 = GameSprite("pictures/sstone.png", 238, 238, 10, 100)
stone3 = GameSprite("pictures/ssstone.png", 172, 248, 80, 130)
stone4 = GameSprite("pictures/stone.png", 196, 250, 170, -30)
stone5 = GameSprite("pictures/sstone.png", 172, 272, 0, 200)
stone6 = GameSprite("pictures/ssstone.png", 190, 254, -10, 400)
stone7 = GameSprite("pictures/stone.png", 168, 238, 60, 550)
stone8 = GameSprite("pictures/sstone.png", 176, 246, 50, 550)
stone9 = GameSprite("pictures/ssstone.png", 166, 274, -20, 600)
stone10 = GameSprite("pictures/stone.png", 180, 270, 110, 620)
stone11 = GameSprite("pictures/sstone.png", 186, 272, 210, 630)#дерево яке можливо теж буде падати
stone12 = GameSprite("pictures/ssstone.png", 166, 274, 600, 620)#дерево яке має падати
stone13 = GameSprite("pictures/stone.png", 172, 248, 700, 550)
stone14 = GameSprite("pictures/sstone.png", 196, 250, 800, 630)
stone15 = GameSprite("pictures/ssstone.png", 172, 272, 880, 550)
stone16 = GameSprite("pictures/stone.png", 190, 254, 950, 630)
stone17 = GameSprite("pictures/sstone.png", 168, 238, 1350, -100)
stone18 = GameSprite("pictures/ssstone.png", 176, 246, 1250, -80)
stone19 = GameSprite("pictures/stone.png", 166, 274, 1320, 50)
stone20 = GameSprite("pictures/sstone.png", 180, 270, 1350, 230)
stones_2.add(stone1)
stones_2.add(stone2)
stones_2.add(stone3)
stones_2.add(stone4)
stones_2.add(stone5)
stones_2.add(stone6)
stones_2.add(stone7)
stones_2.add(stone8)
stones_2.add(stone9)
stones_2.add(stone10)
stones_2.add(stone11)
stones_2.add(stone13)
stones_2.add(stone14)
stones_2.add(stone12)
stones_2.add(stone15)
stones_2.add(stone16)
stones_2.add(stone17)
stones_2.add(stone18)
stones_2.add(stone19)
stones_2.add(stone20)


#Невидимі барєри:
nevidimka_1 = GameSprite("pictures/Colide.jpg",380, 150, 0, 0)
nevidimka_2 = GameSprite("pictures/Colide.jpg", 280, 220, 0, 0)
nevidimka_3 = GameSprite("pictures/Colide.jpg", 190, 380, 0, 0)
nevidimka_4 = GameSprite("pictures/Colide.jpg", 110, 470, 0, 0)
nevidimka_5 = GameSprite("pictures/Colide.jpg", 310, 140, 0, 760)
nevidimka_6 = GameSprite("pictures/Colide.jpg", 110, 150, 0, 630)
nevidimka_7 = GameSprite("pictures/Colide.jpg", 400, 50, 660, 850)
nevidimka_8 = GameSprite("pictures/Colide.jpg", 200, 100, 780, 780)
nevidimka_9 = GameSprite("pictures/Colide.jpg", 150, 350, 1380, 0)
nevidimka_10 = GameSprite("pictures/Colide.jpg", 200, 200, 1330, 0)
nevidimka_11 = GameSprite("pictures/Colide.jpg", 30, 20, 1425, 480)

barriers_2.add(nevidimka_1)
barriers_2.add(nevidimka_2)
barriers_2.add(nevidimka_3)
barriers_2.add(nevidimka_4)
barriers_2.add(nevidimka_5)
barriers_2.add(nevidimka_6)
barriers_2.add(nevidimka_7)
barriers_2.add(nevidimka_8)
barriers_2.add(nevidimka_9)
barriers_2.add(nevidimka_10)
barriers_2.add(nevidimka_11)

enemy9=Enemy('pictures/gizmo.png',150,150,250,200,35, 250, 200)
enemy10=Enemy('pictures/gizmo.png',150,150,250,200,35, 250, 490)
enemy11=Enemy('pictures/gizmo.png',150,150,250,200,35, 250, 300)
enemy12=Enemy('pictures/gizmo.png',150,150,250,200,35, 250, 350)
enemy13=Enemy('pictures/gizmo.png',150,150,600,500,30, 600, 50)
enemy14=Enemy('pictures/gizmo.png',150,150,600,500,30, 600, 80)


monster_2.add(enemy9)
monster_2.add(enemy10)
monster_2.add(enemy11)
monster_2.add(enemy12)
monster_2.add(enemy13)
monster_2.add(enemy14)

listt2=GameSprite('pictures/spysook.png', 50,50,600,50)
listt3=GameSprite('pictures/spysook.png', 50,50,400,200)
listt4=GameSprite('pictures/spysook.png', 50,50,1200,700)

strilka_lvl_2 = GameSprite("pictures/strelk2.png", 50, 50, 550, 830)

hero = Player('player/karoline_staandd.png', 78, 103, 100, 500, 0, 0, 0)


#звуки:
mixer.init()
mixer.music.load('music/song.mp3')
mixer.music.play(-1)

clock = time.Clock()
run = True
finish = False
level_1 = True
level_2 = False
escape = False
start_sound = True
loose_sound = True
win_sound = True
d_1 = 0
d_2 = 0
d_3 = 0
d_4 = 0
dokazi = 0
werewolf_dlg = False
j = 0
k = 0
amount=0
while run:
    time.delay(50)
    pressed_keys = pygame.key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key== K_LEFT:
                hero.x_speed = -5
            elif e.key== K_RIGHT:
                hero.x_speed = 5
            elif e.key == K_DOWN:
                hero.y_speed = 5
            elif e.key == K_UP:
                hero.y_speed = -5
            elif e.key== K_a:
                hero.x_speed = -5
            elif e.key== K_d:
                hero.x_speed = 5  
            elif e.key == K_w:
                hero.y_speed = -5
            elif e.key == K_s:
                hero.y_speed = 5
            elif e.key == K_SPACE:
                hero.fire()
        elif e.type == KEYUP:
            if e.key== K_LEFT:
                hero.x_speed = 0
            elif e.key== K_RIGHT:
                hero.x_speed = 0
            elif e.key == K_UP:
                hero.y_speed = 0
            elif e.key == K_DOWN:
                hero.y_speed = 0
            if e.key== K_a:
                hero.x_speed = 0
            elif e.key== K_d:
                hero.x_speed = 0
            elif e.key == K_w: 
                hero.y_speed = 0
            elif e.key == K_s:
                hero.y_speed = 0
                

    '''if escape:
        if keys[K_a] or keys[K_w] or keys[K_s] or keys[K_d]:
            camerman.move += 1       
        if camerman.move >= 15:
            camerman.move = 0
        if keys[K_a] and keys[K_w]:
            camerman.x_speed = -10
            camerman.y_speed = -10
            camerman.position = 1
        elif keys[K_a] and keys[K_s]:
            camerman.x_speed = -10
            camerman.y_speed = 10
            camerman.position = 1
        elif keys[K_d] and keys[K_w]:
            camerman.x_speed = 10
            camerman.y_speed = -10
            camerman.position = 0
        elif keys[K_s] and keys[K_d]:
            camerman.x_speed = 10
            camerman.y_speed = 10
            camerman.position = 0 
        elif keys[K_a]:
            camerman.x_speed = -10
            camerman.position = 1
        elif keys[K_d]:
            camerman.x_speed = 10
            camerman.position = 0
        elif keys[K_w]:
            camerman.y_speed = -10
        elif keys[K_s]:
            camerman.y_speed = 10
        if (keys[K_a] or keys[K_w] or keys[K_s] or keys[K_d]) == False:
            camerman.move = 0'''

    

    '''if start_menu:
        fon_start_menu = transform.scale(image.load("Assets/werewolf_fon.jpg"), [1500, 900])
        mw.fill((255, 255, 255))
        mw.blit(fon_start_menu, (0, 0))
        button_story = Button("Assets/Buttons/Story_button.png", 280, 88, 1000, 250)
        button_story.reset()
        button_test_level = Button("Assets/Buttons/Test_Level_button.png", 280, 88, 1000, 400)
        button_test_level.reset()
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if button_story.colidepoint(x, y):
                start_menu = False
                level_1 = True
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            if button_test_level.colidepoint(x, y):
                start_menu = False
                test_level = True'''
     
    '''if not level_1 and sprite.collide_rect(camerman, werewolf):
        finish = True
        test_level = False
        level_1 = False
        lose = transform.scale(image.load("Assets/game_over.jpg"), [1500, 900])
        mw.fill((255, 255, 255))
        mw.blit(lose, (0, 0))'''

    if not finish:
        mw.blit(fon_1, [0, 0])
        mw.blit(fon_1, [0, 450])
        mw.blit(fon_1, [750, 0])
        mw.blit(fon_1, [750, 450])
        if level_1:
            if sprite.collide_rect(nevidimka_level_2, hero):
                level_1 = False
                level_2 = True
                hero.level_update(2)
            #barriers_1.draw(mw)
            strilka_lvl_1.reset()
            monster.update()
            monster.draw(mw)
            hero.draw()
            hero.update(barriers_1)
            stones.draw(mw)
            listt.reset()
            listt1.reset()
            bullets.update()
            bullets.draw(mw)
            sprite.groupcollide(monster,bullets, True,True)
            sprite.groupcollide(bullets,barriers_1,True,False)
            sprite.groupcollide(bullets,stones,True,False)
            if sprite.collide_rect(hero,listt):
                amount+=1
                del listt
            if sprite.collide_rect(hero,listt1):
                amount+=1
                del listt1
            if sprite.spritecollide(hero,monster,False):
        
                finish=True
                img=image.load('fon/game__over.jpg')
                mw.blit(transform.scale(img,(1500,900)),(0,0))
   
        if level_2:
            hero.update(barriers_2)
            if sprite.collide_rect(nevidimka_level_1, hero):
                level_2 = False
                level_1 = True
                hero.level_update(1)
            strilka_lvl_2.reset()
            monster_2.update()
            monster_2.draw(mw)
            listt2.reset()
            listt3.reset()
            listt4.reset()
            bullets.update()
            bullets.draw(mw)
            sprite.groupcollide(monster,bullets, True,True)
            sprite.groupcollide(bullets,barriers_2,True,False)
            sprite.groupcollide(bullets,stones_2,True,False)
            if sprite.collide_rect(hero,listt2):
                amount+=1
                del listt2
            if sprite.collide_rect(hero,listt3):
                amount+=1
                del listt3
            if sprite.collide_rect(hero,listt4):
                amount+=1
                del listt4
            hero.draw()
            hero.update(barriers_1)
            stones_2.draw(mw)
            if sprite.spritecollide(hero,monster_2,False):
                finish=True
                imgg=image.load('fon/game__over.jpg')
                mw.blit(transform.scale(imgg,(1500,900)),(0,0))
        if amount == 5:
            if false==True:
                finish=True
                imggg=image.load('fon/you__win.jpg')             
                mw.blit(transform.scale(imggg,(1500,900)),(0,0))
            #barriers_2.draw(mw)
        


    '''if test_level:
        mw.blit(picture, [0, 0])
        barriers.draw(mw)
        camerman.draw()
        werewolf.draw()
        camerman.update(barriers)
        werewolf.update(barriers)
        camerman.moves()
        werewolf.moves()'''
    display.update()
    clock.tick(40)