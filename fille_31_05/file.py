
file1 = open("reaganomics.txt","r")

string = "Federal income tax and payroll tax levels"

def line_number(file, target_str):
    count = 0
    for line in file:
        count += 1
        if line.strip() == target_str.strip():
            return count  
    
start_count = line_number(file1, string)

file1.close()


file1 = open("reaganomics.txt","r")
file2 = open("dat.txt","w")

full_count = 0
for line in file1:
    full_count += 1


file1.seek(0)
lines = file1.readlines()

section = lines[start_count-1:full_count]

file2.writelines(section)


file1.close()
file2.close()