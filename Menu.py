import pygame
import os
import settings
import random

class Option():
    def __init__(self,text):
        self.text=text
        self.size=0
        self.color=(255,199,38)
        self.surface=None
        self.rect=None
    def resize(self,num,pos,fsize,sets):        #重新确定位置和大小
        if num>=0:
            if num==1:
                self.size=1.5*fsize
                self.color=(255,199,38)
            else:
                self.size=fsize
                self.color=(246,231,97)
        else:
            if num==-2:
                self.size=int(fsize*1.8)
            else:
                self.size=fsize//3
                self.color=None
        self.surface=pygame.font.Font(sets.font,int(self.size)).render(self.text,True,sets.frontcolor,self.color)
        self.surface.set_alpha(255)
        self.rect=self.surface.get_rect()
        if num>=0:
            self.rect.center=pos[num]
        else:
            if num==-2:
                self.rect.center=pos[1]
            else:
                self.rect.center=(sets.width//2,self.size)
class Note():
    def __init__(self,imgs,left,n,sets):
        self.surface=imgs[random.randint(0,len(imgs)-1)]
        self.rect=self.surface.get_rect()
        self.rect.left=left
        self.num=n
        self.rect.top=0
        self.line=sets.height-random.randint(1,5)*20
    def update(self):
        if self.rect.bottom<self.line:
            self.rect.top+=1
            
def menu(screen,start=True):    #start为False,则不播放开场动画
    sets=settings.Set()
    fsize=60
    filelist = os.listdir('sounds')
    namelist=[]
    midilist=[]
    selected=False
    done=0
    selected2=False
    menutext=[]
    noteimg=[pygame.image.load(r'pic\note1.png'),pygame.image.load(r'pic\note2.png')]
    pos=[(sets.width//4,sets.height//2-fsize),(sets.width//2,sets.height//2+fsize//2-10),(3*(sets.width//4),sets.height//2-fsize)]
    cnt=1
    anim=0
    noteimgs=[]
    menutext.append(Option('A、D选择，enter确认'))
    menutext.append(Option('esc取消，enter开始'))
    startbutton=Option(' 开始 ')
    startbutton.resize(1,pos,fsize,sets)

    for i in menutext:
        i.resize(-1,pos,fsize,sets)
    c=True
    move=0

    for i in range(len(filelist)):  #处理文件
        namelist.append(filelist[i][:-4])
        if len(namelist[i])>15:
            namelist[i]=namelist[i][:15]
        midilist.append(Option(namelist[i].center(10)))
    curlist=[-1,0,1]

    if start==True:
        cnt2=1
        for i in range(sets.width//60):
            noteimgs.append(Note(noteimg,i*60,i*200,sets))
        Title=pygame.font.Font(sets.font,80).render('钢琴助手',True,sets.frontcolor)
        while True:
            screen.fill(sets.color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # 接收到退出事件后退出程序
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_RETURN and cnt2==1:
                        cnt2+=1
                        startbutton.resize(-2,pos,fsize,sets)
            if cnt2>1:
                cnt2+=1
                if cnt2==200:
                    start=False
                    cnt=1
                    break
            screen.blit(startbutton.surface,startbutton.rect)
            screen.blit(Title,((sets.width-Title.get_rect().width)//2,100))
            for note in noteimgs:
                if note.num<=cnt:
                    note.update()
                screen.blit(note.surface,note.rect)
            cnt+=1
            for j in range(5):
                pygame.draw.line(screen,(255,255,255),(0,sets.height-(j+1)*20),(sets.width,sets.height-(j+1)*20))

            pygame.display.flip()

    while True:
        screen.fill(sets.color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 接收到退出事件后退出程序
                exit()

            if event.type==pygame.KEYDOWN:
                if anim==0:
                    if event.key==pygame.K_a:
                        move=-1
                        selected=False
                    if event.key==pygame.K_d:
                        move=1
                        selected=False
                    if event.key==pygame.K_ESCAPE:
                        selected=False

                if event.key==pygame.K_RETURN:
                    anim=1
                    if selected==True:
                        selected2=True
                    else:
                        selected=True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_a or event.key==pygame.K_d:
                    move=0
        if move!=0:     #翻页
            if (move==1 and len(midilist)>curlist[2]) or (move==-1 and curlist[0]!=-1):
                c=True
                for i in range(len(curlist)):
                    curlist[i]+=move


        if c==True:       #若发生改变，重新设定
            for i in range(len(curlist)):
                if curlist[i]>-1 and curlist[i]<len(midilist):
                    midilist[curlist[i]].resize(i,pos,fsize,sets)
            c=False
            move=0

        if anim==1:     #动画1部分
            midilist[curlist[1]].resize(-2,pos,fsize,sets)
            cnt+=1
        if cnt==100 and anim==1:        #结束动画
            cnt=1
            anim=0
            midilist[curlist[1]].resize(1,pos,fsize,sets)
        if selected2==True:
            if midilist[curlist[1]].surface.get_alpha!=0:
                midilist[curlist[1]].surface.set_alpha(midilist[curlist[1]].surface.get_alpha()-1)
            done+=1
        for miditag in curlist:         #绘图
            if miditag>-1 and miditag<len(midilist) and curlist.index(miditag)!=1:
                screen.blit(midilist[miditag].surface,midilist[miditag].rect)
        screen.blit(midilist[curlist[1]].surface,midilist[curlist[1]].rect)
        if selected==True:
            screen.blit(menutext[1].surface,menutext[1].rect)
        else:
            screen.blit(menutext[0].surface,menutext[0].rect)

        if done==500:
            return filelist[curlist[1]]
        pygame.display.flip()
