from audioReply import getAudioReply
from findGamePrice import findGamePrice
from defineWord import define_word
from googleSearch import search_google
import re
import settings

def assistant(command_text):
	'''
	Main assistant function which searches the command for regex patterns
	and if a match is found, runs the corresponding function then returns a response

	Args:
        command_text (string): Command all in lower-case
	'''
	print("Assistant activated...")
	print("Command: "+ command_text)
	response = ""
	if (re.search("lyrics\s+for\s+", command_text)):
		print("LYRICS function here")
		response = "LYRICS function here"
	elif (re.search("define\s+", command_text)):
		print("DEFINE function here")
		response = define_word(command_text)
	elif (re.search("what's\sthe\sweather", command_text)):
		print("WEATHER function here")
		response = "WEATHER function here"
	elif (re.search("google\s+\w+", command_text)):
		print("GOOGLE function here")
		getAudioReply("I'm on it!")
		command_text = remove_first_term(command_text)
		search_google(command_text)
		response = "Google complete"
	else:
		response = "Unknown request"
	
	if (response != ""):
		getAudioReply(response)

def main():
	# recordedAudio = recordAudio()
	# Test input
	recordedAudio = "google python"
	assistant(recordedAudio)

def remove_first_term(command_text):
	'''
	Removes the first word of the string. Used for specific commands such as "google [something]"

	Args:
        command_text (string): Command all in lower-case

    Returns:
    	string: Input string with first word removed
	'''
	command_text_array = command_text.split(' ', 1)
	command_text = command_text_array[1]
	print(command_text)
	return command_text
	
if __name__ == '__main__':
	main()
