from audioReply import playAudio
from backgroundListener import run_background_assistant

def startAssistant():
	print("Starting assistant")
	playAudio("res\\audio\\system-start-up.mp3")
	run_background_assistant()


if __name__ == '__main__':
	startAssistant()
	