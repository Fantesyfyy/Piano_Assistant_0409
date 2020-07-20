import pygame
from settings import *
import random
import analysis
def text_objects(text, font):
    textSurface = font.render(text, True, sets.frontcolor)
    return textSurface, textSurface.get_rect()

class textobj():
    def __init__(self,text,size,pos):
        self.surface, self.rect=text_objects(text,(pygame.font.Font(sets.font,size)))
        self.rect.center=(pos)
    def blit(self,screen):
        screen.blit(self.surface,self.rect)
class sparkle():
    def __init__(self,color,start,end):
        self.life=random.randint(1000,5000)
        self.time=1
        self.vx=(end[0]-start[0])/self.life
        self.vy=(end[1]-start[1])/self.life
        self.pos=start
        self.end=end
        self.color=color
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(int(self.pos[0]),int(self.pos[1])),5)
    def move(self):
        if not (self.time>self.life):
            self.time+=1
            self.pos=(self.pos[0]+self.vx,self.pos[1]+self.vy)
            return 1
        else:
            return 0

class firework():
    def __init__(self,sets):
        self.color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.pos=(random.randint(0,sets.width),random.randint(0,sets.height))
        self.tick=0
        self.radius=200
        self.sparkles=[]
        for i in range(100):
            self.sparkles.append(sparkle(self.color,self.pos,
            (self.pos[0]+random.randint(-self.radius,self.radius),
            self.pos[1]+random.randint(-self.radius,self.radius))))

    def move(self):
        if len(self.sparkles)==0:
            return 0
        else:
            for i,spark in enumerate(self.sparkles):
                if spark.move()==0:
                    del self.sparkles[i]
            self.tick+=1
            return 1
    def draw(self,screen):
        for spark in self.sparkles:
            spark.draw(screen)

def cal_score(screen,melodys):
    sets=Set()
    
    #pygame.init()
    #screen = pygame.display.set_mode((sets.width, sets.height), DOUBLEBUF | HWSURFACE, 32)

    textobjs=[]
    score=analysis.compare(melodys)
    textobjs.append(textobj("演奏完成",90,((sets.width/2),(sets.height/2.5))))
    textobjs.append(textobj(f"最终得分:{score}",90,((sets.width/2),(sets.height/2.5)+90)))
    textobjs.append(textobj('按下Esc返回曲目选择',30,((sets.width/2),15)))
    textobjs.append(textobj('已经很优秀了，再注意一下休止符会更好哦(*^_^*)',30,((sets.width/2),(sets.height/2.5)+150)))

    fireworks=[]
    while True:
        screen.fill(sets.color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 接收到退出事件后退出程序
                exit()
        for obj in textobjs:
            obj.blit(screen)
        if len(fireworks)<5:
            fireworks.append(firework(sets))
        for j,fire in enumerate(fireworks):
            if fire.move()==0:
                del fireworks[j]
                continue
            else:
                fire.draw(screen)
        pygame.display.update()