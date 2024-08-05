#!python3.6

print('Module werden geladen...')
import pygame as p
import random as r
from tkinter import *
import numpy
print('Pong wird gestartet')

Länge = 1000            #Bildschirmabmessungen vor spiel
Breite = 600         

tempo = 3
Balken_Länge = 15
Balken_Höhe = 100
AI_speed = 7
Abstand_Balken_Rand = 5
FPS = 60
Durchmesser_Ball = 25

p.init()
screen = p.display.set_mode((Länge,Breite))
p.display.set_caption('Pong')
p.mouse.set_visible(1)
p.key.set_repeat(15)

WEISS = (255,255,255)
SCHWARZ = (0,0,0)
ROT = (255,0,0)
BLAU = (0,0,255)
GRUEN = (0,255,255)

uhr = p.time.Clock()
x_user = Abstand_Balken_Rand +10
x_AI = Länge - 10 - Abstand_Balken_Rand - Balken_Länge
y_user = Breite/2 -Balken_Höhe/2
y_AI = Breite/2 -Balken_Höhe/2
score_user = 0
score_AI = 0
vorzeichen_x = 1
vorzeichen_y = 1
bx = Länge/2 -Durchmesser_Ball/2
by = Breite/2 -Durchmesser_Ball/2
Random_list = (-1,1)
Random_list_2 = (3,4)
direction_x = float(r.choice(Random_list_2))
direction_y = 7 -direction_x
Zähler = 0

zeit = False
Options = p.image.load('Options_Zeichen_2.bmp')
if Options.get_alpha == None:
    Options.convert_alpha()
Pause = 1
Neue_Variablen_test = False

file = open('VarLog_Pong.txt','r')
check = file.read()
print(check)
file.close()

if not check == '':
    nptxt = numpy.loadtxt('VarLog_Pong.txt')
    print('Variablen gesavet')
    Durchmesser_Ball = nptxt[0]
    Balken_Höhe = nptxt[1]
    Balken_Länge = nptxt[2]
    AI_speed = nptxt[3]
    tempo = nptxt[4]

def Schlussbildschirm():
    text = 'Hallöchen'
    font = p.font.Font(None,100)
    bildschirmtext = font.render(text,screen,WEISS)

def Set_Settings():
    global e1,e2,e3,e4,e5,master,Neue_Variablen_test,Neue_Variablen
    try:
        e_1 = float(e1.get())
        e_2 = float(e2.get())
        e_3 = float(e3.get())
        e_4 = float(e4.get())
        e_5 = float(e5.get())

        print(e_1,e_2,e_3,e_4,e_5)
        Neue_Variablen = (e_1,e_2,e_3,e_4,e_5)
        print(Neue_Variablen)
        Neue_Variablen_test = True
        master.quit()
        master.destroy()

    except ValueError:
        print('Falscher Wert')
        master.quit()
        master.destroy()
        Eingabefeld()

def safe_Settings():
    global Neue_Variablen,e1,e2,e3,e4,e5,master,Neue_Variablen_test
    try:
        e_1 = float(e1.get())
        e_2 = float(e2.get())
        e_3 = float(e3.get())
        e_4 = float(e4.get())
        e_5 = float(e5.get())

        Neue_Variablen = (e_1,e_2,e_3,e_4,e_5)
        Neue_Variablen_safe = ([e_1,e_2,e_3,e_4,e_5])
        Neue_Variablen_test = True
        numpy.savetxt('VarLog_Pong.txt',Neue_Variablen_safe)
        master.quit()
        master.destroy()

    except ValueError:
        print('Falscher Wert')
        master.quit()
        master.destroy()
        Eingabefeld()


def Eingabefeld(start=True):
    global e1,e2,e3,e4,e5,master

    master = Tk()
    master.title('Einstellungen Pong')
    Label(master, text='Ballgrösse').grid(row=0)
    Label(master, text='Balkenlänge').grid(row=1)
    Label(master, text='Balkenbreite').grid(row=2)
    Label(master, text='AI Tempo').grid(row=3)
    Label(master, text='Tempo Ball').grid(row=4)

    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)

    e1.insert(10,str(Durchmesser_Ball))
    e2.insert(10,str(Balken_Höhe))
    e3.insert(10,str(Balken_Länge))
    e4.insert(10,str(AI_speed))
    e5.insert(10,str(tempo))

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
        
    Button(master, text='OK', command=Set_Settings).grid(row=5, column=0, sticky=W, pady=4)
    Button(master, text='Speichern', command=safe_Settings).grid(row=5, column=1, sticky=W, pady=4)
    Button(master, text='Abbrechen', command=master.quit).grid(row=5, column=4, sticky=W, pady=4)
    if not start:
        master.quit()
        master.destroy()    

    master.mainloop()

