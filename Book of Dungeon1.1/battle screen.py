import sys
import pygame

white=255,255,255

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1618, 1000
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
            ])
        screen.blit(self.buttonSurface, self.buttonRect)

def attack():
    print("1")

def defense():
    pygame.quit()
    
        
def healing():
    pygame.quit()
    sys.exit()

Button(170, 800, 350, 100, 'attack', attack)
Button(620, 800, 350, 100, 'defense', defense)
Button(620, 800, 350, 100, 'defense', defense)
Button(620, 800, 350, 100, 'defense', defense)
Button(1070, 800, 350, 100, 'healing', healing)

while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.draw.rect(screen, (white), (100, 680, 1400, 300), 1)

    for object in objects:
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)