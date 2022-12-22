import pygame
import random
import functions

pygame.init()

size = [1618,1000]

#색깔
Black = (0,0,0)
White = (255,255,255)
Red = (233,100,100)
Green = (60,179,113)
Blue = (74,168,216)
Gray = (211,211,211)
Background = (246,246,246)

#폰트 가져오기
font = pygame.font.SysFont("airal",30)

###################
#function 가져오기#
###################

screen_update = functions.screen_update
class_Stage = functions.Stage

# #############
# #클래스 모음#
# #############

# #이미지 로드 클래스
# class ScreenObject:
#     def __init__(self,sort,content,pos_x=404.5,pos_y=250,blanding = True,txt_color = Black):
#         self.sort = sort
#         self.content = content
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.txt_color = txt_color
#         self.blanding = blanding
        
#         if sort == "img":
#             self.img= pygame.image.load(content)
#             self.rect = self.img.get_rect()
#             self.rect.centerx = pos_x
#             self.rect.centery = pos_y
        
#         elif sort == "txt":
#             self.txt = font.render(content,blanding,txt_color)
#             self.rect = self.txt.get_rect()
#             self.rect.centerx = pos_x
#             self.rect.centery = pos_y
    
#     def rebuild(self):
#         if self.sort == "img":
#             self.img= pygame.image.load(self.content)
#             self.rect = self.img.get_rect()
#             self.rect.centerx = self.pos_x
#             self.rect.centery = self.pos_y
        
#         elif self.sort == "txt":
#             self.txt = font.render(self.content,self.blanding,self.txt_color)
#             self.rect = self.txt.get_rect()
#             self.rect.centerx = self.pos_x
#             self.rect.centery = self.pos_y

# #텍스트 창 클래스
# class ScreenTxt:
#     def __init__(self,sort = 1,name = "I",txt1_1_content ="Shall I compare thee to a summer's day?" ,txt2_1_content="Shall I compare thee to a summer's day?",txt2_2_content="Shall I compare thee to a summer's day?"):
#         self.sort = sort
#         self.txt1_1_content = txt1_1_content
#         self.txt2_1_content = txt2_1_content
#         self.txt2_2_content = txt2_2_content
#         self.name = name

#         txt0_name = ScreenObject("txt",name,pos_x=140,pos_y=355) 
#         txt1_1 = ScreenObject("txt",txt1_1_content,pos_y=400)
#         txt2_1 = ScreenObject("txt",txt2_1_content,pos_y=395)
#         txt2_2 = ScreenObject("txt",txt2_2_content,pos_y=415)       
        
#         pygame.draw.rect(screen,White,(50,350,709,100))
#         pygame.draw.rect(screen,Black,(50,350,709,100),5)
#         pygame.draw.rect(screen,White,(65,335,150,40))
#         pygame.draw.rect(screen,Black,(65,335,150,40),5)
        
#         screen.blit(txt0_name.txt,txt0_name.rect)
        
#         if sort == 1:
#             screen.blit(txt1_1.txt,txt1_1.rect)
        
#         elif sort == 2:
#             screen.blit(txt2_1.txt,txt2_1.rect)
#             screen.blit(txt2_2.txt,txt2_2.rect)

#         screen_update()

# caption_img = ScreenObject("img",content="pngwing.com.png")

# screen = pygame.display.set_mode(size)

# screen.fill(Background)
# ##################################
# class MapBlock:
#     def __init__(self,name,mode = "none"):
#         self.name = name
#         self.mode = mode
#         self.pos_x = name[0]
#         self.pos_y = name[1]

#     def build(self):
#         print("test {}".format(self.name))
#         pygame.draw.rect(screen,Gray,(self.pos_x,self.pos_y,100,100))
#         pygame.draw.rect(screen,Black,(self.pos_x,self.pos_y,100,100),3)

# protago_hp = 100

# map_size = [[],
#             [],
#             [],
#             [],
#             [],
#             [],
#             [],
#             [],
# ]

# for i in range(0,8):
#     for j in range(0,10):
#         map_size[i].append(MapBlock(name=[i,j]))
        
#         map_size[i][j].pos_x = 500 + 101*j 

#         map_size[i][j].pos_y = 100 + 101*i 

#         map_size[i][j].build()

# class StageSet:
#     def __init__(self,mode = "none",size_x = 8,size_y = 10,background = "none",protago_hp = protago_hp) -> None:
#         self.mode = mode
#         self.size_x = size_x
#         self.size_y = size_y
#         self.bakground =background
#         self.protago_hp = protago_hp
    
#     def rebuild(self):
#         for i in range(0,len(map_size)):
#             for j in range(0,len(map_size[i])):
#                 map_size[i][j].build()

# stage_test = StageSet()
# screen_update()
# ##
# class Character:
#     def __init__(self,name = "protago",skill_01 = "none",skill_02 = "none",pos_x = 0,pos_y = 0) -> None:
#         self.name = name
#         self.skill_01 = skill_01
#         self.skill_02 = skill_02
#         self.pos_x = pos_x
#         self.pos_y = pos_y
        
#         self.object = ScreenObject(sort="img",content="protago.png")
    
#     def moving(self):      
#         self.object.pos_x = map_size[self.pos_x][self.pos_y].pos_x + 50
#         print(self.object.pos_x)
#         self.object.pos_y = map_size[self.pos_x][self.pos_y].pos_y + 50
#         print(self.object.pos_y)
#         print(self.object.rect)
#         self.object.rebuild()
#         screen.blit(self.object.img,self.object.rect)
#         screen_update()
    
    

# prota = Character()
# prota.moving()

# End = False

# while not End:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             End = True

#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT and prota.pos_y > 0:
#                 prota.pos_y -= 1
            
#             elif event.key == pygame.K_RIGHT and prota.pos_y < stage_test.size_y-1:
#                 prota.pos_y += 1
            
#             elif event.key == pygame.K_DOWN and prota.pos_x < stage_test.size_x-1:
#                 prota.pos_x += 1
            
#             elif event.key == pygame.K_UP and prota.pos_x > 0:
#                 prota.pos_x -= 1

#             stage_test.rebuild()
#             prota.moving()
#             print(prota.pos_x,prota.pos_y)
def start():
    First_Stage = class_Stage()

    First_Stage.init()
