x = float(input("Enter hour: " ))
y = float(input("Enter number: Am (1) or Pm (2)? ") )
z = float(input("How many hours ahead? " ))   

def Change(x,y,z):  
    if(x <= 0 or z <= 0 or y <= 0 or x > 12 or y > 2 or y % 1 != 0):
        print("Wrong number") 
        return

    if y == 1:
        if (x + z) < 12:
            print("AM",x + z)   
        elif (x + z) >= 12:
            print("PM",(x + z) - 12)
    if y == 2:
        if (x + z) < 12:
            print("PM", x + z) 
        elif (x + z) > 12:
            print("AM",(x + z) - 12)   
    
Change(x,y,z)

        