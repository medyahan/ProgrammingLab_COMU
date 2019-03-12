# 12.03.2019
# Bozuk para listesi verilsin. En az sayida bozuk para kullanarak musteriye para ustu verme..
# Minimum bozuk para sayisini geri dondurme..
# ParaUstuVermeSorusu nun iyilestirmesi

bozukPara = [1, 5, 10, 25, 50]

para = input("Para Ustu: ")

def paraUstu(liste, a, knownResults):
    min = a
    if a in liste:
        knownResults[a] = 1
        return 1
    elif(knownResults[a]>0):
        return knownResults[a]
    else:
        for i in [c for c in liste if c<=a]:
            sayac = 1 + paraUstu(liste, a-i, knownResults)
            if(sayac<min):
                min = sayac
                knownResults[a] = min
    return min

result = paraUstu(bozukPara, para, [0]*(para+1))
print(result)
