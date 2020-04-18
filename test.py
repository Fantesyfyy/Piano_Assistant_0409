import mido


mid=mido.MidiFile('1.mid')
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if not msg.is_meta:
            print(msg.time)

        