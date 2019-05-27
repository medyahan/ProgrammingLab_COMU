import random

def get_n_random_integer(n):
    #random.seed(10) # ayni random degerlere ulasmak icin
    numbers = []
    for i in range(n):
        s = random.randint(-10,10)
        numbers.append(s)
    return numbers

def ShellSort(arr):
    n=len(arr)
    gap=n//2
    karsilastirma_sayisi=0
    yerdegistirme_sayisi=0
    while gap > 0 :
        for i in range(gap,n):
            karsilastirma_sayisi+=1
            temp=arr[i]
            j=i

            while j >= gap and arr[j-gap]>temp:
                karsilastirma_sayisi+=1
                yerdegistirme_sayisi+=1
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap//=2
    return karsilastirma_sayisi,yerdegistirme_sayisi

random.seed(42)
arr=get_n_random_integer(100)
print(ShellSort(arr))
