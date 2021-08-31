#!/usr/local/bin/python3
import os
import sys
import eyed3




filename = os.fsdecode(sys.argv[1])
if os.path.isdir(filename):
    directory = filename
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".mp3"): 
            audio = eyed3.load( directory + "/" + filename)
            #audio.initTag()
            name = filename[:len(filename) - 4]
            name = name.split(" - ")
            print(name)
            if(len(name) == 1):
                audio.tag.title = name[0]
            elif (len(name) == 2):
                audio.tag.title = name[1]
                audio.tag.artist = name[0]
            elif (len(name) == 3):
                audio.tag.title = name[1]
                audio.tag.artist = name[0]
                audio.tag.album = name[2]
            audio.tag.save( directory + "/" + filename)
            continue
        else:
            continue

elif filename.endswith(".mp3"): 
    audio = eyed3.load(sys.argv[1])
    #audio.initTag()
    filename = os.path.basename(filename)
    name = filename[:len(filename) - 4]
    name = name.split(" - ")
    print(name)
    if(len(name) == 1):
        audio.tag.title = name[0]
    elif (len(name) == 2):
        audio.tag.title = name[1]
        audio.tag.artist = name[0]
    elif (len(name) == 3):
        audio.tag.title = name[1]
        audio.tag.artist = name[0]
        audio.tag.album = name[2]
    audio.tag.save(sys.argv[1])
