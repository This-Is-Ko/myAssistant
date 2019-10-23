# User Profile Editing
import json
from os import path

PROFILE_LOCATION = "..\\custom"
PROFILE_FILE = path.join(PROFILE_LOCATION, "profile.json")

def load_profile():
	'''
	Load previously saved personal profile from json into dict

    Returns:
    	dict: User profile
	'''
	user_profile = import_profile_from_file(PROFILE_FILE)
	return user_profile

def new_profile():
	'''
	Load default profile from json into dict

    Returns:
    	dict: User profile
	'''
	user_profile = import_profile_from_file(path.join(PROFILE_LOCATION, "defaultProfile.json"))
	return user_profile

def import_profile_from_file(filename):
	'''
	Load profile from json into a dict

	Args:
        filename (string): Filename of a profile json file

    Returns:
    	dict: User profile
	'''
	with open(filename, 'r') as file:
		user_profile = json.load(file)
	return user_profile

def save_profile(user_profile):
	'''
	Saves profile as a json file at default location

	Args:
        user_profile (dict): User profile
	'''
	profile_json = json.dumps(user_profile)
	file = open(PROFILE_FILE,"w")
	file.write(profile_json)
	file.close()

if __name__ == '__main__':
	user_profile = new_profile()
	print(user_profile)
	