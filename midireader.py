import mido
from settings import *


class Note:
    def __init__(self, tone, velo, time, long):
        self.tone = tone
        self.velo = velo
        self.time = time  # 按下时间
        self.long = long  # 时长


def readmidi(file):
    mid = mido.MidiFile(file)
    melody = []
    melodys = []
    notes = []
    notess = []
    temp = {}
    time = 0
    for track in mid.tracks:
        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                notes.append(msg)
        notess.append(notes)
        notes = []
    for notes in notess:
        for note in notes:
            time += note.time
            try:
                for i in list(temp.keys()):
                    temp[i] = (temp[i][0], temp[i][1] +
                               note.time, temp[note.note][2])
            except:
                pass
            if note.type == 'note_on' and note.velocity != 0:
                temp[note.note] = (time, 0, note.velocity)
            if note.type == 'note_off' or (note.type == 'note_on' and note.velocity == 0):
                melody.append(
                    Note(note.note-35, temp[note.note][2], temp[note.note][0], temp[note.note][1]))
                del temp[note.note]
        melodys.append(melody)
        melody = []
        time = 0
    return melodys
