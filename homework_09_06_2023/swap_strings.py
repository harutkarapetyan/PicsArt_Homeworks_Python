def swap_strings(str1,str2):
    temp = str1
    str1 = str2
    str2 = temp
    print("New_str1 =",str1)
    print("New_str2 =",str2)

str1 = str(input("str1 = "))
str2 = str(input("str2 = "))   

swap_strings(str1,str2)