#Python3
from pocketsphinx import get_model_path, get_data_path
from os import path

MODELDIR = 					get_model_path()
DATADIR = 					get_data_path()
LOGS_DIR =     				"logs"
KEYPHRASES_DIR = 			path.join(DATADIR, 'keyphrases')

POCKET_DICTIONARY = 		path.join(MODELDIR, 'en-us/cmudict-en-us.dict')
POCKET_LANGUAGE_MODEL = 	path.join(MODELDIR, 'en-us/en-us.lm.bin')
POCKET_HMM_ACOUSTIC_MODEL = path.join(MODELDIR, 'en-us')

# Not yet implemented
# POCKET_KEYPHRASES = 		path.join(KEYPHRASES_DIR, "keyphrases.txt")
# POCKET_LOG = 				path.join(LOGS_DIR,   'pocketsphinx-listen.log')
