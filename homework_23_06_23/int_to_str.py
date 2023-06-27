
Unit = {0:"zero", 1:"one", 2:"two",3:"three", 4:"four", 5:"five",6:"six",7:"seven",8:"eight", 9:"nine", 10:"ten",
        11:"eleven",12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}

Tens = {1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety", 11:"eleven", 12:"twelve"}

Hundreds = {1:"hundred", 2:"two hundred", 3:"three hundred", 4:"four hundred", 5:"five hundred", 6:"six hundred", 7:"seven hundred", 8:"eight hundred", 9:"nine hundred"}

'''Ծրագիրը գրված է մինչև 9999 թվերի համար՝ 9999-ը ներառյալ'''

def int_to_str(x):
    l = len(str(x))
    if l == 1:
        print(Unit[x])
    elif l == 2:
        if x in Unit:
            print(Unit[x])
        else:
           a =  x // 10 
           y = x % 10
           print(Tens[a], Unit[y])

    elif l == 3:
        a = x // 100
        y = (x - (a * 100)) // 10
        z = x % 10
        if y == 1:
            print(Hundreds[a],Unit[(y * 10) + z ])
        elif y == 0 and z == 0:
            print(Hundreds[a])          
        elif y == 0:
            print(Hundreds[a],Unit[z])    
        elif  z == 0:
            print(Hundreds[a],Tens[y])  
        elif y == 0 and z == 0:
            print(Hundreds[a])           
        else:
            print(Hundreds[a],Tens[y],Unit[z])    

    elif l == 4:
        a = x // 1000
        y = (x - (a * 1000)) // 100
        z = (x - (a * 1000) - (y * 100)) // 10
        m = x % 10
    
        if z == 1:    
            print(f"{Unit[a]} thousand {Hundreds[y]} {Unit[(z * 10) + m]}")
        elif y == 0 and z == 0 and m == 0:
            print(f"{Unit[a]} thousand")    
        elif m == 0 and z == 0:
            print(f"{Unit[a]} thousand {Hundreds[y]}")  
        elif y == 0 and z == 0:
            print(f"{Unit[a]} thousand {Unit[m]}")    
        elif y == 0 and m == 0:
            print(F"{Unit[a]} thousand {Tens[z]}")    
        elif z == 0:    
            print(f"{Unit[a]} thousand {Hundreds[y]} {Unit[m]}")
        elif m == 0:
            print(f"{Unit[a]} thousand {Hundreds[y]} {Tens[z]} ")
        elif y == 0:
            print(f"{Unit[a]} thousand  {Tens[z]} {Unit[m]}")
        else:
            print(f"{Unit[a]} thousand {Hundreds[y]} {Tens[z]} {Unit[m]}")

try:
    x = int(input("Write number: "))
    int_to_str(x)

except ValueError:
    print("ValueError, write integer")
