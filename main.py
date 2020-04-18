'''
To do:
35 add "|FULLSCREEN"
fsize
<<<<<<< HEAD
midi 可用音轨
=======

>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408











'''
<<<<<<< HEAD
import  pygame
=======
import pygame
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408
import time
import mido  # 导入头文件
from settings import *
<<<<<<< HEAD
from pygame.locals import * #导入设置文件
from midireader import  *
=======
from pygame.locals import *  # 导入设置文件
from midireader import *
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408
from Menu import *

# 获取图片库和声音库路径
img_dir = path.join(path.dirname(__file__), 'pic')
sound_folder = path.join(path.dirname(__file__), 'sounds')


font_name = pygame.font.match_font('arial')


sets = Set()
pygame.init()
<<<<<<< HEAD
screen = pygame.display.set_mode((sets.width,sets.height), DOUBLEBUF|HWSURFACE, 32)
pygame.display.set_caption("钢琴助手")
screen.fill(sets.color) #创建窗口，编辑窗口数据
clock=pygame.time.Clock()
=======
screen = pygame.display.set_mode(
    (sets.width, sets.height), DOUBLEBUF | HWSURFACE, 32)
screen.fill(sets.color)  # 创建窗口，编辑窗口数据
clock = pygame.time.Clock()
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408


####加载图片###
track0w_img = pygame.image.load(path.join(img_dir, 'track0w.png')).convert()
track0b_img = pygame.image.load(path.join(img_dir, 'track0b.png')).convert()
track1w_img = pygame.image.load(path.join(img_dir, 'track1w.png')).convert()
track1b_img = pygame.image.load(path.join(img_dir, 'track1b.png')).convert()

keyboard = keyboard_init()  # 加载键盘图库


class Fallingnotes(pygame.sprite.Sprite):
    '''创建掉落音符类'''

    def __init__(self, track, note):
        pygame.sprite.Sprite.__init__(self)
<<<<<<< HEAD
        self.size = (note.long/sets.falling_rate)/speedbyfps 
        self.track=track
        self.tone=note.tone
        self.velo=note.velo
        self.time=note.time
        self.long=note.long
        self.worb=(note.tone%12)
        if track==0:
            if self.worb==0 :
                self.image =track0b_img
            else :
=======
        self.size = (note.long/sets.falling_rate)/speedbyfps
        self.track = track
        self.tone = note.tone
        self.velo = note.velo
        self.time = note.time
        self.long = note.long
        self.worb = (note.tone % 12)
        if track == 0:
            if self.worb == 0:
                self.image = track0b_img
            else:
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408
                self.image = track0w_img
        else:
            if self.worb == 0:
                self.image = track1b_img
            else:
                self.image = track1w_img
<<<<<<< HEAD
        self.image = pygame.transform.scale(self.image,(keyboard[self.tone][0].width,int(self.size)))
        self.rect = self.image.get_rect()
        self.rect.centerx =keyboard[self.tone][0].centerx
        self.rect.bottom = 0
        self.floatbottom = 0
        self.last_update = frame
        

    def update(self):
        now = frame
        self.floatbottom+=(now - self.last_update)/sets.falling_rate
=======
        self.image = pygame.transform.scale(
            self.image, (keyboard[self.tone][0].width, int(self.size)))
        self.rect = self.image.get_rect()
        self.rect.centerx = keyboard[self.tone][0].centerx
        self.rect.bottom = 0
        self.floatbottom = 0
        self.last_update = frame

    def update(self):
        now = frame
        self.floatbottom += (now - self.last_update)/sets.falling_rate
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408
        self.rect.bottom = int(self.floatbottom)
        self.last_update = now
        if self.rect.bottom-self.size > sets.height:
            self.kill()


def fps_control(fps):
    clock.tick(fps)
<<<<<<< HEAD
    getfps=clock.get_fps()
    if getfps+0.5<sets.baseFPS:
        fps+=0.1
    elif getfps-0.5>sets.baseFPS:
        fps-=0.1
    # print(getfps,fps)
    if getfps < 10:
        getfps = 60
    speedbyfps =speedbymidi*24*1.32889*60/getfps
