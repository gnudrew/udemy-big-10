 

def sortAndCap(*args):
# assume *args are all strings. 
    newList = []
    length = len(args)

    startList = list(args)
    while True:  #we'll pop args down to empty to build our new list
        # get lowest in current startList
        im_first = 0
        for i in range(len(startList)):
            a = startList[i].lower()
            b = startList[im_first].lower()
            if a < b:
                im_first = i  # a new winner in the current list!

        new = startList.pop(im_first)
        newList.append(new.upper())
        if len(newList) == length:
            break

    return newList

print(sortAndCap("Zedd", "Corbin", "Andrew", "Peter", "Gregg", "Puff"))
# print(sortAndCap(1, 3, 2))

# testList = input("Type a few comma-separated strings to sort and capitalize: ")
# testList = [
#     str(i) 
#     for i in testList
# ]
# print(sortAndCap(testList))
