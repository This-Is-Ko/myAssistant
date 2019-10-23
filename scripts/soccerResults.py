import http.client
import json
import re
from wordToNumber import text2int

ladder_trigger_words = ["ladder", "standings", "table"]
position_trigger_words = [""]

#Returns json ladder from football-data.org
def get_ladder():
	connection = http.client.HTTPConnection('api.football-data.org')
	headers = { 'X-Auth-Token': '338ef77c60104da0b4f46ea5fb82d87c' }
	connection.request('GET', '/v2/competitions/PL/standings', None, headers)
	soccer_ladder_json = json.loads(connection.getresponse().read().decode())
	ladder = soccer_ladder_json["standings"][0]["table"]
	return ladder

#Returns partial ladder; used for getting a certain number of teams from top or bottom of the ladder
def part_ladder(upper_bound, lower_bound, points):
	ladder = get_ladder()
	response = ""
	if (point == true):
		ladderString = "{}: {} on {} points.\n"
		for i in range(upper_bound, lower_bound):
			response += ladderString.format(ladder[i]["position"],ladder[i]["team"]["name"], ladder[i]["points"])
	else:
		ladderString = "{}\n"
		for i in range(upper_bound, lower_bound):
			response += ladderString.format(ladder[i]["team"]["name"])
	return response

#Returns minimal formatting of full ladder with position, name and points
def full_ladder():
	ladder = get_ladder()
	response = ""
	for i in range(0, 20):
		ladderString = "{}: {} - {} points.\n"
		response += ladderString.format(ladder[i]["position"],ladder[i]["team"]["name"], ladder[i]["points"])
	return response

#Read regex to work out number of teams wanted to query from top or bottom
def number_teams_wanted(partial_ladder):
	print(partial_ladder)
	partial_ladder = partial_ladder[0].split()
	#Convert word number into int; eg "one" to 1
	bound = text2int(re.findall("\w+", partial_ladder[1])[0])
	return bound

def command_type(command):
	#Top ladder for requests about top; eg "top 4"
	top_ladder = re.findall("top\s+\w+", command)
	#Bottom ladder for requests about bottom; eg "bottom 3"
	bottom_ladder = re.findall("bottom\s+\w+", command)
	if (top_ladder):
		bound = number_teams_wanted(top_ladder)
		print(part_ladder(0, bound))
	elif (bottom_ladder):
		#Assume max 20 for EPL
		bound = number_teams_wanted(bottom_ladder)
		print(part_ladder(20 - bound, 20))

def main():
	command = input("Enter command: ")
	command_type(command)



if __name__ == '__main__':
	main()
