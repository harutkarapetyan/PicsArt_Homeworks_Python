n = int(input("n = "))

ls1 = []
print("Input ls1")
for _ in range(n):
    x = int(input(""))
    ls1.append(x)
   

ls2 = []
print("Input ls2")
for _ in range(n):
    y = int(input(""))
    ls2.append(y)
  
ls3 = []

def find_common_elements(ls1,ls2):
    for i in range(n):
        if ls1[i] in ls2:
            ls3.append(ls1[i])  
    return ls3  
     
result = find_common_elements(ls1,ls2)
print("ls3 = ",ls3)