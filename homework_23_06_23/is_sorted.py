ls = []
size = int(input("size = "))
print("Input ls")

for i in range(size):
    ls.append(int(input()))

""" sortavorumy stugum e yst achman"""

def is_sorted(ls):
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]:
            print(False)
            break 
    else:
        print(True) 

is_sorted(ls)  