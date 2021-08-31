import os
import eyed3

directory = os.fsencode("./Spare/")
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".mp3"): 
        audio = eyed3.load("./Spare/" + filename)
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
        audio.tag.save("./Spare/" + filename )
        continue
     else:
        continue
