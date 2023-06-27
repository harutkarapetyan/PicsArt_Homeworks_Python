def outer_function(x):
    def inner_function(n):
        return x * n
    return inner_function

try:
    x = int(input("x = "))
    n = int(input("n = "))
    res = outer_function(x)
    result = res(n)
    print("result =",result)
except ValueError as error:
    print("Invalide value",error)