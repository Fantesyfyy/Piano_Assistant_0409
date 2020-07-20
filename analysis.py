from midireader import *
import settings
import os

def purify(file,th_tone=24,th_long=10,ori=480): #不用看
    raw=readmidi(file)
    tpb=read_tpb(file)
    cooked=[]
    for note in raw[0]:
        if note.long<th_long:
            continue
        if abs(note.tone-25)>th_tone:
            #th_long=(note.long+th_long)/1.5
            continue
        note.time*=ori/tpb
        note.long*=ori/tpb
        note.time=int(note.time)
        note.long=int(note.long)
        cooked.append(note)
    return cooked

def w2m():
    os.system('.\waon\waon.exe -i output.wav')
    time.sleep(8)

def compare(melodys,ori=480): #计算分数 ori是原曲的tick_per_beat,可不传参
    w2m()
    ingredient=r'output.mid'
    cooked=purify(ingredient,ori=ori)
    temp=[]
    threshold=50
    for melody in melodys:
        temp.extend(melody)
    temp.sort(key=lambda note: note.time)
    cooked.sort(key=lambda note: note.time)
    cnt=0
    for i,note in enumerate(temp):
        for j,note2 in enumerate(cooked):
            if abs(note2.time-note.time)>threshold:
                continue
            else:
                if note2.tone==note.tone:
                    cnt+=1
                    cooked=cooked[j+1:]
    return ((100-int(cnt/len(temp)*100))//17)*10+int(cnt/len(temp)*100)


