# Imports
import sys
import pygame
import functions

# Configuration
pygame.init()
pygame.display.set_caption("Book of Dungeon")

caption_logo = pygame.image.load("image\guitar\caption_logo.png")
pygame.display.set_icon(caption_logo)

width, height = 1618, 1000
screen = pygame.display.set_mode((width, height))

#색깔
Black = (12,12,12)
White = (255,255,255)
Red = (233,100,100)
Green = (60,179,113)
Blue = (74,168,216)
Gray = (211,211,211)
Background = (246,246,246)

#폰트 가져오기
font = pygame.font.SysFont("airal",30)

# functions.intro()

def menu():
    # Configuration
    pygame.init()
    pygame.display.set_caption("Book of Dungeon")

    caption_logo = pygame.image.load("image\guitar\caption_logo.png")
    pygame.display.set_icon(caption_logo)

    width, height = 1618, 1000
    screen = pygame.display.set_mode((width, height))

    Background = (246,246,246)

    #폰트 가져오기
    font = pygame.font.SysFont("airal",30)

    ###################
    #function 가져오기#
    ###################

    screen_update = functions.screen_update
    class_Stage = functions.Stage
    fadeout = functions.fadeout

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

    def myFunction1():
        tro_bgm = functions.tro_bgm
        tro_bgm.fadeout(2000)
        txt0 = functions.ScreenObject("txt","Loading...",pos_x=809,pos_y=500,txt_color=Background)
        screen_update()
        screen.blit(txt0.txt,txt0.rect)
        fadeout(color = (20, 20, 20))

        First_Stage = class_Stage()

        First_Stage.init()


    def myFunction2():
        fadeout(color=Background)
        manual()     

    def myFunction3():
        pygame.quit()
        sys.exit()


    Button(120, 800, 400, 100, 'game start', myFunction1)
    Button(620, 800, 400, 100, 'game menual', myFunction2)
    Button(1120, 800, 400, 100, 'exit', myFunction3)

    screen.fill((20, 20, 20))
    main_screen_background = functions.ScreenObject("img",r"image\background\main screen background.jpg",pos_x = 809,pos_y=500)
    screen.blit(main_screen_background.img,main_screen_background.rect)
    screen_update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for object in objects:
            object.process()
        pygame.display.flip()

    
def manual():
    pygame.init()
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

    def game_menu():
        fadeout = functions.fadeout
        fadeout(color=(246,246,246))
        menu()

    Button(1100, 800, 400, 100, 'menu', game_menu)

    while True:
        screen.fill((20, 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        image1 = pygame.image.load(r"image\manual\manual .png")
        screen.blit(image1, (0, 0))

        for object in objects:
            object.process()
        
        pygame.display.flip()

functions.intro()
menu()
