import pygame
import os
import settings
import random

class Option():
    def __init__(self,text):
        rainbow=[(255,0,0),(255,127,0),(255,255,0),(0,255,0),(0,255,255) ,(0,0,255),(216,0,255)]
        self.text=text
        self.size=0
        self.color=rainbow[random.randint(0,6)]
        self.surface=None
        self.rect=None
    def resize(self,num,pos,fsize,sets):
        if num==1:
            self.size=2*fsize
        elif num>=0:
            self.size=fsize
        else:
            self.size=40
        self.surface=pygame.font.Font(sets.font,self.size).render(self.text,False,self.color,sets.color)
        self.rect=self.surface.get_rect()
        if num>=0:
            self.rect.center=pos[num]
        else:
            self.rect.center=(sets.width//2,self.size)
def menu(screen):
    sets=settings.Set()
    fsize=120
    filelist = os.listdir('sounds')
    midilist=[]
    selected=False
    pos=[(320,480),(640,300),(960,480)]
    helptext=Option('A、D选择，enter确认')
    helptext.resize(-1,pos,fsize,sets)
    select=Option('esc取消，enter开始')
    select.resize(-1,pos,fsize,sets)
    c=True
    move=0
    for i in range(len(filelist)):
        filelist[i]=filelist[i][:-4]
        if len(filelist[i])>10:
            filelist[i]=filelist[i][:10]
        midilist.append(Option(filelist[i]))
    curlist=[-1,0,1]
    while True:
        screen.fill(sets.color)
        if c==True:
            for i in range(len(curlist)):
                if curlist[i]>-1:
                    midilist[curlist[i]].resize(i,pos,fsize,sets)
            c=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 接收到退出事件后退出程序
                exit()
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    move=-1
                if event.key==pygame.K_d:
                    move=1
                if event.key==pygame.K_RETURN:
                    if selected==True:
                        return midilist[curlist[1]].text+'.mid'
                    else:
                        selected=True
                if event.key==pygame.K_ESCAPE:
                    selected=False
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_a or event.key==pygame.K_d:
                    move=0
        if move!=0:
            if (move==1 and len(midilist)>curlist[2]) or (move==-1 and curlist[0]!=-1):
                c=True
                for i in range(len(curlist)):
                    curlist[i]+=move


        if c==True:       
            for i in range(len(curlist)):
                if curlist[i]>-1 and curlist[i]<len(midilist):
                    midilist[curlist[i]].resize(i,pos,fsize,sets)
            c=False
            move=0
        for miditag in curlist:
            if miditag>-1 and miditag<len(midilist):
                screen.blit(midilist[miditag].surface,midilist[miditag].rect)
        if selected==True:
            screen.blit(select.surface,select.rect)
        else:
            screen.blit(helptext.surface,helptext.rect)
            
        pygame.display.flip()
