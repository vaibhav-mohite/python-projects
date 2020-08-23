import json
from difflib import get_close_matches

data = json.load(open("D:\Python\Applications\Dictionary\data.json", "r"))

def dictionary(word):
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data)) > 0:
        answer = input(f"Did you mean : {get_close_matches(word, data)[0]}. If Yes press 'Y', if NO Press 'N' : ")
        if answer.upper() == "Y":
            return data[get_close_matches(word, data)[0]]
        elif answer.upper() == "N":
            return f"Sorry, the word '{word}' does not exists."
        else:
            return "Please enter a valid input"

    else:
        return f"Sorry, the word {word}' does not exists."


word = input("Please enter a word : ").casefold()
output = dictionary(word)

if type(output) == list:
    for items in output:
        print(items)

else:
    print(output)
