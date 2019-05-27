# 29.04.2019

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
    return toplam/kactane

def get_std_for_n_integer(numbers):
    toplam = 0
    kactane = 0
    ortalama = get_mean_for_n_integer(numbers)

    for sayi in numbers:
        toplam = toplam + (sayi-ortalama)**2
        kactane = kactane + 1
    var1 = toplam / (kactane - 1)
    std1 = var1**0.5
    return std1

def normalizasyon(numbers):
    newNumbers = []
    ortalama = get_mean_for_n_integer(numbers)
    standartSapma = get_std_for_n_integer(numbers)

    for x in numbers:
        newX = (x - ortalama) / standartSapma
        newNumbers.append(newX)

    return newNumbers

sayilar = get_n_random_integer(5)
ortalama = get_mean_for_n_integer(sayilar)
standartSapma = get_std_for_n_integer(sayilar)
yeniSayilar = normalizasyon(sayilar)
print("Sayilar: ", sayilar)
print("Ortalama: ", ortalama)
print("Standart Sapma: ", standartSapma)
print("Yeni Normalize Edilmiş Liste: ", yeniSayilar)

def get_mean_one_std_neighbor_ratio(numbers):
    kacTane = 0
    toplam = 0
    toplamKacSayi = 0

    ortalama = get_mean_for_n_integer(numbers)
    standartSapma = get_std_for_n_integer(numbers)

    low = ortalama - standartSapma
    high = ortalama + standartSapma

    for x in numbers:
        toplamKacSayi = toplamKacSayi + 1
        if(x > low and x < high):
            kacTane = kacTane + 1
    return kacTane / toplamKacSayi

sayilar1 = get_n_random_integer(100)
print(get_mean_one_std_neighbor_ratio(sayilar1))
print(yeniSayilar)
print(get_mean_for_n_integer(yeniSayilar))
print(get_std_for_n_integer(yeniSayilar))

sayilar2 = get_n_random_integer(5)
print(sayilar2)
