def fib(n):
    '''Calculate the fibonnaci sequence up to or less than n'''
    a, b = 1, 1
    print(a)
    while b < n:
        print(b)
        a, b = b, a + b
        
max = int(input("Enter the max number for fib:"))
fib(max)
