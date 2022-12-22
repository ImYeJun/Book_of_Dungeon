import pygame
import random
import time
import sys

###########
#기본 세팅#
###########

#색깔
Black = (12,12,12)
White = (255,255,255)
Red = (233,100,100)
Green = (60,179,113)
Blue = (74,168,216)
Gray = (128,128,128)
Background = (246,246,246)

pygame.init()
pygame.font.init()

size = [1618,1000]

screen = pygame.display.set_mode(size)

screen.fill(Background)

#폰트 가져오기
font = pygame.font.SysFont("airal",50)

################
#필수 함수 모음#
################

#화면 업데이트
def screen_update():
    pygame.display.update()

#이미지 로드 클래스
class ScreenObject:
    def __init__(self,sort,content,pos_x=404.5,pos_y=250,blanding = True,txt_color = Black):
        self.sort = sort
        self.content = content
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.txt_color = txt_color
        self.blanding = blanding
        
        if sort == "img":
            self.img= pygame.image.load(content)
            self.rect = self.img.get_rect()
            self.rect.centerx = pos_x
            self.rect.centery = pos_y
        
        elif sort == "txt":
            self.txt = font.render(content,blanding,txt_color)
            self.rect = self.txt.get_rect()
            self.rect.centerx = pos_x
            self.rect.centery = pos_y
    
    def rebuild(self):
        if self.sort == "img":
            self.img= pygame.image.load(self.content)
            self.rect = self.img.get_rect()
            self.rect.centerx = self.pos_x
            self.rect.centery = self.pos_y
        
        elif self.sort == "txt":
            self.txt = font.render(self.content,self.blanding,self.txt_color)
            self.rect = self.txt.get_rect()
            self.rect.centerx = self.pos_x
            self.rect.centery = self.pos_y

#텍스트 창 클래스
class ScreenTxt:
    def __init__(self,sort = 1,name = "I",txt1_1_content ="Shall I compare thee to a summer's day?" ,txt2_1_content="Shall I compare thee to a summer's day?",txt2_2_content="Shall I compare thee to a summer's day?"):
        self.sort = sort
        self.txt1_1_content = txt1_1_content
        self.txt2_1_content = txt2_1_content
        self.txt2_2_content = txt2_2_content
        self.name = name

        txt0_name = ScreenObject("txt",name,pos_x=215,pos_y=575,txt_color=White) 
        txt1_1 = ScreenObject("txt",txt1_1_content,pos_x=759,pos_y=750,txt_color=White)
        txt2_1 = ScreenObject("txt",txt2_1_content,pos_x=759,pos_y=700,txt_color=White)
        txt2_2 = ScreenObject("txt",txt2_2_content,pos_x=759,pos_y=800,txt_color=White)       
        
        pygame.draw.rect(screen,Gray,(50,550,1518,400))
        pygame.draw.rect(screen,Background,(50,550,1518,400),5)
        pygame.draw.rect(screen,Gray,(65,535,300,80))
        pygame.draw.rect(screen,Background,(65,535,300,80),5)
        
        screen.blit(txt0_name.txt,txt0_name.rect)
        
        if sort == 1:
            screen.blit(txt1_1.txt,txt1_1.rect)
        
        elif sort == 2:
            screen.blit(txt2_1.txt,txt2_1.rect)
            screen.blit(txt2_2.txt,txt2_2.rect)

        screen_update()

#페이드아웃 
def fadeout(width = 1618, height = 1000 ,loop = 120,color = Background): 
    fade = pygame.Surface((width, height))
    fade.fill(color)
    for alpha in range(0, loop):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(10)

#기타 객체
jeonjugo_logo = ScreenObject("img",content="image\guitar\jeonjugo_logo.png",pos_x=809,pos_y=500)

tro_bgm = pygame.mixer.Sound("bgm\main_lobby\AdhesiveWombat - Night Shade.mp3")
tro_bgm.set_volume(0.3)
map_bgm00 = pygame.mixer.Sound("bgm\map\eight_bit.mp3")
map_bgm00.set_volume(0.3)

intro_img01 = ScreenObject("img","image/intro/1.png",pos_x=809,pos_y=500)
intro_img02 = ScreenObject("img","image/intro/2.png",pos_x=809,pos_y=500)
intro_img03 = ScreenObject("img","image/intro/3.png",pos_x=809,pos_y=500)
intro_img04 = ScreenObject("img","image/intro/4.png",pos_x=809,pos_y=500)
intro_img05 = ScreenObject("img","image/intro/5.png",pos_x=809,pos_y=500)
intro_img06 = ScreenObject("img","image/intro/6.png",pos_x=809,pos_y=500)
intro_img07 = ScreenObject("img","image/intro/7.png",pos_x=809,pos_y=500)
intro_img08 = ScreenObject("img","image/intro/8.png",pos_x=809,pos_y=500)
intro_img09 = ScreenObject("img","image/intro/9.png",pos_x=809,pos_y=500)
intro_img010 = ScreenObject("img","image/intro/10.png",pos_x=809,pos_y=500)


