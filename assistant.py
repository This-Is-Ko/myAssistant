from audioReply import getAudioReply
from findGamePrice import findGamePrice
import re

def assistant(commandText):
	# commandText = recordedAudio.split()
	if (re.search("lyrics", commandText)):
		print("LYRICS")
	elif (re.search("define\s\w+", commandText)):
		print("DEFINE")
	elif (re.search("what's\sthe\sweather", commandText)):
		print("WEATHER")
	
	# response = findGamePrice(commandText)
	# getAudioReply(response)

def main():
	recordedAudio = recordAudio()
	# Test input
	# recordedAudio = "what's the weather"
	assistant(recordedAudio)
	


if __name__ == '__main__':
	main()