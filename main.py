from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError, ID3, TIT2, TPE1, TALB, TDRC, TRCK, TCON, USLT, APIC
import os
from pathlib import Path


target = Path("/home/suman/Documents/git directories/media_renamer/q")

val = []
for item in target.iterdir():

    file_path = item
    # print(item.name)
    tags = ID3(file_path)
    tags["TPE1"] = TPE1(encoding=3, text=item.name)# Artist
    tags["TIT2"] = TIT2(encoding=3, text=item.name)# Title
    tags["TALB"] = TALB(encoding=3, text="TvQuran.com__Maher") #Album
    tags.save(file_path)

    
    # val.append(item.suffix)

# print(len(val))
# file_path = "001 Al-Fatihah(the Opening).mp3"

# audio = MP3("001 Al-Fatihah(the Opening).mp3")
# print(audio.info.length)  # duration in seconds
# print(audio.info.bitrate)  # bitrate in bp
# using the ID3 object
# tags = ID3(file_path)
# tags.add(TIT2(encoding=3, text="001 Al-Fatihah(the Opening)"))
# tags.add(TPE1(encoding=3, text="001 Al-Fatihah(the Opening)"))
# tags.add(TALB(encoding=3, text="001 Al-Fatihah(the Opening)"))
# tags.save()

# tags["TIT2"] = TIT2(encoding=3, text="")# Title
# tags["TPE1"] = TPE1(encoding=3, text="001 Al-Fatihah(the Opening)")# Artist
# tags["TALB"] = TALB(encoding=3, text="")     

# print(tags.get("TIT2"))  # Title
# print(tags.get("TPE1"))  # Artist
# print(tags.get("TALB"))  # Album


# if "TDRC" in tags:
#     year = tags["TDRC"].text[0]
#     print("Year:", year)