#인트로
def intro():
    screen.fill(Background)
    screen.blit(jeonjugo_logo.img,jeonjugo_logo.rect)

    screen_update()
    tro_bgm.play(-1)
    time.sleep(1)
    fadeout(loop = 50,color=Black)

    screen.blit(intro_img01.img,intro_img01.rect)
    screen_update()
    time.sleep(2.3)
    fadeout(color=Black)
    
    screen.blit(intro_img02.img,intro_img02.rect)
    screen_update()
    time.sleep(1)
    fadeout(color=Black,loop = 50)
    
    screen.blit(intro_img03.img,intro_img03.rect)
    screen_update()
    time.sleep(0.4)
    
    screen.blit(intro_img04.img,intro_img04.rect)
    screen_update()
    time.sleep(0.4)
    
    screen.blit(intro_img05.img,intro_img05.rect)
    screen_update()
    time.sleep(0.4)
    fadeout(loop = 50,color=Black)

    screen.blit(intro_img06.img,intro_img06.rect)
    screen_update()
    time.sleep(2.5)
    fadeout(loop = 50,color=Black)

    screen.blit(intro_img07.img,intro_img07.rect)
    screen_update()
    time.sleep(1)
    fadeout(loop = 50,color=Black)

    screen.blit(intro_img08.img,intro_img08.rect)
    screen_update()
    time.sleep(0.5)


    screen.blit(intro_img09.img,intro_img09.rect)
    screen_update()
    time.sleep(0.5)


    screen.blit(intro_img010.img,intro_img010.rect)
    screen_update()
    time.sleep(0.5)
    fadeout(loop = 100,color=(1,127,124))


################
#스테이지 클래스#
################# 
map_size = [[],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
]

# [img,type]
enemy_value_list = [["image/character/enemy_fire.png","fire"],["image/character/enemy_grass.png","dendro"],["image/character/enemy_water.png","water"]]

#tile list
tile_list = ["image/UI/tile01.jpg"]

class Skill:
    def __init__(self,name = None,sort = "attack",type = "fire",value01 = 0,value02 = 0,img = None,txt = "Test"):
        self.name = name
        self.sort = sort
        self.type = type
        self.value01 = value01
        self.value02 = value02
        self.img = ScreenObject(sort = "img", content= img)
        self.txt = txt

        if type== None:
            self.enemy_strong_type=None
            self.enemy_weak_type=None
        
        elif type=="fire":
            self.enemy_strong_type="dendro"
            self.enemy_weak_type="water"

        elif type=="water":
            self.enemy_strong_type="fire"
            self.enemy_weak_type="dendro"

        elif type=="dendro":
            self.enemy_strong_type="water"
            self.enemy_weak_type="fire"

normal_attack = Skill(name = "normal_attack",type= None , img="image/UI/skill/normal_attack.gif")   

blooming = Skill(name = "blooming",type= "dendro" , img="image/UI/skill/blooming.gif")
healing = Skill(name = "healing",type= "dendro" , img="image/UI/skill/healing.gif")
leaf_blade = Skill(name = "leaf blade",type= "dendro" , img="image/UI/skill/leaf_blade.gif")

fire_arrow = Skill(name = "fire arrow",type= "fire" , img="image/UI/skill/fire_arrow.gif")
hell_fire = Skill(name = "hell fire",type= "fire" , img="image/UI/skill/hell_fire.gif")
meteo = Skill(name = "meteo",type= "fire" , img="image/UI/skill/meteo.gif")

tsunami = Skill(name = "tsunami",type= "water" , img="image/UI/skill/tsunami.gif")
water_tornado = Skill(name = "water tornado",type= "water" , img="image/UI/skill/water_tornado.gif")
water_shot = Skill(name = "water shot",type= "water" , img="image/UI/skill/water_shot.png")

skill_list = [normal_attack,blooming,healing,leaf_blade,fire_arrow,hell_fire,meteo,tsunami,water_tornado,water_shot]

class Character:
    def __init__(self,name = "protago",skill01 = "none",skill02 = "none",pos_x = 0,pos_y = 0,img = "image\character\prota.png", hp = 100, type = None) -> None:
        self.name = name
        self.skill_01 = skill01
        self.skill_02 = skill02
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = img
        self.object = ScreenObject(sort="img",content=img)
        self.hp = hp
        self.type = type

    def __del__(self):
        print("deleted")

    def moving(self):
        #print(self.name,self.pos_x,self.pos_y) 
        self.object.pos_x = map_size[self.pos_x][self.pos_y].pos_x + 50
        self.object.pos_y = map_size[self.pos_x][self.pos_y].pos_y + 50
        
        self.object.rebuild()
        screen.blit(self.object.img,self.object.rect)
        screen_update()


