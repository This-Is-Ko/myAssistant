from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def getAudioReply(audioString):
	makeAudioReply(audioString)
	playAudio("temp\\output\\reply.mp3")

def makeAudioReply(audioString):
	print(audioString)
	tts = gTTS(text=audioString, lang='en')
	tts.save("temp\\output\\reply.mp3")

def playAudio(audio_file):
	sound = AudioSegment.from_mp3(audio_file)
	play(sound)

def main():
	getAudioReply("Test")

if __name__ == '__main__':
	main()
