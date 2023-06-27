num = int(input("Input number: "))

def print_pattern(num):
    matrix = [[" "] * num for _ in range(num)]

    for i in range(num):
        for j in range(i + 1):
            matrix[i][j] = j + 1
    return matrix        
            
res = print_pattern(num)

for i in res:
    for j in i:
        print(j,end=" ")
    print()    
        

# def foo(num):
#     ls = []
#     for i in range(1,num + 1):
#         ls.append(str(i))
#         print(" ".join(ls))

# foo(num)