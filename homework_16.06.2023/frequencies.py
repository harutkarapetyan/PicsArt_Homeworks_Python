text = input("Input a string: ")
text = text.lower()

st = ""
for i in text:
    if ord(i) >= 97 and ord(i) <= 122 or ord(i) == 32:
        st += i

ls = st.split()

dic = {}

for i in ls:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1   

for i, j in dic.items():
    print(f"{i}: {j}")