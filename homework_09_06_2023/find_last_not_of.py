def find_last_not_of(a,b):
    for i in range(len(a)-1,-1,-1):
        if a[i] == b:
            print(i)
            return
        else:
            print(-1)
            return
        
line = str(input("line = "))
darget = str(input("darget = "))               

find_last_not_of(line,darget)