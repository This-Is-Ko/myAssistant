from os import path
import sys
import random
sys.path.append('scripts')

from audioReply import playAudio, getAudioReply
from backgroundListener import run_background_assistant
import profileManager
import settings

def startAssistant():
	print("Starting assistant")
	startup_audio()
	profileManager.init()
	run_background_assistant()

def startup_audio():
	playAudio(path.join(settings.AUDIO_DIR, "system-start-up.mp3"))
	random_clip = str(random.randint(0,3))
	playAudio(path.join(settings.AUDIO_DIR, "system-start-up-voice" + random_clip + ".mp3"))

if __name__ == '__main__':
	startAssistant()
	