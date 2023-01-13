from gtts import gTTS
from io import BytesIO
from pygame import mixer
import time


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
# time used to allow speech to run (5 seconds), will refactor
time.sleep(5)
