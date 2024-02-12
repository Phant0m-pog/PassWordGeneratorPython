from random import choice,randint

class PassGenerator():
    def __init__(self):
        self.password = ""
        self.Numbers = "1234567890"
        self.Leter = "qwertyuiopasdfghjklzxcvbnm"
        self.CAPSleter = "QWERTYUIOPASDFGHJKLZXCVBNM"
        self.specialSymbol = "!@#$%-^&*()_+\"№;%:?=[]\{}|/,.'<>"
        self.PassLen = 20
        self.Lists = [self.Leter,self.CAPSleter,self.Numbers,self.specialSymbol]
        self.LeterProcent = 35
        self.CAPSleterProcent = 25
        self.NumbersProcent = 30
        self.specialSymbolProcent = 10
        self.BufferList = ""

    def GenBuffer(self):
        self.password = ""
        self.BufferList = ""
        Procents = self.LeterProcent+self.NumbersProcent+self.CAPSleterProcent+self.specialSymbolProcent
        LeterCount = self.PassLen*self.LeterProcent//Procents
        CAPSLeterCount = self.PassLen*self.CAPSleterProcent//Procents
        NumberCount = self.PassLen*self.NumbersProcent//Procents
        SpecialSymbCount = self.PassLen*self.specialSymbolProcent//Procents
        while LeterCount+CAPSLeterCount+NumberCount+SpecialSymbCount < self.PassLen:
            Value = randint(1,4)
            if Value == 1 and NumberCount > 0:
                NumberCount += 1
            if Value == 2 and LeterCount > 0:
                LeterCount += 1
            if Value == 3 and CAPSLeterCount > 0:
                CAPSLeterCount += 1
            if Value == 4 and SpecialSymbCount > 0:
                SpecialSymbCount += 1
        for i in range(LeterCount):
            self.BufferList += "1"
        for i in range(CAPSLeterCount):
            self.BufferList += "2"
        for i in range(NumberCount):
            self.BufferList += "3"
        for i in range(SpecialSymbCount):
            self.BufferList += "4"
        IndexList = []
        RedactedBuffer = ""
        while len(IndexList) != self.PassLen:
            randomIndex = randint(0,self.PassLen-1)
            if randomIndex in IndexList:
                continue
            else:
                IndexList.append(randomIndex)
                RedactedBuffer += self.BufferList[randomIndex]
        for Symbol in RedactedBuffer:
            if Symbol == "1":
                self.password += self.Leter[randint(0,len(self.Leter)-1)]
            elif Symbol == "2":
                self.password += self.CAPSleter[randint(0,len(self.CAPSleter)-1)]
            elif Symbol == "3":
                self.password += self.Numbers[randint(0,len(self.Numbers)-1)]
            elif Symbol == "4":
                self.password += self.specialSymbol[randint(0,len(self.specialSymbol)-1)]
        print(self.password)

    def OneSymbolsType(self,SymbolsList):
        self.password = ""
        for i in range(self.PassLen):
            self.password += SymbolsList[randint(0,len(SymbolsList)-1)]
        print(self.password)

    def TwoSymbolsType(self,SymbolsList1,SymbolList2):
        self.password = ""
        for i in range(self.PassLen):
            IndexList = randint(1,2)
            if IndexList == 1:
                self.password += SymbolsList1[randint(0,len(SymbolsList1)-1)]
            else:
                self.password += SymbolList2[randint(0, len(SymbolList2)-1)]
        print(self.password)

    def ThreeSymbolsType(self,SymbolsList1,SymbolList2,SymbolList3):
        self.password = ""
        for i in range(self.PassLen):
            IndexList = randint(1,3)
            if IndexList == 1:
                self.password += SymbolsList1[randint(0,len(SymbolsList1)-1)]
            elif IndexList == 3:
                self.password += SymbolList3[randint(0,len(SymbolList3)-1)]
            else:
                self.password += SymbolList2[randint(0, len(SymbolList2)-1)]
        print(self.password)

    def SetPassLen(self):
        self.PassLen = int(input("Введите длинну пороля:\n"))

    def HardPass(self):
        self.password = ""
        for i in range(self.PassLen):
            List = choice(self.Lists)
            self.password += List[randint(0,len(List)-1)]
        print(self.password)
