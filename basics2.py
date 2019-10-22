def foo(temp):
    if temp > 7:
        return 'Hot'

    else:
        return 'Cold'

user_input = float(input("Enter some input:"))
feels = foo(user_input)

print(user_input, ' feels ', feels)