Eingabefeld(False)

def StartBildschirm():
    font=p.font.SysFont('calibri',70)
    font_2=p.font.SysFont(None,20)
    
    text1=font_2.render('Pong by Jérôme Trachsel',1,WEISS)
    text2=font.render('1 Player',1,WEISS)
    text3=font.render('2 Players',1,WEISS)

    laufzeit = True
    Players_2 = False
    if_quit = True
    Neue_Variablen = ()
    
    while laufzeit:
        uhr.tick(30)
        screen.fill(SCHWARZ)
        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN:
                print(event)
                mx,my = p.mouse.get_pos()
                if Länge/2-100<mx<Länge/2+50 and Breite/2-100<my<Breite/2-25:
                    if event.button == 1:
                        Players_2 = False
                        laufzeit = False

                if Länge/2-100<mx<Länge/2+50 and Breite/2<my<Breite/2+75:       #Der Mauscursour muss noch angepasst werden
                    if event.button == 1:
                        Players_2 = True
                        laufzeit = False

                if 50<mx<100 and Breite-100<my<Breite-50:
                    Eingabefeld()
                    print('eingabe Startbildschirm beendet')
                        
            if event.type == p.KEYDOWN:
                if event.key == p.K_RETURN:
                    laufzeit = False

            if event.type == p.QUIT:
                if_quit = False
                laufzeit = False

        screen.blit(Options,(50,Breite-100))
        screen.blit(text1,(Länge-175,Breite-20))
        screen.blit(text2,(Länge/2 -100,Breite/2 -100))
        screen.blit(text3,(Länge/2 -100,Breite/2))

        p.display.update()

    return Players_2,if_quit

def Hintergrund(score_user, score_AI):
    screen.fill(SCHWARZ)
    screen.blit(B_0,(5,5))
    screen.blit(B_2,(5,5))
    screen.blit(B_3,(Länge/2,5))
    screen.blit(B_4,(Länge-10,5))
    screen.blit(B_5,(5,Breite-10))

    font=p.font.Font(None,30)
    scoretext=font.render(str(score_user),1,WEISS)
    screen.blit(scoretext, (Länge/4, Breite/2))

    font=p.font.Font(None,30)
    scoretext=font.render(str(score_AI),1,WEISS)
    Position_text = (Länge/4)*3
    screen.blit(scoretext, (Position_text, Breite/2))
    
B_0 = p.Surface((5,Breite-10))
B_0 = B_0.convert()
B_0.fill(WEISS)
B_2 = p.Surface((Länge-10,5))
B_2 = B_2.convert()                      #oberer und unterer rand funktionieren nicht
B_2.fill(WEISS)
B_3 = p.Surface((5,Breite-10))
B_3 = B_3.convert()
B_3.fill(WEISS)
B_4 = p.Surface((5,Breite-10))
B_4 = B_4.convert()
B_4.fill(WEISS)
B_5 = p.Surface((Länge-10,5))
B_5 = B_5.convert()
B_5.fill(WEISS)

def Ball(position_Ball,zeit):
    x,y = position_Ball
    screen.blit(circle,(x,y))

D_B = int(Durchmesser_Ball/2)
circ_sur = p.Surface((Durchmesser_Ball,Durchmesser_Ball))
circ = p.draw.circle(circ_sur,(0,255,0),(D_B,D_B),D_B)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))


def Balken_user(position_Balken_user):
    Bildschirm = p.Surface((Balken_Länge,Balken_Höhe))
    x,y = position_Balken_user
    Balken = Bildschirm.convert()
    Balken.fill(BLAU)
    screen.blit(Balken,(x,y))

def Balken_AI(position_Balken_AI):
    Bildschirm = p.Surface((Balken_Länge,Balken_Höhe))
    x,y = position_Balken_AI
    Balken = Bildschirm.convert()
    Balken.fill(ROT)
    screen.blit(Balken,(x,y))
    
speed_hit_AI = Länge -10 -Durchmesser_Ball -Balken_Länge-Abstand_Balken_Rand
speed_hit_user =  10 + Balken_Länge+Abstand_Balken_Rand 
start = True
Players_2,laufzeit = StartBildschirm()
global Neue_Variablen
if Neue_Variablen_test:
    print(Neue_Variablen)
    Durchmesser_Ball,Balken_Höhe,Balken_Länge,AI_speed,tempo = Neue_Variablen

