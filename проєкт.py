from pygame import*

window = display.set_mode((700, 500))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
fire_sound=mixer.Sound("fire.ogg")

img_back="galaxy.jpg"
img_hero="rocket.png"
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        def fire(self):
            pass

win_width =1200
win_height = 800

ship=Player(img_hero,5,win_width-100,80,100,10)

finish=False

run=True

while run:
    for e in event.get():
        if e.type == QUIT:
            run= False
    window.blit(background,(0,0))
    ship.update()
    ship.reset()
    display.update()
    time.delay(50)