class StageSet:
    def __init__(self,mode = "none",size_x = 8,size_y = 10,background = "none") -> None:
        
        self.map_size = map_size
        self.tile_img = ScreenObject("img",content = random.choice(tile_list))
        self.mode = mode
        self.size_x = size_x
        self.size_y = size_y
        self.bakground = background
        
        class MapBlock:
            def __init__(self01,self,name,):
                self01.name = name
                self01.mode = self.mode
                self01.pos_x = name[0]
                self01.pos_y = name[1]
                self01.prese = False

            def build(self01):
                self01.prese = False
                self.tile_img.pos_x = self01.pos_x + 50
                self.tile_img.pos_y = self01.pos_y + 50

                self.tile_img.rebuild()

                screen.blit(self.tile_img.img,self.tile_img.rect)
                pygame.draw.rect(screen,Black,(self01.pos_x,self01.pos_y,100,100),5)

        for i in range(0, self.size_x):
            for j in range(0, size_y):
                self.map_size[i].append(MapBlock(self,name=[i,j]))
                
                self.map_size[i][j].pos_x = 500 + 100*j 

                self.map_size[i][j].pos_y = 100 + 100*i 
    
    def stage_rebuild(self):
        for i in range(0,len(self.map_size)):
            for j in range(0,len(self.map_size[i])):
                self.map_size[i][j].build()



