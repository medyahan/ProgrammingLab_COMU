# 11.03.2019

# Verilen sayının asal çarpanlarını bulma ve asal olup olmadığını belirleme

a = 0
sayi = input("Sayi: ")
for i in range(2, int(sayi)):
    if(int(sayi)%i == 0):
        print(i)
        a+=1
if(a != 0):
    print("Asal sayi degil..")
else:
    print("Asal sayi..")
    
    
    
# Verilen listedeki elemanların ardışık olarak toplamlarından en büyüğünü bulma

liste = [4, -3, 2, -1, -2, 6, -5]

def toplam(liste):
    
    max = liste[0]

    for i in range(len(liste)):
        top = 0
        for j in range(i, len(liste)):
            top = top + liste[j]

            if (top > max):
                max = top
    return max

print(toplam(liste))
