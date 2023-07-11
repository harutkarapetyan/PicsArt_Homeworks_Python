
def foo(n):
    if n < 0:
        print("Negativ number ")
        return -1
    elif n == 0:
        return 0
    else:
        return n % 10 + foo(n // 10)   
    
try:
    n = int(input("Write number: "))
    print("Sum =",foo(n))
except ValueError:
    print("Write integer ")   