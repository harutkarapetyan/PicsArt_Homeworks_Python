num = int(input("Input a number: "))

def find_factorial(num):
   
    if num < 0:
        raise ValueError("Negative number")
    
    result = 1
    if num == 0:
        pass

    while num > 0:
        result *= num
        num -= 1
    return result

try: 
    res = find_factorial(num)
    print(res)
except ValueError as error:
    print(error)






   
# num = int(input("Input a number "))

# def find_factorial(num):
#     if num < 0:
#         raise ValueError("Negative number not allowed")
    
    
#     result = 1

#     if num == 0:
#         pass

#     while num > 0:
#         result *= num
#         num -= 1
#     return result

# try:
#     res = find_factorial(num)
#     print(res)
# except ValueError as error:
#     print("Error:", error)

