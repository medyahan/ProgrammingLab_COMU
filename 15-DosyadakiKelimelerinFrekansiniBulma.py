# 25.03.2019

# Dosya okuma

class myClass():
    def __init__(self, myFile = ""):

        # https://www.gutenberg.org/files/1342/1342-0.txt

        f = open("C:/Users/excalıbur/Desktop/deneme.txt", "r")
        myContent = f.read()
        mySentences = myContent.split(".")
        self.myWords = []
        for sentence in mySentences:
            wordsInTheSentence = sentence.split(" ")
            for word1 in wordsInTheSentence:
                self.myWords.append(word1)

        self.myFrequency1()
        self.writeFrequency1()
        self.myFrequency2()
        self.writeFrequency2()

    def myFrequency1(self):
        self.frequencyList1 = {}
        for word in self.myWords:
            if(word in self.frequencyList1):
                self.frequencyList1[word] += 1
            else:
                self.frequencyList1[word] = 1

    def writeFrequency1(self):
        for word1 in self.frequencyList1:
            print(word1 + " " + str(self.frequencyList1[word1]))

    def myFrequency2(self):
        self.frequencyList2 = {}
        for i in range(len(self.myWords)-1):
            w1, w2 = self.myWords[i], self.myWords[i+1]

            if((w1, w2) in self.frequencyList2):
                self.frequencyList2[(w1, w2)] += 1
            else:
                self.frequencyList2[(w1, w2)] = 1

    def writeFrequency2(self):
        for w1 in self.frequencyList2:
            print(str(w1) + " " + str(self.frequencyList2[w1]))

myClass1 = myClass()
print(len(myClass1.myWords))
myClass1.myFrequency1()
myClass1.frequencyList1['truth']

www1, www2 = 'test1', 'test2'
