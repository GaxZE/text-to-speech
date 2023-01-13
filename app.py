from gtts import gTTS
from io import BytesIO
from pygame import mixer, time



def speak(text):
    mp3_fp = BytesIO()
    tts = gTTS(text, lang="en")
    tts.write_to_fp(mp3_fp)
    return mp3_fp


text = input("What would you like to say?: \n")
mixer.init()
sound = speak(text)
# Set starting point for file.
sound.seek(0)
# Load sound in mixer.
mixer.music.load(sound, "mp3")
mixer.music.play()
# Lets wait for mixer to finish playing.
while mixer.music.get_busy() == True:
    continue
