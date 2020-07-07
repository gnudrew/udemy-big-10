'''
Try some SQL statements with the instructor's database
'''

import mysql.connector

# connect to remote database
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database",
)

cursor = con.cursor()

#word = input("Enter a word: ")

# q1 = cursor.execute("SELECT * FROM Dictionary WHERE Expression = 'rain'")
# r1 = cursor.fetchall()
# print("1: ", r1)

# q2 = cursor.execute("SELECT * FROM Dictionary WHERE Expression  LIKE 'r%'")
# r2 = cursor.fetchall()
# print("2: ", r2)

# q3 = cursor.execute("SELECT * FROM Dictionary WHERE Expression  LIKE 'rain%'")
# r3 = cursor.fetchall()
# print("3: ", r3)

# q4 = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression) < 4")
# r4 = cursor.fetchall()
# print("4: ", r4)

# q5 = cursor.execute("SELECT * FROM Dictionary WHERE length(Expression) = 4")
# r5 = cursor.fetchall()
# print("5: ", r5)

q6 = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = 'rain'")
r6 = cursor.fetchall()
print("6: ", r6)

print("r6 type is ",type(r6))
print("r6[0] type is ", type(r6[0]))
print("r6[0][0] type is ", type(r6[0][0]))
