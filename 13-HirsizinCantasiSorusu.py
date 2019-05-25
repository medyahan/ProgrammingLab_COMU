# 18.03.2019

# br = value/weight

# Bir hirsizin cantasinin kapasitesi 40 br

class Item(object):
    def __init__(self, n, v, w, br):
        self.name = n
        self.value = v
        self.weight = w
        self.birim = br

def getItems():

    items = []

    items.append(item('Clock', 175, 10, 17.5))
    items.append(item('Painting', 90, 9, 10))
    items.append(item('Radio', 20, 4, 5))
    items.append(item('Vase', 50, 2, 25))
    items.append(item('Book', 10, 1, 10))
    items.append(item('Computer', 200, 20, 10))

    return items

def printItems(items):
    for item in items:
        print(item.name, item.value)

def sortMyItems(items):
    return sorted(items, key = lambda item: item.name, reverse = True)

def test():
    items = getItems()
    printItems(items)
    print("--------- Sorted Items ---------")
    items = sortMyItems(items)
    printItems(items)

def getListForBurglar(items, maxWeight):
    result = []
    totalValue, totalWeight = 0, 0
    for i in range(len(items)):
        if(totalWeight + items[i].weight <= maxWeight):
            result.append(items[i])
            totalWeight = totalWeight + items[i].weight
            totalValue = totalValue + items[i].value
            return (result, totalValue)

def printResult(items2):
    for item1 in item2[0]:
        print(item1.name)
    print(items2[1])

test()
