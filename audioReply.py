from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def getAudioReply(audioString):
	makeAudioReply(audioString)
	playAudioReply()

def makeAudioReply(audioString):
	print(audioString)
	tts = gTTS(text=audioString, lang='en')
	tts.save("reply.mp3")

def playAudioReply():
	sound = AudioSegment.from_mp3('reply.mp3')
	play(sound)

def main():
	getAudioReply("Test")

if __name__ == '__main__':
	main()