import time
import os
import pandas

while True:
    if os.path.exists("files/fruits.txt"):
        with open("files/fruits.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")

    time.sleep(5)