##########################    
class Stage:
    def __init__(self,enemy_count = 5,stage_set_value = ["none",8,10,"none"]):    
        prota_attack_skill01 = random.choice(skill_list)
    
        while True:
            check = random.choice(skill_list)

            if check.name == prota_attack_skill01.name:
                
                continue
            else:
                prota_attack_skill02 = check
                break

        self.stage = 10
        self.prota = Character(skill01 = prota_attack_skill01,skill02=prota_attack_skill02)
        self.stage_set_value = stage_set_value
        self.stage_field = StageSet(mode = stage_set_value[0],size_x = stage_set_value[1],size_y = stage_set_value[2],background = stage_set_value[3])
        self.enemy_count = enemy_count
        self.enemy_list = []
                
        for i in range(1,enemy_count+1):
            enemy_value =  random.choice(enemy_value_list)
            self.enemy_list.append(Character(name="enemy{}".format(i), img=enemy_value[0],type=enemy_value[1]))

            self.enemy_list[i-1].pos_x = random.randint(0,stage_set_value[1]-1)
            self.enemy_list[i-1].pos_y = random.randint(0,stage_set_value[2]-1)
    
    def fight(self):
        check = False
        enemy_list_number = None

        for k in range(0,len(self.enemy_list)):
            if (self.enemy_list[k].pos_x == self.prota.pos_x and self.enemy_list[k].pos_y == self.prota.pos_y):
                enemy_list_number = k 
                check = True
                break
        
        if check == True:
            print(self.enemy_list[k])
            print(self.enemy_list)
            screen.fill(Background)
            print("test")
            screen_update()
            del self.enemy_list[enemy_list_number]
            print(self.enemy_list)
            time.sleep(1)
        
        else:
            return None
    
    def ending_click(self):
                
        End = False
        while not End:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:                   
                    End = True
                    return None
            
                elif event.type == pygame.QUIT:
                    sys.exit()


    def ending(self):
        def ending_txt(content = None):
            ScreenTxt(name = "???",txt1_1_content=content)
            self.ending_click()
            fadeout(loop = 50,color=Black)
        
        map_bgm00.fadeout(3)
        fadeout(color=Black)
        time.sleep(1)

        ending_txt("Oh")
        ending_txt("Unexpected")
        ending_txt("Don't you wonder why you here?")
        ending_txt("\"Who take me here? and for what reason?\"")
        ending_txt("...")
        ending_txt("Before you find the answer")
        ending_txt("You must first get used to this world")
        ending_txt("We will come back when you get ready")


        self.outro()

    def outro(self):
        tro_bgm.play()
        time.sleep(1)
        
        outro_img01 = ScreenObject("img","image/outro/1.png",pos_x=809,pos_y=500)
        outro_img02 = ScreenObject("img","image/outro/2.png",pos_x=809,pos_y=500)
        outro_img03 = ScreenObject("img","image/outro/3.png",pos_x=809,pos_y=500)

        screen.blit(outro_img01.img,outro_img01.rect)
        screen_update()

        time.sleep(2)
        fadeout(loop=120,color=Black)
        
        screen.blit(outro_img02.img,outro_img02.rect)
        screen_update()

        time.sleep(2)
        fadeout(loop=120,color=Black)
        
        screen.blit(outro_img03.img,outro_img03.rect)
        screen_update()

        time.sleep(2)
        fadeout(loop=120,color=Black)

        End = False
        while not End:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def init(self):
        
        End = False

        txt11 = ScreenObject("txt","{}".format(self.prota.skill_01.name),txt_color=Background,pos_y=500)
        txt12 = ScreenObject("txt","Minimum:{}   Maximum:{}   Type:{}".format(self.prota.skill_01.value01,self.prota.skill_01.value02,self.prota.skill_01.type),txt_color=Background,pos_y=600)
        txt13 = ScreenObject("txt","{}".format(self.prota.skill_01.txt),txt_color=Background,pos_y=700)

        self.prota.skill_02.img.pos_x = 1213.5
        self.prota.skill_02.img.rebuild()
        
        txt21 = ScreenObject("txt","{}".format(self.prota.skill_02.name),txt_color=Background,pos_x = self.prota.skill_02.img.pos_x,pos_y=500)
        txt22 = ScreenObject("txt","Minimum:{}   Maximum:{}   Type:{}".format(self.prota.skill_02.value01,self.prota.skill_01.value02,self.prota.skill_02.type),txt_color=Background,pos_x = self.prota.skill_02.img.pos_x,pos_y=600)
        txt23 = ScreenObject("txt","{}".format(self.prota.skill_02.txt),txt_color=Background,pos_x = self.prota.skill_02.img.pos_x,pos_y=700)

        txt00 = ScreenObject("txt","Press Any Key",txt_color=Background,pos_x=809,pos_y=900)

        screen.blit(self.prota.skill_01.img.img,self.prota.skill_01.img.rect)
        screen.blit(self.prota.skill_02.img.img,self.prota.skill_02.img.rect)
        screen.blit(txt11.txt,txt11.rect)
        screen.blit(txt12.txt,txt12.rect)
        screen.blit(txt13.txt,txt13.rect)
        screen.blit(txt21.txt,txt21.rect)
        screen.blit(txt22.txt,txt22.rect)
        screen.blit(txt23.txt,txt23.rect)
        screen.blit(txt00.txt,txt00.rect)

        screen_update()

        while not End:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:                   
                    fadeout(color=Gray)
                    map_bgm00.play(-1)
                    End = True
                
                elif event.type == pygame.QUIT:
                    sys.exit()
        
        self.stage_field.stage_rebuild()
        self.prota.moving()
        pygame.display.update()

        End = False

        while not End:
            screen.fill(Background)
            #pygame.screen.rect(50,50,1000,500)
            if len(self.enemy_list) == 0:
                self.ending()

            if len(self.enemy_list) == 0:
                pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    End = True

                elif event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                    exit = False

                    self.stage_field.stage_rebuild()
                    if event.key == pygame.K_LEFT and self.prota.pos_y > 0:
                        self.prota.pos_y -= 1
                    
                    elif event.key == pygame.K_RIGHT and self.prota.pos_y < self.stage_field.size_y-1:
                        self.prota.pos_y += 1
                    
                    elif event.key == pygame.K_DOWN and self.prota.pos_x < self.stage_field.size_x-1:
                        self.prota.pos_x += 1
                    
                    elif event.key == pygame.K_UP and self.prota.pos_x > 0:
                        self.prota.pos_x -= 1

                    ##
                    else:
                        continue

 
                    self.fight()


                    if exit == True:
                        break

                    for k in self.enemy_list:                       
                        pre_pos_x = k.pos_x
                        pre_pos_y = k.pos_y

                        moving_random_value = random.randint(0,3)
                        #print("{} moving value:{}".format(k.name,moving_random_value))
                        if moving_random_value == 0 and k.pos_y > 0:
                            k.pos_y -= 1
                        
                        elif moving_random_value == 1 and k.pos_y < self.stage_field.size_y-1:
                            k.pos_y += 1
                        
                        elif moving_random_value == 2 and k.pos_x < self.stage_field.size_x-1:
                            k.pos_x += 1
                        
                        elif moving_random_value == 3 and k.pos_x > 0:
                            k.pos_x -= 1

                        for l in self.enemy_list:
                            if (k.name != l.name) and (k.pos_x == l.pos_x and k.pos_x == l.pos_y):
                                    k.pos_x = pre_pos_x
                                    k.pos_y = pre_pos_y

                        k.moving()
                        

                        self.fight()

                    print()
                    self.prota.moving()