while laufzeit: 
    uhr.tick(FPS)
    Hintergrund(score_user,score_AI)
    Zähler+= 1
    for event in p.event.get():
        
        if event.type == p.QUIT:  
            laufzeit = False

        if event.type == p.MOUSEBUTTONDOWN:
            mx,my = p.mouse.get_pos()
            if 0<mx<Länge and 0<my<Breite:
                Pause*= -1
                
        if event.type == p.KEYDOWN:

            if event.type == p.K_ESCAPE:
                #Funktionniert noch nicht -> reagiert nicht auf Escape-Knopf
                print('zurück zum Menu')
                Players_2,laufzeit = StartBildschirm()
                Zähler = 0
                score_user = 0
                score_AI = 0
                pause = False

            if not Players_2:

                if event.key == p.K_UP:
                    if Pause == 1:
                        y_user-= 10
                        if y_user < 10+Abstand_Balken_Rand:
                            y_user = 10+Abstand_Balken_Rand

                if event.key == p.K_DOWN:
                    if Pause == 1:
                        y_user+= 10
                        if y_user > Breite-Balken_Höhe-10-Abstand_Balken_Rand:
                            y_user = Breite-Balken_Höhe-10-Abstand_Balken_Rand

            if Players_2:

                if event.key == p.K_UP:
                    if Pause == 1:
                        y_AI-= 10
                        if y_AI < 10+Abstand_Balken_Rand:
                            y_AI = 10+Abstand_Balken_Rand

                if event.key == p.K_DOWN:
                    if Pause == 1:
                        y_AI+= 10
                        if y_AI > Breite-Balken_Höhe-10-Abstand_Balken_Rand:
                            y_AI = Breite-Balken_Höhe-10-Abstand_Balken_Rand

                if event.key == p.K_w:
                    if Pause == 1:
                        y_user-= 10
                        if y_user < 10+Abstand_Balken_Rand:
                            y_user = 10+Abstand_Balken_Rand

                if event.key == p.K_s and event.key == p.K_DOWN:
                    if Pause == 1:
                        y_user+= 10
                        if y_user > Breite-Balken_Höhe-10-Abstand_Balken_Rand:
                            y_user = Breite-Balken_Höhe-10-Abstand_Balken_Rand


    if by < 10:
        vorzeichen_y = 1
            
    elif by > Breite-10-Durchmesser_Ball:
        vorzeichen_y = -1
            
    elif bx < speed_hit_user and y_user-Durchmesser_Ball/2<by<y_user+Balken_Höhe:
        vorzeichen_x = 1

    elif bx > speed_hit_AI and y_AI-Durchmesser_Ball/2<by<y_AI+Balken_Höhe:
        vorzeichen_x = -1
            
    elif bx < 10:
        score_AI+= 1
        bx = Länge/2 -Durchmesser_Ball/2
        by = Breite/2 -Durchmesser_Ball/2
        vorzeichen_x = -1
        vorzeichen_y = float(r.choice(Random_list))
        direction_x = float(r.choice(Random_list_2))
        direction_y = 7 -direction_x
        zeit = True
            
    elif bx > Länge-10:
        score_user+= 1
        bx = Länge/2 -Durchmesser_Ball/2
        by = Breite/2 -Durchmesser_Ball/2
        vorzeichen_x = 1
        vorzeichen_y = float(r.choice(Random_list))
        direction_x = float(r.choice(Random_list_2))
        direction_y = 7 -direction_x
        zeit = True

    if zeit:
        if Zähler>1:
            if Zähler == 60:
                zeit = False
    if Pause == 1:
        if zeit == False:
            bx+= vorzeichen_x*direction_x*tempo
            by+= vorzeichen_y*direction_y*tempo
            Zähler = 0
            
    if not Players_2:
        if Pause == 1:
            if bx > Länge/2:
                if by < y_AI+Balken_Höhe/2:
                    y_AI-= AI_speed
                    if y_AI < 10+Abstand_Balken_Rand:
                        y_AI = 10+Abstand_Balken_Rand
                if by > y_AI+Balken_Höhe/2:
                    y_AI+= AI_speed
                    if y_AI > Breite-Balken_Höhe-10- Abstand_Balken_Rand:
                        y_AI = Breite-Balken_Höhe-10 -Abstand_Balken_Rand

    position_Balken_user = (x_user,y_user)
    pos_ball = (bx,by)
    position_Balken_AI = (x_AI,y_AI)
    Ball(pos_ball,zeit)
    Balken_user(position_Balken_user)
    Balken_AI(position_Balken_AI)
    p.display.update() 

p.quit()
