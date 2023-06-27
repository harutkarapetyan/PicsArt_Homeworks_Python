def Matrix(old_matrix):

    erk = len(old_matrix)
    layn = len(old_matrix[0])

    new_matrix = [[0] * layn for i in range(erk)]

    for i in range(erk):
        for j in range(layn):
            if old_matrix[i][j] == "M":
                new_matrix[i][j] = "M"
            else:
                count = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        if x == 0 and y == 0:
                            continue
                        new_x = i + x
                        new_y = j + y
                        
                        if 0 <= new_x < erk and 0 <= new_y < layn and old_matrix[new_x][new_y] == "M":
                            count += 1
                new_matrix[i][j] = count
    return new_matrix                        

old_matrix =  [
    [0,'M', 0,'M', 0],
    [0, 0, 'M', 0, 0],
    [0, 0, 0, 0, 0],
    ['M','M', 0, 0, 0],
    [0, 0, 0, 'M', 0]
]            

new = Matrix(old_matrix)
for i in new:
    print(i)



