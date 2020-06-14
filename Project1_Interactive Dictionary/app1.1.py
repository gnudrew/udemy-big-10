import json
from difflib import get_close_matches as g

def define(word):
    w = word.lower() # lowercase version of word
    w2 = w.capitalize() # capitalized version of word for proper nouns, like 'Texas'.
    w3 = w.upper() # upercase version of word for acronymns like 'USA'.
    if w in data or w2 in data or w3 in data:
        if w in data:
            return(data[w])
        elif w2 in data:
            return(data[w2])
        elif w3 in data:
            return(data[w3])
    else:
        close_matches = g(w, data.keys())
        if len(close_matches) > 0:
            test = close_matches[0]
            inp = input(f"Did you mean {test}? (Y/N): ")
            if inp == "Y":
                return data[test]
            elif inp == "N":
                return f"The word {w} does not exist. Please double check it."
            else:
                return "User input not recognized. Exiting..."
        else: 
            return f"The word {w} does not exist. Please double check it."

data = json.load(open("data.json"))
inp = input("Please enter a word: ")
results = define(inp)
if isinstance(results,list):
    # How many defs found
    le = len(results)
    if le == 1:
        print(f"{le} definition found:")
    elif le > 1:
        print(f"{le} definitions found:")
    # Show the defs
    for x in results:
        print(x)
else:
    print(results)