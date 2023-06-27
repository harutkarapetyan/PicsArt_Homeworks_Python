try:
    x = int(input("x = "))
    y = int(input("y = "))
except ValueError:
        print("Input integer ")
        
def calculator(x,y):

    flag = True
    while flag:

        num = int(input("1 for add, 2 for sub , 3 for mul, 4 for div, 5 for Exit: "))
      
        if num == 1:
            print("result = ",x + y)
        elif num == 2:
            print("result = ",x - y)
        elif num == 3:
            print("result = ",x * y) 
        elif num == 4:
            print("result = ",x / y)
        elif num == 5:
            break
        else:
            print("Invalid value ")                      

calculator(x,y)