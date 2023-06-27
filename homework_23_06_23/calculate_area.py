import math
p = math.pi

def claculate_area(r):
    result = p * r ** 2
    return result

try:
    r = int(input("Input R: "))
    res = claculate_area(r)
    print("area =",res)
except ValueError:
    print("Invalide value, must enter an integer") 