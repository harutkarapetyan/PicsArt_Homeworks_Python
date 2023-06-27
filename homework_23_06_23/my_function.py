x = 10
def my_function():
    global x
    y = x
    x = 20
    print("static x:",x)
    print("global x:",y)
    x = y

my_function() 

