import random

x = random.randint(1,11)
count = 0
Flag = True

while Flag:
    count += 1
    try:
        y = float(input("Mutqagreq tiv(1 ic 10): "))
        
    except ValueError:
        print("Mutqagreq integer ")
 
    if y == x:
        Flag = False
        print(f"Duq haxteciq, sxalvelov {count} angam 🎈🎉")
    elif y > x:
        print("Porceq aveli poqr: ")   
    else:
        print("Porceq aveli mec: ")     