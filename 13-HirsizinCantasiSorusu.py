# 18.03.2019

# br = value/weight

# Bir hirsizin cantasinin kapasitesi 40 br

class item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w


item_1 = item('computer', 200, 20)
item_2 = item('clock', 175, 10)
item_3 = item('painting', 90, 9)
item_4 = item('radio', 20, 4)
item_5 = item('vase', 50, 2)
item_6 = item('book', 10, 1)

item = [item_6, item_5, item_4, item_3, item_2, item_1]
max_para = 0
max_agirlik = 20

for k in range(len(item) - 1, -1, -1):  # Sondan başlayarak her elemanı dener.
    agirlik_test = item[k].weight
    toplam_para = item[k].value
    i = k
    while (
            max_agirlik >= agirlik_test and i >= 0):  # Ağırlığı aşana kadar "k" indisindeki eleman ile kaç para kazanabileceğini hesaplasın.
        b = i - 1
        if (b == 0):
            break
        if (agirlik_test == max_agirlik):
            if (max_para < toplam_para):
                max_para = toplam_para
                break
        elif (agirlik_test < max_agirlik):
            for dene in range(b, -1, -1):
                if (agirlik_test + item[dene].weight > 20):

                    continue

                elif (agirlik_test + item[dene].weight <= 20):
                    agirlik_test += item[dene].weight
                    toplam_para += item[dene].value

            if (max_para < toplam_para):
                max_para = toplam_para
        i -= 1

print(max_para)
