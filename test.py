import mido


mid=mido.MidiFile('Adilina by the water.mid')
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
       # if not msg.is_meta:
            #print(msg.time)
        if (msg.is_meta):
            print(msg)

        