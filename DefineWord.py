#Function to get definition from Dictionary.com	
def definition_function(message_text):
	if len(message_text) == 1:
		return "No word to define"
	definition_words = ["define", "definition", "mean", "meaning", "mean?", "meaning?", "definition?"]
	if ("mean" in message_text):
		index = 0
		for word in message_text:
			if (word == "mean"):
				word_define = message_text[index - 1]
				break
			index += 1
	for word in message_text:
		if (word in definition_words):
			pass
		else:
			word_define = word
	dictionary = PyDictionary()
	try:
		definition = dictionary.meaning(word_define)
		print_definition = []
		for type, definition_result in definition.items():
			print_definition.append(type + ":")
			for single in definition_result:
				if (len(single) != 1):
					print_definition.append(" " + str(single) + ";\n")
		print_definition = "".join(print_definition)
		response = ("{} means \n{}").format(word_define.capitalize(), print_definition)
		return response
	except:
		return ("I could not define {}. Please check the spelling.").format(word_define)