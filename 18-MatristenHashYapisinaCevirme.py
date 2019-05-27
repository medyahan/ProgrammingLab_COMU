# 02.04.2019

# İstenilen boyutlarda matris oluşturup bu matrisi yazdıran fonksiyonları yazınız.
# Bu matrisi HASH yapısına çevirip yazdıran fonksiyonları yazınız.

import random

def myFunctionCreate(m, n):
    myList = []
    for i in range(m):
        myList.append([])
        for j in range(n):
            s = random.randint(-2,2)
            #s = -1
            myList[i].append(s)
    return myList

def myFunctionPrint(myList):
    m = len(myList)
    n = len(myList[0])
    for i in range(m):
        for j in range(n):
            print(myList[i][j], end=" ")
        print()

def myFunctionConvertToHash(myList):
    myDict  = {}
    m = len(myList)
    n = len(myList[0])
    for i in range(m):
        for j in range(n):
            myDict[(i,j)] = myList[i][j]
            #print(myList[i][j], end=" ")
        #print()
    return myDict

def myFunctionPrintHash(myHashList):
    print("  ")
    for key in myHashList:
        print(myHashList[key], end=" ")


my2dArray = myFunctionCreate(3, 2)
myFunctionPrint(my2dArray)

my2dHash = myFunctionConvertToHash(my2dArray)
myFunctionPrintHash(my2dHash)
