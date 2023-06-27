def start_swith(a,b):
    ls = a.split()
    if ls[0] == b:
        print(True)
    else:
        print(False)     

a = str(input("Input line = "))
b = str(input("Input a darget string = "))

start_swith(a,b)