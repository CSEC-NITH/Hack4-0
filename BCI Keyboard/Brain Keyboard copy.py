import pyautogui as py
from graphics import *
from time import sleep
import numpy as np
import cv2

import serial
s=serial.Serial("/dev/cu.usbserial-1430",57600,timeout=1)
threshold=250

def suggestions():
    global t
    tex=[]
    txt_file=open("/Users/uttkarshchaurasia/Desktop/Brain controlled keyboard/wordlist.txt",'r')
    for i in txt_file:
        if t in i[:len(t)]:
            tex.append(i.split()[0])
    txt_file.close()
    jj=0
    y_c=0
    for j in range(21):
        sugg_text[j].undraw()
    print(len(tex))
    for j in range(min(21,len(tex))):
        sugg_text[j]=Text(sugg_rect[j].getCenter(),tex[j])
        sugg_text[j].setTextColor('snow')
        sugg_text[j].draw(win)
        jj=jj+1
        if jj==7:
            jj=0
            y_c=y_c+2
    return tex

def move_suggestions():
    global text_s
    jj=0
    y_c=0
    print(len(text_s))
    global uio
    global t
    global ert
    for j in range(min(21,len(text_s))):
        sugg_rect[j].undraw()
        sugg_rect[j]=Rectangle(Point(jj*(x2-x1)/7+2,y_cor[y_c]),Point((jj+1)*(x2-x1)/7-2,y_cor[y_c+1]))
        sugg_rect[j].setFill("snow")
        sugg_rect[j].setOutline("snow")
        sugg_rect[j].draw(win)
        sugg_text[j]=Text(sugg_rect[j].getCenter(),text_s[j])
        sugg_text[j].setTextColor('grey37')
        sugg_text[j].draw(win)
        thr=False
        tuy=0
        global threshold
        ss=""
        while(1):
            ss=ss+s.read().decode('ascii')
            u=0
            two=0
            if '\n' in ss:
                k=ss.split(" ")
                two=int(ss)
                ss=""
                print(two)
                if(two>threshold):
                    thr=True
                    sugg_rect[j]=Rectangle(Point(jj*(x2-x1)/7+2,y_cor[y_c]),Point((jj+1)*(x2-x1)/7-2,y_cor[y_c+1]))
                    sugg_rect[j].setFill("dodger blue")
                    sugg_rect[j].setOutline("dodger blue")
                    sugg_rect[j].draw(win)
                    sugg_text[j]=Text(sugg_rect[j].getCenter(),text_s[j])
                    sugg_text[j].setTextColor('snow')
                    sugg_text[j].draw(win)
                    sleep(2)
                    break
                else :
                    tuy=tuy+1
                if tuy==3:
                    break
        if(thr):
            t=text_s[j]+" "
            py.typewrite(t)
            t=""
            uio.undraw()
            uio=Text(Point(500,20),t)
            uio.setTextColor("white")
            uio.draw(win)
            ert=False
        sugg_rect[j]=Rectangle(Point(jj*(x2-x1)/7+2,y_cor[y_c]),Point((jj+1)*(x2-x1)/7-2,y_cor[y_c+1]))
        sugg_rect[j].setFill("grey37")
        sugg_rect[j].setOutline("grey37")
        sugg_rect[j].draw(win)
        sugg_text[j]=Text(sugg_rect[j].getCenter(),text_s[j])
        sugg_text[j].setTextColor('snow')
        sugg_text[j].draw(win)
        jj=jj+1
        if jj==7:
            jj=0
            y_c=y_c+2
        if ert==False:
            sleep(1)
            break

def move():
        global text_s
        global t
        global j
        global i
        global ert
        d[j][i]=Rectangle(Point(rows[j][i][0],cols[j][0]),Point(rows[j][i][1],cols[j][1]))
        d[j][i].setFill("snow")
        d[j][i].setOutline("snow")
        d[j][i].draw(win)
        txt[j][i]=Text(d[j][i].getCenter(),buttons[j][i])
        # print(buttons[j][i])
        txt[j][i].setTextColor("grey37")
        txt[j][i].draw(win)
        thr=False
        tuy=0
        ss=""
        global threshold
        while(1):
            ss=ss+s.read().decode('ascii')
            u=0
            two=0
            if '\n' in ss:
                k=ss.split(" ")
                two=int(ss)
                ss=""
                print(two)
                if(two>threshold):
                    d[j][i]=Rectangle(Point(rows[j][i][0],cols[j][0]),Point(rows[j][i][1],cols[j][1]))
                    d[j][i].setFill("dodger blue")
                    d[j][i].setOutline("dodger blue")
                    d[j][i].draw(win)
                    txt[j][i]=Text(d[j][i].getCenter(),buttons[j][i])
                    txt[j][i].setTextColor("snow")
                    txt[j][i].draw(win)
                    txt[j][i].setTextColor("snow")
                    sleep(2)
                    thr=True
                    break
                else :
                    tuy=tuy+1
                if tuy==3:
                    break
        global uio
        rty=False
        if ert==False and thr:
            ert=True
        elif(thr):
            if(buttons[j][i]=='enter'):
                ert=False
                py.typewrite(t+" ")
                t=""
                uio.undraw()
                uio=Text(Point(500,20),t)
                uio.setTextColor("white")
                uio.draw(win)
                print(t)
            elif(buttons[j][i]=='suggest'):
                rty=True
            elif(buttons[j][i]=='backspace'):
                ert=False
                if(len(t)==0):
                    py.press('backspace')
                else:
                    t=t[:-1]
                    uio.undraw()
                    uio=Text(Point(500,20),t)
                    uio.setTextColor("white")
                    uio.draw(win)
                    print(t)
            else:
                ert=False
                t=t+buttons[j][i]
                uio.undraw()
                uio=Text(Point(500,20),t)
                uio.setTextColor("white")
                uio.draw(win)
                print(t)
                text_s=suggestions()
        d[j][i]=Rectangle(Point(rows[j][i][0],cols[j][0]),Point(rows[j][i][1],cols[j][1]))
        d[j][i].setFill("grey37")
        d[j][i].setOutline("grey37")
        d[j][i].draw(win)
        txt[j][i]=Text(d[j][i].getCenter(),buttons[j][i])
        txt[j][i].setTextColor("snow")
        txt[j][i].draw(win)
        txt[j][i].setTextColor("snow")
        if rty:
            move_suggestions()
