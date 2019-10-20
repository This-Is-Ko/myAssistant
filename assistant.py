from audioReply import getAudioReply
from findGamePrice import findGamePrice
from defineWord import define_word
import re

def assistant(commandText):
	# commandText = recordedAudio.split()
	if (re.search("lyrics", commandText)):
		print("LYRICS")
	elif (re.search("define", commandText)):
		print("DEFINE")
		response = define_word(commandText)
	elif (re.search("what's\sthe\sweather", commandText)):
		print("WEATHER")
	
	getAudioReply(response)

def main():
	recordedAudio = recordAudio()
	# Test input
	# recordedAudio = "what's the weather"
	assistant(recordedAudio)
	


if __name__ == '__main__':
	main()