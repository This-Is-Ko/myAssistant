import time
import speech_recognition as sr
import re
from assistant import assistant

def recordAudio():
	# Record Audio
	r = sr.Recognizer()
	m = sr.Microphone()
	with m as source:
		r.adjust_for_ambient_noise(source)  # Calibrate once before we start listening

	output = ""
	# start listening in the background (note that we don't have to do this inside a `with` statement)
	stop_listening = r.listen_in_background(m, callback)
	# `stop_listening` is now a function that, when called, stops background listening

	# do some unrelated computations for 5 seconds
	for _ in range(50):
		time.sleep(0.1)  # we're still listening even though the main thread is doing other things

	# do some more unrelated things
	while True:
		time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping

def stopListening(stop_listening):
	# calling this function requests that the background listener stop listening
	stop_listening(wait_for_stop=False)

# this is called from the background thread
def callback(recognizer, audio):
	# received audio data, now we'll recognize it using Google Speech Recognition
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`

		# Convert audio to text using Google Speech Recognition
		commandInput = recognizer.recognize_google(audio)
		# Get a match on trigger word; returns array of len 1
		commandAfterTrigger = re.findall("(?<=^Edith).*", commandInput)
		if (commandAfterTrigger):
			print(commandAfterTrigger)
			assistant(commandAfterTrigger[0])
		else:
			print("Failed")
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
	recordAudio()

if __name__ == '__main__':
	main()