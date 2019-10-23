import contextlib
import sys
import os
import pyaudio
import traceback
import speech_recognition
import settings
from pocketsphinx import DefaultConfig, Decoder, get_model_path, get_data_path

from audioReply import playAudio
from assistant import assistant

TRIGGER_WORD = "edith"
CANCEL = "cancel"

def init():
	# Create a decoder with certain model
	config = DefaultConfig()
	# config.set_string('-logfn', settings.POCKET_LOG)
	config.set_string('-hmm', settings.POCKET_HMM_ACOUSTIC_MODEL)
	config.set_string('-lm', settings.POCKET_LANGUAGE_MODEL)
	config.set_string('-dict', settings.POCKET_DICTIONARY)
	# config.set_string('-kws',   settings.POCKET_KEYPHRASES)

	# Decode streaming data
	global decoder, p
	decoder = Decoder(config)
	p = pyaudio.PyAudio()

	# Set up speech recognition recogniser
	global r
	r = speech_recognition.Recognizer()

def listen_keyword():
	""" Passively listens till trigger word is heard """
	
	global decoder, p
	stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000,
					input=True, frames_per_buffer=1024)
	stream.start_stream()

	print("Passive listening...")
	# Process audio chunk by chunk. On keyword detected perform action and restart search
	decoder.start_utt()
	waiting = False
	wait_count = 0
	while True:
		buf = stream.read(1024, exception_on_overflow=False)
		decoder.process_raw(buf, False, False)
		# Check whether a hypothesis was formed
		if (decoder.hyp()):
			# Check whether trigger word was heard
			if (decoder.hyp().hypstr[:5] == "edith"):
				decoder.end_utt()
				return TRIGGER_WORD
			elif (decoder.hyp().hypstr[:11] == "edith cancel" or decoder.hyp().hypstr[:9] == "edith stop"):
				decoder.end_utt()
				return CANCEL
			else:
				if waiting:
					if wait_count >= 8:
						decoder.end_utt()
						return "failed"
					else:
						wait_count += 1
				else:
					waiting = True


def active_listen():
	"""
	Actively listens for speech
	:return: speech input as a text string
	"""
	global r
	# use the default microphone as the audio source
	with speech_recognition.Microphone() as src:
		# listen for 1 second to adjust energy threshold for ambient noise
		# r.adjust_for_ambient_noise(src)

		print("Active listening... ")
		playAudio("res\\audio\\chimes-notification.mp3")

		# listen for the first phrase and extract it into audio data
		audio = r.listen(src)

	command = ''
	try:
		command = r.recognize_google(audio)  # recognize speech using Google STT
	except speech_recognition.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except speech_recognition.RequestError as e:
		print("Could not request results from Google STT; {0}".format(e))
		print("Perhaps you need to update the 'SpeechRecognition' python package")
	except:
		print("Unknown exception occurred!")
		print(traceback.format_exc())
	finally:
		return command

def run_background_assistant():
	# Start passive listener and when trigger word is heard, start active listener
	init()
	while True:
		trigger = listen_keyword()
		print(trigger)
		if (trigger == TRIGGER_WORD):
			command = active_listen().lower()
			print(command)
			assistant(command)
		elif (trigger == CANCEL):
			continue

if __name__ == '__main__':
	run_background_assistant()
