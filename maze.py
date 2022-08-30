import pygame

pygame.init()
pygame.mixer.init()

win_width = 700
win_height = 500
FPS = 60

clock = pygame.time.Clock()
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Maze')

background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (win_width, win_height))

def imgfromtext(text, size, color = (0, 0, 0)):
    return pygame.font.Font(None, size).render(text, False, color)

class Sprite:
    def __init__(self, window : pygame.display.set_mode, width : int, height : int, images : list() = [], sounds : list() = [], speed : int = 1):
        self.images = list()
        self.sounds = list()
        self.speed = speed
        self.width = width
        self.height = height
        for image in images:
            if type(image) == type(''):
                self.images.append(pygame.transform.scale(pygame.image.load(image), (width, height)))
            else:
                self.images.append(pygame.transform.scale(image, (width, height)))
        self.image = 0
        self.rect = pygame.rect.Rect(0, 0, width, height)
        if self.images:
            self.__upimg__()
        for sound in sounds:
            self.sounds.append(pygame.mixer.Sound(sound))
        self.window = window

    def __upimg__(self):
        self.img = self.images[self.image]
        self.rect = self.img.get_rect()

    def draw(self):
        self.window.blit(self.img, (self.rect.x, self.rect.y))

    def goto(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_img(self, num):
        self.image = num
        self.__upimg__()

    def add_img(self, img):
        self.images.append(pygame.transform.scale(img, (width, height)))
        self.__upimg__()

    def collide(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def play(self, num):
        self.sounds[num].play()

    def controls(self, *args):
        keys = pygame.key.get_pressed()
        if keys[args[0]]:
            if self.rect.x > 0:
                self.rect.x -= self.speed
        if keys[args[1]]:
            if (self.rect.x + self.rect.width) < win_width:
                self.rect.x += self.speed
        if keys[args[2]]:
            if self.rect.y > 0:
                self.rect.y -= self.speed
        if keys[args[3]]:
            if (self.rect.y + self.rect.height) < win_height:
                self.rect.y += self.speed

background = Sprite(win, win_width, win_height, ['background.jpg'], ['jungles.ogg'])
hero = Sprite(win, 50, 50, ['hero.png'], ['kick.ogg', 'money.ogg'], 5)
cyborg = Sprite(win, 50, 50, ['cyborg.png'], [], 5)
enemy = Sprite(win, 50, 50, ['cyborg.png'], [], 5)
treasure = Sprite(win, 50, 50, ['treasure.png'])
wall1 = Sprite(win, 10, 400, [imgfromtext('1', 0, (0, 255, 0))])
wall2 = Sprite(win, 10, 400, [imgfromtext('1', 0, (0, 255, 0))])
wall3 = Sprite(win, 10, 400, [imgfromtext('1', 0, (0, 255, 0))])
wall4 = Sprite(win, 10, 400, [imgfromtext('1', 0, (0, 255, 0))])
wall5 = Sprite(win, 10, 400, [imgfromtext('1', 0, (0, 255, 0))])
wall6 = Sprite(win, 10, 400, [imgfromtext('1', 0, (0, 255, 0))])

hero.goto(10, 410)
cyborg.goto(610, 310)
treasure.goto(640, 440)
wall1.goto(100, 100)
wall2.goto(200, 100)
wall3.goto(300, 000)
wall4.goto(400, 100)
wall5.goto(500, 000)
wall6.goto(600, 100)

cyborg.xlst = [440.0, 443.3333333333333, 446.6666666666667, 450.0, 453.3333333333333, 456.6666666666667, 460.0, 463.3333333333333, 466.6666666666667, 470.0, 473.3333333333333, 476.6666666666667, 480.0, 483.3333333333333, 486.6666666666667, 490.0, 493.3333333333333, 496.6666666666667, 500.0, 503.3333333333333, 506.6666666666667, 510.0, 513.3333333333334, 516.6666666666666, 520.0, 523.3333333333334, 526.6666666666666, 530.0, 533.3333333333334, 536.6666666666666, 540.0, 543.3333333333334, 546.6666666666666, 550.0, 553.3333333333334, 556.6666666666666, 560.0, 563.3333333333334, 566.6666666666666, 570.0, 573.3333333333334, 576.6666666666667, 580.0, 583.3333333333334, 586.6666666666667, 590.0, 593.3333333333334, 596.6666666666667, 600.0, 603.3333333333334, 606.6666666666667, 610.0, 613.3333333333334, 616.6666666666667, 620.0, 623.3333333333334, 626.6666666666667, 630.0, 633.3333333333334, 636.6666666666667, 640.0, 636.6666666666667, 633.3333333333334, 630.0, 626.6666666666667, 623.3333333333334, 620.0, 616.6666666666667, 613.3333333333334, 610.0, 606.6666666666667, 603.3333333333334, 600.0, 596.6666666666667, 593.3333333333334, 590.0, 586.6666666666667, 583.3333333333334, 580.0, 576.6666666666667, 573.3333333333334, 570.0, 566.6666666666666, 563.3333333333334, 560.0, 556.6666666666666, 553.3333333333334, 550.0, 546.6666666666666, 543.3333333333334, 540.0, 536.6666666666666, 533.3333333333334, 530.0, 526.6666666666666, 523.3333333333334, 520.0, 516.6666666666666, 513.3333333333334, 510.0, 506.6666666666667, 503.3333333333333, 500.0, 496.6666666666667, 493.3333333333333, 490.0, 486.6666666666667, 483.3333333333333, 480.0, 476.6666666666667, 473.3333333333333, 470.0, 466.6666666666667, 463.3333333333333, 460.0, 456.6666666666667, 453.3333333333333, 450.0, 446.6666666666667, 443.3333333333333, 440.0]
cyborg.ylst = [440.0, 437.8333333333333, 435.6666666666667, 433.5, 431.3333333333333, 429.1666666666667, 427.0, 424.8333333333333, 422.6666666666667, 420.5, 418.3333333333333, 416.1666666666667, 414.0, 411.8333333333333, 409.6666666666667, 407.5, 405.3333333333333, 403.1666666666667, 401.0, 398.8333333333333, 396.6666666666667, 394.5, 392.3333333333333, 390.1666666666667, 388.0, 385.8333333333333, 383.6666666666667, 381.5, 379.3333333333333, 377.1666666666667, 375.0, 372.83333333333337, 370.6666666666667, 368.5, 366.33333333333337, 364.1666666666667, 362.0, 359.83333333333337, 357.6666666666667, 355.5, 353.33333333333337, 351.1666666666667, 349.0, 346.83333333333337, 344.6666666666667, 342.5, 340.33333333333337, 338.1666666666667, 336.0, 333.83333333333337, 331.6666666666667, 329.5, 327.33333333333337, 325.1666666666667, 323.0, 320.83333333333337, 318.6666666666667, 316.5, 314.33333333333337, 312.1666666666667, 310.0, 312.1666666666667, 314.33333333333337, 316.5, 318.6666666666667, 320.83333333333337, 323.0, 325.1666666666667, 327.33333333333337, 329.5, 331.6666666666667, 333.83333333333337, 336.0, 338.1666666666667, 340.33333333333337, 342.5, 344.6666666666667, 346.83333333333337, 349.0, 351.1666666666667, 353.33333333333337, 355.5, 357.6666666666667, 359.83333333333337, 362.0, 364.1666666666667, 366.33333333333337, 368.5, 370.6666666666667, 372.83333333333337, 375.0, 377.1666666666667, 379.3333333333333, 381.5, 383.6666666666667, 385.8333333333333, 388.0, 390.1666666666667, 392.3333333333333, 394.5, 396.6666666666667, 398.8333333333333, 401.0, 403.1666666666667, 405.3333333333333, 407.5, 409.6666666666667, 411.8333333333333, 414.0, 416.1666666666667, 418.3333333333333, 420.5, 422.6666666666667, 424.8333333333333, 427.0, 429.1666666666667, 431.3333333333333, 433.5, 435.6666666666667, 437.8333333333333, 440.0]
enemy.xlst = [0.0, 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0, 27.5, 30.0, 32.5, 35.0, 37.5, 40.0, 42.5, 45.0, 47.5, 50.0, 52.5, 55.0, 57.5, 60.0, 62.5, 65.0, 67.5, 70.0, 72.5, 75.0, 77.5, 80.0, 82.5, 85.0, 87.5, 90.0, 92.5, 95.0, 97.5, 100.0, 102.5, 105.0, 107.5, 110.0, 112.5, 115.0, 117.5, 120.0, 122.5, 125.0, 127.5, 130.0, 132.5, 135.0, 137.5, 140.0, 142.5, 145.0, 147.5, 150.0, 147.5, 145.0, 142.5, 140.0, 137.5, 135.0, 132.5, 130.0, 127.5, 125.0, 122.5, 120.0, 117.5, 115.0, 112.5, 110.0, 107.5, 105.0, 102.5, 100.0, 97.5, 95.0, 92.5, 90.0, 87.5, 85.0, 82.5, 80.0, 77.5, 75.0, 72.5, 70.0, 67.5, 65.0, 62.5, 60.0, 57.5, 55.0, 52.5, 50.0, 47.5, 45.0, 42.5, 40.0, 37.5, 35.0, 32.5, 30.0, 27.5, 25.0, 22.5, 20.0, 17.5, 15.0, 12.5, 10.0, 7.5, 5.0, 2.5, 0.0]
enemy.ylst = enemy.xlst.copy()
background.play(0)

cyborg.xw = 0
cyborg.yw = 0
cyborg.xch = 1
cyborg.ych = 1
while True:
    keys = pygame.key.get_pressed()
    if cyborg.xw >= FPS or cyborg.xw < 0:
        cyborg.xch *= -1
    if cyborg.yw >= FPS or cyborg.yw < 0:
        cyborg.ych *= -1
    if hero.collide(cyborg) or hero.collide(enemy) or hero.collide(wall1) or hero.collide(wall2) or hero.collide(wall3) or hero.collide(wall4) or hero.collide(wall5) or hero.collide(wall6):
        hero.play(0)
        lbl = Sprite(win, 100, 10, [], [])
        lbl.images.append(imgfromtext('!YOU LOSE!', 72))
        lbl.set_img(0)
        lbl.goto(200, 20)
        lbl.draw()
        break
    if hero.collide(treasure):
        hero.play(1)
        lbl = Sprite(win, 100, 10, [], [])
        lbl.images.append(imgfromtext('!YOU WIN!', 72))
        lbl.set_img(0)
        lbl.goto(200, 200)
        lbl.draw()
        break
    hero.controls(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
    background.draw()
    hero.draw()
    cyborg.draw()
    enemy.draw()
    treasure.draw()
    if not keys[pygame.K_BACKSPACE]:
        wall1.draw()
        wall2.draw()
        wall3.draw()
        wall4.draw()
        wall5.draw()
        wall6.draw()
    cyborg.goto(cyborg.xlst[cyborg.xw], cyborg.ylst[cyborg.yw])
    enemy.goto(enemy.xlst[cyborg.xw], enemy.ylst[cyborg.yw])
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(FPS)
    cyborg.xw += cyborg.xch
    cyborg.yw += cyborg.ych
    pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()