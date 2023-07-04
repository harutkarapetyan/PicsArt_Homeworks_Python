
ls = [1,3,8,7,6]

def foo(n):
    return n % 2

def filterr(foo,iter):
    for i in iter:
        if foo(i) == False:
            yield i

res = list(filterr(foo,ls))
print(res)   