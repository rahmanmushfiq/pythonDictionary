# Import Library
import json
from difflib import get_close_matches

# Load the json data as python dictionary
data = json.load(open("dictionary.json"))


# data = json.load(open("websters_dictionary_compact.json"))
# data = json.load(open("websters_dictionary_alpha_arrays.json"))
# data = json.load(open("websters_dictionary.json"))


# function for retrieving definition
def retrieve_definition(word):
    # handling case-sensitivity
    word = word.lower()

    # check for non-existing data
    # 1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
    # 2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(
            word, data.keys())[0])
        # in action is yes, retrieve the info of suggested word
        if action == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif action == "n":
            return ("The word doesn't exist yet!")
    else:
        return ("We don't understand your entry! Apologies..")


# taking input from users
user_input = input("Enter a word: ")

# retrieve the definition using function and print the result
output = retrieve_definition(user_input)

# if a word has more than one definition, print them all recursively
if type(output) == list:
    for item in output:
        print("-", item)
    # for words having a single definition, print the output
else:
    print("-", output)
