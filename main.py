import pygame,random
from sys import exit
W,H = 600,600
FPS=60
Money = 530
t = str('')
MAX_MORALE = 100
CURRENT_MORALE = 100
Economy = 100
year = 1947
Money = 570
Inventions = 0
pygame.display.init()
Next =-1
fill = str('WHITE')
color = (154,0,0)
EXIT = pygame.Rect(1880,0,40,35)
Side = 0
    #0- No side
    #1- USSR
    #2-USA
ON = True  
"""sans serif"""
""" Roboto"""
"""script"""
"""Georgia"""
pygame.font.init()
F = pygame.font.SysFont('Georgia',85)
f = pygame.font.SysFont('Georgia',100)
font = pygame.font.SysFont('Georgia',20)
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((W,H))
class button():
    def __init__(self,x,y,On,color,w,h):
        self.text = str('')
        self.rect = pygame.Rect(x,y,w,h)
        self.on = On
        self.x = x
        self.w = w 
        self.h = h
        self.color = (color)
        self.y =y
    def drawing(self):
        if self.on:
            text = F.render(f'{self.text}',True,(0,0,0))
            pygame.draw.rect(screen,(self.color),self.rect)
            screen.blit(text,(self.x,self.y-5))
def cheking():
    global fill
    if buttun.on:
       buttun.text = "PLAY"
    if buttun.on== False:
        fill = (80,80,80)
def Pickup_side():
    global Side
    USSR_Button.text = 'USSR'
    USA_Button.text = ' USA'
    USA_Button.drawing()
    USSR_Button.drawing()    
def Logo():
    pygame.draw.rect(screen,(180,0,0),LOGO)
    text_LOGO = F.render(f' Cold| Era',True,(0,0,0))
    Logo_year = f.render(str(year),True,(0,0,0))
    pygame.draw.rect(screen,(0,0,150),pygame.Rect(300,0,200,60))
    screen.blit(text_LOGO,(90,-22))
    screen.blit(Logo_year,(200,35))
LOGO = pygame.Rect(100,0,400,60)
buttun = button(168,368,ON,color,250,90)
USSR_Button = button(0,148,ON,(154,0,0),250,90)
NEXT = button(168,290,ON,('GREEN'),250,90)
USA_Button = button(350,148,ON,(0,0,180),250,90)
invention = button(0,180,ON,(100,50,0),60,60)
war = button(200,400,ON,(90,0,0),205,90)
def drawing():
    global Money,Inventions
    Money_text = font.render(f'Money:{Money}',True,(0,0,0))
    Invention_text = font.render(f'Inventions:{Inventions}',True,(0,0,0))
    screen.blit(Money_text,(0,90))
    screen.blit(Invention_text,(0,200))
def mainloop():
    global t,fill,Side,Next,CURRENT_MORALE,MAX_MORALE,Money,Next,year,Inventions,Economy,screen
    CLOCK = pygame.time.Clock()
    
    while True:
        screen.fill((fill))
        morale_bx = pygame.Rect(W-50,120,40,250)
        morale_box = pygame.Rect(W-50,120+(250-(250*(CURRENT_MORALE/MAX_MORALE))),40,250*(CURRENT_MORALE/MAX_MORALE))
        mx,my = pygame.mouse.get_pos()
        cursor = pygame.Rect(mx,my,10,10)
        MILITARY = random.randint(25,35)
        #Exit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((W,H))
                if event.key == pygame.K_f:
                    screen = pygame.display.set_mode()
                if Next >= 0:
                    if event.key == pygame.K_SPACE:
                        Next+=1
                        if Next>0:
                            if Side == 1:
                                if Inventions>Next:
                                    CURRENT_MORALE+=40
                                    Economy+=50
                                if Money<400:
                                    CURRENT_MORALE -= 10
                                if CURRENT_MORALE > 89:
                                    Money+= 50
                                if MILITARY >30:
                                    CURRENT_MORALE -=10
                                    Economy-=10
                                if year <= 1991:
                                    year+=1
                                if Economy >90:
                                    CURRENT_MORALE += 20
                                Money-= MILITARY
                                if CURRENT_MORALE<70:
                                    CURRENT_MORALE-=5
                                Money += (Economy*(CURRENT_MORALE/MAX_MORALE))
                                if CURRENT_MORALE > 100:
                                    CURRENT_MORALE = 100
                                if CURRENT_MORALE<0:
                                    break
                                if Inventions>= Next:
                                    Economy+=20
                            if Side == 2:
                                print(H)
            if event.type == pygame.QUIT:
                exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if EXIT.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                    if buttun.rect.collidepoint(event.pos):
                        buttun.on = False
                    if Side != 2:
                        if USSR_Button.rect.collidepoint(event.pos):
                            USA_Button.on = False
                            USSR_Button.color = 'DARK GREEN'
                            USSR_Button.drawing()
                            Side = 1
                    if Side!=1:
                        if USA_Button.rect.collidepoint(event.pos):
                            USSR_Button.on = False
                            USA_Button.color = 'DARK GREEN'
                            USA_Button.drawing()
                            Side = 2
                    if NEXT.rect.collidepoint(event.pos):
                        NEXT.on = False
                        USA_Button.on = False
                        USSR_Button.on = False
                        Next = 1
                    if invention.rect.collidepoint(event.pos):
                        if Money > 200:
                            Inventions+= 1
                            Money-=200
                        else:
                            print(f'Not enough money')
        cheking()
        if fill == (80,80,80):
            Pickup_side()
        buttun.drawing()
        Logo()
        if USA_Button.on == False:
            NEXT.text = 'NEXT'
            NEXT.drawing()
        elif USSR_Button.on == False:
            NEXT.text = 'NEXT'
            NEXT.drawing()
        if Next>0:
            invention.text = ''
            invention.drawing()
            war.text = 'WAR'
            war.drawing()
            pygame.draw.rect(screen,(0,0,0),morale_bx)
            pygame.draw.rect(screen,(0,200,0),morale_box)
            drawing()
        pygame.draw.rect(screen,(200,0,0),EXIT)
        pygame.draw.rect(screen,(0,0,0),cursor)
        pygame.display.update()
        CLOCK.tick(FPS)

if __name__ == "__main__":
      mainloop()
