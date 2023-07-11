
def binary_search(ls, start, end, n):

    if start <= end:
        kes = (start + end) // 2
        
        if ls[kes] == n:
            return kes
        elif ls[kes] < n:
            return binary_search(ls, kes + 1, end, n)
        elif ls[kes] > n:
            return binary_search(ls, start, kes - 1, n)
    else:
        return -1
    
try:
    size = int(input("Write size "))
except ValueError:
    print("Write integer ") 

else:

    ls = []
    for i in range(size):
        try:
            ls.append(int(input()))
        except ValueError:
            print("Write integer ") 
    ls.sort()

    try:
        n = int(input("Write target number "))
        res = binary_search(ls, 0, len(ls) - 1, n)
        if res != -1:
            print("Index =",res)
        else:
            print("Chka")
    except ValueError:
        print("Write integer ")  

                                 