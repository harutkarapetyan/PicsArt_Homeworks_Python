def binary_search(ls,target):
    start = 0
    end = len(ls)
   
    while start <= end:
        kes = (start + end) // 2

        if ls[kes] == target:
            return kes
        elif ls[kes] < target:
            start = kes + 1
        else:
            end = kes - 1

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

    from function import bubble_sort
    bubble_sort(ls)

    try:
        target = int(input("Write target number "))
        res = binary_search(ls,target)
        if res != -1:
            print("Index =", res)
        else:
            print("Chka")
    except ValueError:
        print("Write integer ")                                      
