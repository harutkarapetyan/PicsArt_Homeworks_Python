def rotate_by(arr,x):
    for i in range(x):
        arr.insert(0, arr.pop())

    return arr


message = input("Enter the list: ")
arr = [int(i) for i in message.split()]
x = int(input("Enter a number: "))

print(rotate_by(arr,x))