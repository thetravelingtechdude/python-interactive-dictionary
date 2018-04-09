"""This program takes a word as user input and returns its dictionary meaning as the output if the word exists. It uses a JSON file data.json as the data source of the dictionary."""


import json
from difflib import get_close_matches

data_set = json.load(open("data.json"))

def meaning(word):
    word = word.lower()
    if word in data_set:
        return data_set[word]
    elif len(get_close_matches(word, data_set.keys())) > 0:
        user_input = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data_set.keys())[0])
        if user_input == "Y":
            return data_set[get_close_matches(word, data_set.keys())[0]]
        elif user_input == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
