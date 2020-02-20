def sayHi(username):
    #msg = "Hi %s" % username
    msg = f"Hi {username}"
    return msg

inp = str(input("Enter your username:"))
print(sayHi(inp))
