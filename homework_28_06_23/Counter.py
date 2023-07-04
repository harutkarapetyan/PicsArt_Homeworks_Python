
count = 0
def counter():
    def result():
        global count
        count += 1
        return count
    return result

a = counter()

print(a())
print(a())
print(a())