from recordAudio import recordAudio
from audioReply import getAudioReply
from findGamePrice import findGamePrice

def main():
	#recordedAudio = recordAudio()
	recordedAudio = "rimworld"
	messageText = recordedAudio.split()
	response = findGamePrice(messageText)
	getAudioReply(response)


if __name__ == '__main__':
	main()