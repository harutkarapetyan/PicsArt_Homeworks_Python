def power_of(n):
    def power(x):
        result = x ** n
        return result
    return power

try:
    x = int(input("x = "))
    n = int(input("n = "))
    res = power_of(n)
    result = res(x)
    print("result =",result)

except ValueError:
    print("Invalid value") 