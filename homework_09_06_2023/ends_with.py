def ends_with(a,b):
    ls = a.split()
    if b == ls[-1]:
        print(True)
    else:
        print(False)    

a = str(input("Input line = "))
b = str(input("Input a darget string = "))

ends_with(a,b)
