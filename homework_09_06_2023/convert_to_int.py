def convert_to_int(a):
    for i in a:
        if ord(i) in range(48,58):
            print(i,end="")
        else:
            print()
            print("Error") 
            return 
a = str(input("Input string = "))  
convert_to_int(a) 