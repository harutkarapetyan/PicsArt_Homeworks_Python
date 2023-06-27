num = int(input("num = "))

def parz(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True
                
def find_prime_factors(num):
    ls = []
    start = 2

    while start < (num + 1):
        if num % start == 0:
            if parz(start) == True:
                ls.append(start)      
        start += 1
    print(ls) 

find_prime_factors(num)