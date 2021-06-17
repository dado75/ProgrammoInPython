import os
from gtts import gTTS
from playsound import playsound

file = input('input name file: ')
try:
    #text = open(file)
    with open(file) as str:
        text = list(str)
except:
    print('File connot be opened:' , file)
    exit()

for pippo in text:
    #pippo = pippo.strip()
    tts = gTTS(text=pippo, lang='it')
    tts.save("audio.mp3")

print("tutto fatto, file salvato!")
playsound('audio.mp3')
