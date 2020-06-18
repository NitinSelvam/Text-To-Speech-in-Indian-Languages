import os
import sys

from gtts import gTTS
import playsound

def speech(my_text,language):
	filename = "demo.mp3"
	tts = gTTS(text=my_text, lang=language)
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)