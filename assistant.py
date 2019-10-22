from audioReply import getAudioReply
from findGamePrice import findGamePrice
from defineWord import define_word
from googleSearch import search_google
import re

def assistant(command_text):
	# command_text = recordedAudio.split()
	response = ""
	if (re.search("lyrics", command_text)):
		print("LYRICS")
	elif (re.search("define", command_text)):
		print("DEFINE")
		response = define_word(command_text)
	elif (re.search("what's\sthe\sweather", command_text)):
		print("WEATHER")
	elif (re.search("google\s+\w+", command_text)):
		print("GOOGLE")
		command_text = remove_first_term(command_text)
		search_google(command_text)
	
	if (response != ""):
		getAudioReply(response)

def main():
	recordedAudio = recordAudio()
	# Test input
	# recordedAudio = "what's the weather"
	assistant(recordedAudio)

def remove_first_term(command_text):
	command_text_array = command_text.split()
	command_text_array.remove(0)
	command_text = " ".join()
	return command_text
	
if __name__ == '__main__':
	main()