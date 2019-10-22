def sayHi(username):
    #msg = "Hi %s" % username
    msg = f"Hi {username}"
    return msg

inp = str(input("Enger your username:"))
print(sayHi(inp))
