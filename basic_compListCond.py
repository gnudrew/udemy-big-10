def foo(myList):
    newList = [
        0 if isinstance(value, str) else value
        for value in myList
        ]
    return newList

data = [1.1, 2.2, 'no data', 4.4, 'no data', 5.5,]
print('Foo input: ', data)
print('Foo output: ', foo(data))