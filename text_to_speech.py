from gtts import gTTS
import os.path
import time


def get_audio(word: str):
    file_name = r"./sound/" + word + r".mp3"
    if not os.path.isfile(file_name):
        tts = gTTS(word)
        tts.save(file_name)
        print(word)
        time.sleep(1)
