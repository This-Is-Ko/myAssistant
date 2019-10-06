import requests
import json

def findGamePrice(message_text):
	game_name = []
	for word in message_text:
		if (word != "@cheapshark"):
			game_name.append(word)
	game_name = " ".join(game_name)
	game_name = game_name.capitalize()
	try:
		#Only return exact game name otherwise no information
		url = "http://www.cheapshark.com/api/1.0/games?title=" + game_name + "&limit=1" + "&exact=1"
		cheapshark_resp = requests.get(url)
		cheapshark_json = cheapshark_resp.json()
		cheapestDealID = cheapshark_json[0]["cheapestDealID"]
		url = "http://www.cheapshark.com/api/1.0/deals?id=" + cheapestDealID
		cheapshark_resp = requests.get(url)
		cheapshark_json = cheapshark_resp.json()
		current_lowest_price = cheapshark_json["cheaperStores"][0]["salePrice"]
		historical_lowest_price = cheapshark_json["cheapestPrice"]["price"]
		if (current_lowest_price == historical_lowest_price):
			response = ("Currently the lowest price for {} is ${}. This is the lowest price to date. :)").format(game_name, current_lowest_price)
		else:
			response = ("Currently the lowest price for {} is ${}. The historic lowest is ${}.").format(game_name, current_lowest_price, historical_lowest_price)
	except:
		try:
			current_price = cheapshark_json["gameInfo"]["salePrice"]
			response = ("{} has never gone on sale with ${} being its current price.").format(game_name, current_price)
		except:
			response = "I couldn't find price information for that game. Check that you spelt the game correctly."
	return response