x1,y1,x2,y2=[35, 132, 1309, 460]
win = GraphWin('Keyboard',x2-x1+1,y2-y1+201)
win.setBackground('grey7')
cols=[[199, 262], [266, 329], [333, 396], [400, 462], [466, 527]]
d=[]
txt=[]
rows=[[[0, 78], [82, 160], [164, 242], [246, 324], [328, 406], [410, 488], [492, 570], [574, 652], [656, 734], [738, 816], [820, 898], [902, 980], [984, 1062], [1066, 1144], [1149, 1273]], [[0, 119], [123, 201], [205, 283], [287, 365], [369, 447], [451, 529], [533, 611], [615, 693], [697, 775], [779, 857], [861, 939], [943, 1021], [1025, 1103], [1107, 1185], [1190, 1273]], [[0, 161], [165, 243], [247, 325], [329, 407], [411, 489], [493, 571], [575, 653], [657, 735], [739, 817], [821, 899], [903, 981], [985, 1063], [1068, 1273]], [[0, 202], [206, 284], [288, 366], [370, 448], [452, 530], [534, 612], [616, 694], [698, 776], [780, 858], [862, 940], [944, 1022], [1026, 1104], [1109, 1273]], [[0, 78], [82, 160], [164, 242], [246, 324], [328, 777], [781, 859], [863, 941], [945, 1023], [1027, 1105], [1109, 1187], [1192, 1273]]]
for j in rows:
    t=[]
    for i in j:
        t.append(1)
    d.append(t) 
    txt.append(t) 
buttons = [['esc','`','1','2','3','4','5','6','7','8','9','0','-','=','backspace'],
			['tab','q','w','e','r','t','y','u','i','o','p','[',']','\\','suggest'],
			['capslk','a','s','d','f','g','h','j','k','l',';',"'","enter"],
			["shift",'z','x','c','v','b','n','m',',','.','/',"up",'suggest'],
			["fn", "ctrl","win",'alt','space','alt','ctrl','left','down','right','suggest']]
for j in range(len(rows)):
    for i in range(len(rows[j])):
        d[j][i]=Rectangle(Point(rows[j][i][0],cols[j][0]),Point(rows[j][i][1],cols[j][1]))
        d[j][i].draw(win)
        d[j][i].setOutline("grey37")
        d[j][i].setFill("grey37")
        txt[j][i]=Text(d[j][i].getCenter(),buttons[j][i])
        txt[j][i].setTextColor("snow")
        txt[j][i].draw(win)

uio=Text(Point(500,20),"")
uio.setTextColor("white")
uio.draw(win)
y_c=0
y_cor=[38,88,92,142,146,194]
sugg_rect=[]
sugg_text=[]
text_s=[]
for j in range(21):
    sugg_rect.append(j)
    sugg_text.append(j)
jj=0
for j in range(21):
    sugg_rect[j]=Rectangle(Point(jj*(x2-x1)/7+2,y_cor[y_c]),Point((jj+1)*(x2-x1)/7-2,y_cor[y_c+1]))
    sugg_rect[j].setFill("grey37")
    sugg_rect[j].setOutline("grey37")
    sugg_rect[j].draw(win)
    sugg_text[j]=Text(sugg_rect[j].getCenter(),"-")
    sugg_text[j].setTextColor('snow')
    sugg_text[j].draw(win)
    jj=jj+1
    if jj==7:
        jj=0
        y_c=y_c+2
t=""
j=0
i=0
main_string=""
while(1):
    j,i=0,0
    ert=False
    while(1):
        j=j+1
        if(j==len(d)):
            j=0
        move()
        if(ert==False):
            continue
        for i in range(len(d[j])):
            move()
        ert=False
        i=0
        

win.close()
