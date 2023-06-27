ls1 = [1, 2, 3, 7]
ls2 = [2, 3, 3, 3, 4 , 8, 9, 11]
ls3 = []


def merg(ls1,ls2):
    i = 0
    j = 0
    while i < len(ls1) and j < len(ls2):
        if ls1[i] > ls2[j]:
            ls3.append(ls2[j])
            j += 1   

        elif ls1[i] < ls2[j]:
            ls3.append(ls1[i])
            i += 1

        elif ls1[i] == ls2[j]:
            ls3.append(ls1[i])
            ls3.append(ls2[j])    
            i += 1
            j += 1
# Հնարավոր է որ առաջին while-ից հետո լինեն էլեմենտներ որոնք դեռ չեն ավելացվել ls3 ի մեջ
# Վերջին 2 while-ը հենց այդ դեպքերի համար է            
    while i < len(ls1):
        ls3.append(ls1[i])
        i += 1

    while j < len(ls2):
        ls3.append(ls2[j])
        j += 1        
        
    print(ls3)  

merg(ls1,ls2)   