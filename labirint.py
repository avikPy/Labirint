# Разработай свою игру в этом файле!
import pygame

window = pygame.display.set_mode((700,500))
pygame.display.set_caption('Лабиринт')

run = True
clock = pygame.time.Clock()
FPS = 50

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,x,y,width,height):
        super().__init__()
        img = pygame.image.load(image_name)
        self.image = pygame.transform.scale(img,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
    def rotate(self,degree):
        self.image = pygame.transform.rotate(self.image, degree)


class Player(GameSprite):
    def __init__(self, image_name, x, y, width, height, speed_x,speed_y):
        super().__init__(image_name,x,y,width,height)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        # self.rect.x += self.speed_x
        # self.rect.y += self.speed_y
        if self.rect.x <= 700 - 70 and self.speed_x > 0 or self.rect.x >= 0 and self.speed_x < 0:
            self.rect.x += self.speed_x
        
        if self.rect.y <= 500 - 80 and self.speed_y > 0 or self.rect.y >= 0 and self.speed_y < 0:
            self.rect.y += self.speed_y
            
        platforms_toched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_x > 0:
            for plat in platforms_toched:
                self.rect.right = min(self.rect.right, plat.rect.left)
        
        elif self.speed_x < 0:
            for plat in platforms_toched:
                self.rect.left = max(self.rect.left, plat.rect.right)
        
        elif self.speed_y > 0:
            for plat in platforms_toched:
                self.rect.bottom = min(self.rect.bottom, plat.rect.top)
        
        elif self.speed_y < 0:
            for plat in platforms_toched:
                self.rect.top = max(self.rect.top, plat.rect.bottom)       
                
                
                
    def fire(self):
        bullet = Bullet(
            image_name = 'images/fbullet.png',
            x = self.rect.right,
            y = self.rect.centery,
            width = 40,
            height = 20,
            speed = 5)
        
        bullets.add(bullet)
        
        
bullets = pygame.sprite.Group()
        

class Enemy(GameSprite):
    def __init__(self,image_name,x,y,width,height,speed):
        super().__init__(image_name,x,y,width,height)
        self.speed = speed
        self.direction = None
        
    def move(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 700 - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
    def move2(self):        
        if self.rect.x <= 0:
            self.direction = 'right'
        if self.rect.x >= 700 - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    

class Bullet(GameSprite):
    def __init__(self,image_name,x,y,width,height,speed):
        super().__init__(image_name,x,y,width,height)
        self.speed = speed
        
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 700:
            self.kill()
        






pygame.font.init()
font = pygame.font.SysFont('Arial',60)
def win():
    window.fill((0,255,100))
    win_text = font.render('YOU WIN!',True,(33, 219, 184))
    window.blit(win_text, (220,220))

def louse():
    window.fill((255,0,100))
    louse_text = font.render('YOU LOUSE!',True,(255,0,0))
    window.blit(louse_text, (180,220))
    
    
background = GameSprite(image_name = 'images/colorful.png',
                        x = 0,
                        y = 0,
                        width = 700,
                        height = 500)

platform = GameSprite(image_name = 'images/wall.png',
                        x = 150,
                        y = 220,
                        width = 300,
                        height = 100)

platform2 = GameSprite(image_name = 'images/wall.png',
                        x = 340,
                        y = 130,
                        width = 120,
                        height = 400)
# platform2.rotate(90)

walls = pygame.sprite.Group()
walls.add(platform)
walls.add(platform2)

ghost = Player(image_name = 'images/ghost.png',
                    x = 50,
                    y = 400,
                    width = 70,
                    height = 80,
                    speed_x = 0,
                    speed_y = 0)

cake = GameSprite(image_name = 'images/cake.png',
                    x = 600,
                    y = 420,
                    width = 70,
                    height = 60)

evil = Enemy(image_name = 'images/evil.png',
                    x = 620,
                    y = 200,
                    width = 70,
                    height = 70,
                    speed = 4)

evil2 = Enemy(image_name = 'images/evil.png',
                    x = 20,
                    y = 40,
                    width = 70,
                    height = 70,
                    speed = 4)




# dddddd
finish = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                ghost.speed_y = -5
                
            elif event.key == pygame.K_s:
                ghost.speed_y = 5
            
            elif event.key == pygame.K_a:
                ghost.speed_x = -5
                
            elif event.key == pygame.K_d:
                ghost.speed_x = 5
            elif event.key == pygame.K_SPACE:
                ghost.fire()



        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                ghost.speed_y = 0
                
            elif event.key == pygame.K_s:
                ghost.speed_y = 0
            
            elif event.key == pygame.K_a:
                ghost.speed_x = 0
                
            elif event.key == pygame.K_d:
                ghost.speed_x = 0
        
        
        
        
    if not finish:
        
        
        
        background.draw()
        platform.draw()
        ghost.draw()
        cake.draw()
        evil.draw()
        platform2.draw()
        ghost.move()
        evil.move()
        bullets.draw(window)
        bullets.update()
        evil2.draw()
        evil2.move2()
        
        if pygame.sprite.spritecollide(evil, bullets, True):
            evil.rect.x = 800
            evil.rect.y = 800
            evil.kill()
        
        
        pygame.sprite.groupcollide(bullets, walls, True, False)
        
        if ghost.rect.colliderect(evil.rect):
            louse()
            finish = True
            
        if ghost.rect.colliderect(cake.rect):
            win()
            finish = True
    clock.tick(FPS)
    pygame.display.update()
            