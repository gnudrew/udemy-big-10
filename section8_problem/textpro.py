def sentify(sometext):
    cap = sometext.capitalize()
    Interrogatives = ("Who", "What", "When", "Where", "Why", "How")
    if cap.startswith(Interrogatives):
        return("%s?" % cap)
    else:
        return("%s." % cap)

# initialize a list of strings to store the data.
sentences = []

# Build the data from user input.
# user enters /end to terminate the input.
while True:
    nextSentence = input("Enter some text:")
    if nextSentence == '/end':
        break
    else:
        sentences.append(sentify(nextSentence))
        continue

# join and print the sentences. 
print(sentences)   
print(' '.join(sentences))

