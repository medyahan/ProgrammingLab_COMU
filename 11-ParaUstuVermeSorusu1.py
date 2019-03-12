# Bozuk para listesi verilsin. En az sayida bozuk para kullanarak musteriye para ustu verme..
# Minimum bozuk para sayisini geri dondurme..

bozukPara = [1, 5, 10, 25]

para = input("Para Ustu: ")

def paraUstu(liste,a):
    min = a
    if a in liste:
        return 1
    else:
        for i in [c for c in liste if c<=a]:
            sayac = 1 + paraUstu(liste,a-i)
            if(sayac<min):
                min = sayac
    return min

print(paraUstu(bozukPara,para))
