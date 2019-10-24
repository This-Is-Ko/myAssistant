# myAssistant

myAssistant is a personal voice assistant with basic functionality and responsiveness to voice commands. Uses [PocketSphinx](https://pypi.org/project/pocketsphinx/) and [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for recognising verbal commands. Ensure micrphone and speaker are working. myAssistant can function without a speaker however some functionality will not work such as voice feedback and notifications when mic is active.

For initial setup, install all requirements listed in requirements.txt
```
pip install -r requirements.txt
```

Run myAssistant
```
python start.py
```
myAssistant will then begin to passively listen and if the trigger word is detected (default: "Edith"), it will begin to actively listen for a command and this will be acted upon.

Potential setup issues
Using pip to install pocketsphinx had issues for me and found the solution [here](https://stackoverflow.com/questions/44504899/installing-pocketsphinx-python-module-command-swig-exe-failed). Download the [binary version](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pocketsphinx) of pocketsphinx and install it.
```
pip install pocketsphinx-0.1.15-cp37-cp37m-win32.whl
```
Likewise PyAudio also had installation issues which was fixed using the same solution.
```
pip install PyAudio-0.2.11-cp37-cp37m-win32.whl
```

Goals: 
- [ ] More functionality and API integration
- [ ] Peronal profile
- [ ] Visual effect when assistant is actively listening
- [ ] Offline usablity
- [ ] GUI for easier personalisation
