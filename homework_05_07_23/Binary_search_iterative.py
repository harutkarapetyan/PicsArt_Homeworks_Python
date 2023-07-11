
def binary_search(ls, x):
    start = 0
    end = len(ls) - 1

    while start <= end:
        kes = (end + start) // 2
        if ls[kes] == x:
            return kes
        elif ls[kes] < x:
            start = kes + 1   
        else:
            end = kes - 1
    return -1


try:
    size = int(input("Write size: "))
except ValueError:
    print("Write integer") 
else:    
    ls = []   
    for i in range(size):
        try:
            ls.append(int(input()))
        except ValueError:
            print("Input integer")
    ls.sort()

    try:
        x = int(input("Write number "))
    except ValueError:
        print("Write integer")   
    else:
        result = binary_search(ls, x)
        if result != -1:
            print("Index: ", result)
        else:
            print("Chka")
