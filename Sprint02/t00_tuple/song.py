def song(verses, chorus):
    j = 0
    my_song = ()
    for i in verses:
        my_song += verses[j] + chorus
        j += 1
    if j == len(verses):
        my_song += chorus
    return my_song
