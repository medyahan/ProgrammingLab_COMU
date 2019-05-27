import random

def get_n_random_integer(n):
    # random.seed(100)
    numbers = []
    for i in range(n):
        s = random.randint(-100, 100)
        numbers.append(s)
    return numbers

def get_mean_for_n_integer(numbers):
    toplam = 0
    kactane = 0
    for sayi in numbers:
        toplam = toplam + sayi
        kactane = kactane + 1
    return toplam / kactane

def get_std_for_n_integer(numbers):
    toplam = 0
    kactane = 0
    ortalama = get_mean_for_n_integer(numbers)

    for sayi in numbers:
        toplam = toplam + (sayi - ortalama) ** 2
        kactane = kactane + 1

    var_1 = toplam / (kactane - 1)
    std_1 = var_1 ** 0.5
    return std_1

def normalizasyon(numbers):
    new_numbers = []
    ortalama = get_mean_for_n_integer(numbers)
    standart_sapma = get_std_for_n_integer(numbers)

    for x in numbers:
        new_x = (x - ortalama) / standart_sapma
        new_numbers.append(new_x)

    return new_numbers

def get_mean_of_swap_in_insertion(numTrials, numInt):
    swap_sayilari = []
    for i in range(numTrials):
        sayilar_1 = get_n_random_integer(numInt)
        sayilar_2 = insertion(sayilar_1)
        s_1 = sayilar_2[2]
        swap_sayilari.append(s_1)

    mean_1 = get_mean_for_n_integer(swap_sayilari)
    std_1 = get_std_for_n_integer(swap_sayilari)

    return numInt, int(mean_1), int(std_1)

def get_mean_of_swap_in_bubble(numTrials, numInt):
    swap_sayilari = []
    for i in range(numTrials):
        sayilar_1 = get_n_random_integer(numInt)
        s_1 = bubblesort(sayilar_1)
        swap_sayilari.append(s_1[1])

    mean_1 = get_mean_for_n_integer(swap_sayilari)
    std_1 = get_std_for_n_integer(swap_sayilari)

    return numInt, int(mean_1), int(std_1)

def insertion(numbers):
    sayilar_2 = numbers
    temp = 0
    karsilastirma_sayisi = 0
    yerdegistirme_sayisi = 0
    length_1 = len(sayilar_2)
    #print(sayilar_2)

    for i in range(1, length_1):
        for j in range(i, 0, -1):
            karsilastirma_sayisi += 1

            if (sayilar_2[j] < sayilar_2[j - 1]):
                yerdegistirme_sayisi += 1
                sayilar_2[j - 1] = sayilar_2[j]
                sayilar_2[j] = temp
            else:
                break
        #print(sayilar_2)

    return sayilar_2, karsilastirma_sayisi, yerdegistirme_sayisi

def bubblesort(arr):
    n = len(arr)
    karsilastirma_sayisi = 0
    yerdegistirme_sayisi = 0

    for i in range(n):
        karsilastirma_sayisi += 1
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                yerdegistirme_sayisi += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return karsilastirma_sayisi, yerdegistirme_sayisi

def get_mean_one_std_neigbor_ratio(numbers):
    kactane = 0
    toplamKacSayi = 0
    ortalama = get_mean_for_n_integer(numbers)
    standartd_sapma = get_std_for_n_integer(numbers)

    low = ortalama - standartd_sapma
    high = ortalama + standart_sapma

    for x in numbers:
        toplamKacSayi = toplamKacSayi + 1
        if (x > low and x < high):
            kactane = kactane + 1
    return kactane / toplamKacSayi

sayilar = get_n_random_integer(5)
ortalama = get_mean_for_n_integer(sayilar)
standartsapma = get_std_for_n_integer(sayilar)
yenisayilar = normalizasyon(sayilar)

print("Sayilar: ", sayilar)
print("Ortalama: ", ortalama)
print("Standart Sapma: ", standartsapma)
print("Normalize Edilmis Yeni Sayilar: ", yenisayilar)
