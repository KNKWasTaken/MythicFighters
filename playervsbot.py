import pygame, sys, os, random
from playerdict import *
from PIL import Image

class literalPlayer(pygame.sprite.Sprite):
    def __init__(self, name: str | None = "", action: str | None = "", health: int | None = 0, defence: int | None = 0, output: str | None = "Assets/RunTimeData", center: tuple | None = (0, 0), flipx: bool | None = False, flipy: bool | None = False):
        super().__init__()
        self.name = name
        self.state = action
        self.output = output
        self.flipx = flipx
        self.flipy = flipy
        self.images = self.extractImages(name, action, output, flipx, flipy)
        self.currentImage = 0
        self.image = self.images[self.currentImage]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.animationSpeed = 0.6
        self.health = health
        self.defence = defence
        self.stateCheck = False
        self.pendingState = None

    def update(self, dt):
        self.currentImage += self.animationSpeed
        if self.currentImage >= len(self.images):
            self.currentImage = 0
            self.stateCheck = True
            if self.pendingState:
                self.newState(self.pendingState)
                self.pendingState = None
        self.image = self.images[int(self.currentImage)]

    def newState(self, state):
        self.state = state
        self.images = self.extractImages(self.name, self.state, self.output, self.flipx, self.flipy)
        self.currentImage = 0
        self.stateCheck = False

    def extractImages(self, name, action, output, flipx, flipy):
        frameList = []
        with Image.open(f'Assets/{name}{action}.gif') as img:
            for frame in range(img.n_frames):
                img.seek(frame)
                frameImage = img.convert('RGBA')
                framePath = os.path.join(output, f'{name}{action}{frame}.png')
                frameImage.save(framePath)
                frameList.append(pygame.transform.flip(pygame.image.load(framePath).convert_alpha(), flipx, flipy))
            
        return frameList
    

def textrender(text: str, font: pygame.font.Font, color: tuple, window: pygame.Surface, size: tuple):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(size[0]//2, size[1]//2))
    window.blit(surface, rect)

def statusrender(window, font, chara, charb, size):
    charatextlines = [
        f"Player 1",
        f"HP: {chara.health}",
        f"DEF: {chara.defence}"
    ]
    charbtextlines = [
        f"Player 2",
        f"HP: {charb.health}",
        f"DEF: {charb.defence}"
    ]
    
    for i, line in enumerate(charatextlines):
        linesurface = font.render(line, True, (255, 255, 255))
        window.blit(linesurface, (10, 10 + i * 40))  # Adjust the position as needed

    for i, line in enumerate(charbtextlines):
        linesurface = font.render(line, True, (255, 255, 255))
        linerect = linesurface.get_rect(topright=(size[0] - 10, 10 + i * 40))  # Adjust the position as needed
        window.blit(linesurface, linerect)

def atk(victim: literalPlayer, damage: int | None = 0):
    if victim.defence > 0:
        victim.defence -= 1
    else:
        victim.health -= damage

def selfdef(user: literalPlayer, defup: int):
    user.defence += defup

def cleanup():
    directory = 'Assets/RunTimeData'
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

pygame.init()
pygame.font.init()

namea = input('namea/')
nameb = input('nameb/')

size = (1250, 700)
window = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.Font('Assets/Font/Disket-Mono-Bold.ttf', 36)
pygame.display.set_caption('GameTest')

bg = pygame.image.load('Assets/bg.png')
chara = literalPlayer(namea, "Idle", center=(230, 500), health=10)
charb = literalPlayer(nameb, "Idle", center=(1020, 500), flipx=True, health=10)
attacka = literalPlayer('Attack', 'Default', center=(610, 500))
attackb  = literalPlayer('Attack', 'Default', center=(610, 500), flipx=True)
allSprites = pygame.sprite.Group(chara, charb, attacka, attackb)
message = None

turncount = 0

run = True
while run:
    dt = clock.tick(60) / 1000

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if turncount % 2 == 0 and any(keys[key] for key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]):
        if chara.name == 'Akiro':
            if keys[pygame.K_1]:
                exec(Akiro['move1'].format(char='chara', victim='charb', atkframe='attacka'))
            elif keys[pygame.K_2]:
                exec(Akiro['move2'].format(char='chara', victim='charb', atkframe='attacka'))
            elif keys[pygame.K_3]:
                exec(Akiro['move3'].format(char='chara', message='message'))
            elif keys[pygame.K_4]:
                exec(Akiro['move4'].format(char='chara', message='message'))
        elif chara.name == 'Mac':
            if keys[pygame.K_1]:
                exec(Mac['move1'].format(char='chara', victim='charb', atkframe='attacka'))
            elif keys[pygame.K_2]:
                exec(Mac['move2'].format(char='chara', victim='charb', atkframe='attacka'))
            elif keys[pygame.K_3]:
                exec(Mac['move3'].format(char='chara', message='message'))
            elif keys[pygame.K_4]:
                exec(Mac['move4'].format(char='chara', message='message'))
        turncount += 1
    elif turncount % 2 != 0:
        botMove = random.randint(1, 4)
        pygame.time.delay(5000)
        if charb.name == 'Akiro':
            if botMove == 1:
                exec(Akiro['move1'].format(char='charb', victim='chara', atkframe='attackb'))
            elif botMove == 2:
                exec(Akiro['move2'].format(char='charb', victim='chara', atkframe='attackb'))
            elif botMove == 3:
                exec(Akiro['move3'].format(char='charb', message='message'))
            elif botMove == 4:
                exec(Akiro['move4'].format(char='charb', message='message'))
        elif charb.name == 'Mac':
            if botMove == 1:
                exec(Mac['move1'].format(char='charb', victim='chara', atkframe='attackb'))
            elif botMove == 2:
                exec(Mac['move2'].format(char='charb', victim='chara', atkframe='attackb'))
            elif botMove == 3:
                exec(Mac['move3'].format(char='charb', message='message'))
            elif botMove == 4:
                exec(Mac['move4'].format(char='charb', message='message'))
        turncount += 1

    allSprites.update(dt)

    window.blit(bg, (0,0))
    
    allSprites.draw(window)

    if message:
        textrender(message, font, (255,255,255), window, size)
        pygame.display.flip
        pygame.time.delay(1000)
        message = None

    statusrender(window, font, chara, charb, size)

    pygame.display.flip()

    if chara.health <= 0:
        chara.kill()
        allSprites.remove(chara)
        textrender('GAME OVER', font, (255,0,0), window, size)
        pygame.time.delay(10000)
        run = False
        print('Winner is 1')
    elif charb.health <= 0:
        charb.kill()
        allSprites.remove(charb)
        textrender('GAME OVER', font, (255,0,0), window, size)
        pygame.time.delay(10000)
        run = False
        print('Winner is 2')

pygame.quit()
cleanup()
sys.exit()