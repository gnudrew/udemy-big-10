import mysql.connector
from difflib import get_close_matches

def query(expr):
    cursor.reset()
    cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{expr}'")
    return cursor.fetchall()

def define(word):
    # 3 text formats for query hits: (1) basic words like 'rain', (2) proper nouns like 'Texas', (3) acronyms like 'USA'
    # We'll look in this order, taking the first hit
    w1 = word.lower()
    w2 = word.title()
    w3 = word.upper()

    # query w1
    results = query(w1)
    if results:
        return results
    else:
        # query w2
        results = query(w2)
        if results:
            return results
        else:
            # query w3
            results = query(w3)
            if results:
                return results
            else:
                # No word found -> empty
                return []

# connect to remote database
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database",
)

cursor = con.cursor()

word = input("Enter a word: ")

results = define(word)
if len(results) > 1:
    i = 1
    for result in results:
        print(result[0],str(i)+":",result[1])
        i = i + 1
elif len(results) == 1:
    print(str(results[0][0])+":",results[0][1])

else:
    print("This word not found!")

    # # 11/6/2019, ASR
    # # HEre was my attempt at using get_close_matches methods using SQL database queries. It was slow and not quite working yet.
    # # look for close matches, just on lowercase for now
    
    # cursor.reset()
    # cursor.execute("SELECT * FROM Dictionary")
    # full_table = cursor.fetchall()
    # #print(full_table)
    # close_matches = get_close_matches(word.lower(), full_table, cutoff = 0.78)

    # if close_matches:

    #     while True:
    #         # repeat till correct input format
    #         yn = input(f"Did you mean {close_matches[0]}? Enter y for 'yes' or n for 'no': ")

    #         if yn == 'y':
    #             results = define(close_matches[0])

    #             if len(results) > 1:
    #                 i = 1
    #                 for result in results:
    #                     print(result[0],str(i)+":",result[1])
    #                     i = i + 1

    #             elif len(results) == 1:
    #                 print(str(results[0][0])+":",results[0][1])

    #             break

    #         elif yn == 'n':
    #             print("This word does not exist. Please double check it.")
            
    #             break

    #         else:
    #             print("User input not recognized. Please try again...")

    #             continue
    # else:
    #     print("This word does not exist. Please double check it. Exiting...")
