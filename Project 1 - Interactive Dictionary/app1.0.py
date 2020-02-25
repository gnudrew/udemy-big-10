import json
from difflib import get_close_matches as g

def define(word):
    w = word.lower()
    if w in data:
        return(data[w])
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
    print(f"{len(results)} definitions found:")
    for x in results:
        print(x)
else:
    print(results)