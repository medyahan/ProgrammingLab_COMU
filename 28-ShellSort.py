# 07.05.2019

# Shell sort ile diziyi sıralama ve karşılaştırma-yer değiştirme sayılarını bulma

import random

def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)

    karsilastirmaSayisi = 0
    yerDegistirmeSayisi = 0

    while(gap >  0):
        for i in range(gap, n):
            karsilastirmaSayisi += 1
            temp = arr[i]
            j = i
            while(j >= gap  and arr[j-gap] > temp):
                karsilastirmaSayisi += 1
                yerDegistirmeSayisi += 1
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr, karsilastirmaSayisi, yerDegistirmeSayisi

def createRandomArray(n):
    arr = []
    for i in range(n):
        x = random.randint(-n, n)
        arr.append(x)
    return arr


arr = createRandomArray(100)

print(shellSort(arr))