=======
    getfps = clock.get_fps()
    if getfps+0.5 < sets.baseFPS:
        fps += 0.1
    elif getfps-0.5 > sets.baseFPS:
        fps -= 0.1
    # print(getfps,fps)
    if getfps < 10:
        getfps = 60
    speedbyfps = perclick1*1.32889*60/getfps
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408
    return fps


# 加载midi文件
<<<<<<< HEAD
midiname=menu(screen)
=======
midiname = menu(screen)
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408
mid = mido.MidiFile(path.join(sound_folder, midiname))  # 导入音乐mid文件
perclick1=24
n32npb=8
for i, track in enumerate(mid.tracks):
    for msg in track:
        if  msg.is_meta:
            if msg.type=='time_signature':
                perclick1 = msg.clocks_per_click
                n32npb = msg.notated_32nd_notes_per_beat
        #if hasattr(mid.tracks[i][j], 'clocks_per_click'):
        #    perclick1 = (mid.tracks[i][j].clocks_per_click)
speedbymidi=3*n32npb/perclick1
print(speedbymidi)
melodys = readmidi(path.join(sound_folder, midiname))
<<<<<<< HEAD
speedbyfps =speedbymidi*24*1.32889  #越大越快
sets.falling_rate*=1


frame=0
fps=sets.baseFPS
note1=Fallingnotes(0,melodys[0][0])
notegroup=pygame.sprite.Group(note1)
tracksnum=len(melodys)
ononit=[]
unemptytracks=list(range(0,tracksnum))
for i in range(0,tracksnum):
=======
speedbyfps = perclick1*1.32889  # 越大越快


frame = 0
fps = sets.baseFPS
note1 = Fallingnotes(0, melodys[0][0])
notegroup = pygame.sprite.Group(note1)
tracksnum = len(melodys)
ononit = []
unemptytracks = list(range(0, tracksnum))
for i in range(0, tracksnum):
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408
    # ordinal_number_of_notes_in_track
    ononit.append(0)
while True:
    frame += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()
<<<<<<< HEAD
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                exit()
    screen.fill(sets.color)
    
=======
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                exit()
    screen.fill(sets.color)

>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408
    notegroup.update()
    notegroup.draw(screen)
    for i in range(1, 61):
        if keyboard[i][1] == 1:
            pygame.draw.rect(screen, (255, 255, 240), keyboard[i][0], 0)
            pygame.draw.rect(screen, (0, 0, 0), keyboard[i][0], 1)
    for i in range(1, 60):
<<<<<<< HEAD
        if keyboard[i][1] ==0:
            pygame.draw.rect(screen, (0,0,0), keyboard[i][0], 0)
    for i in unemptytracks:
        if melodys[i][ononit[i]].time/speedbyfps <= frame:
            if melodys[i][ononit[i]].tone <= 0:
                ononit[i]+=1
                continue
            newfallingnote=Fallingnotes(i,melodys[i][ononit[i]])
            newfallingnote.add(notegroup)
            if ononit[i] <len(melodys[i])-1: 
                ononit[i]+=1
            else:
                unemptytracks.remove(i)
            #print(ononit[i],i,len(melodys[0]),len(melodys[1]))
=======
        if keyboard[i][1] == 0:
            pygame.draw.rect(screen, (0, 0, 0), keyboard[i][0], 0)
    for i in unemptytracks:
        if melodys[i][ononit[i]].time/speedbyfps <= frame:
            if melodys[i][ononit[i]].tone <= 0:
                ononit[i] += 1
                continue
            newfallingnote = Fallingnotes(i, melodys[i][ononit[i]])
            newfallingnote.add(notegroup)
            if ononit[i] < len(melodys[i])-1:
                ononit[i] += 1
            else:
                unemptytracks.remove(i)
            print(ononit[i], i, len(melodys[0]), len(melodys[1]))
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408


# if melodys[0][0].time<=time.time()-starting:  # +修订值（半个循环时长）+(掉落时间)
    pygame.display.flip()
    clock.tick(fps)
<<<<<<< HEAD
    fps=fps_control(fps)
=======
    fps = fps_control(fps)
>>>>>>> 489a19e46b50d798d8b70e97f604f15b9f1a5408
