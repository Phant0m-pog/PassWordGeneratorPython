from tkinter import *

class ProcentView():
    def __init__(self,window,canvas,Y,ProcentInfo,type):
        self.ValidationProcent = window.register(self.CheckProcentText)
        self.LblProcent = Label(canvas,bg = "black",fg = "white",font=("Bips",24),text = "Введите проц. соотношение")
        self.LblProcent.place(x=550,y=Y)
        self.EntryProcent = Entry(canvas,font=("Bips",24),width=3,validate="key",validatecommand=(self.ValidationProcent,"%P"))
        self.EntryProcent.place(x=450,y=Y)
        self.TotalProcent = 0
        self.ProcentInfo = ProcentInfo
        self.type = type
    def Destroy(self):
        self.LblProcent.destroy()
        self.EntryProcent.destroy()

    def CheckProcentText(self,symbol):
        if len(symbol) > 2:
            return False
        if symbol == "0":
            if len(self.EntryProcent.get()) == 0:
                return False
        if symbol.isdigit():
            if self.type == "Num":
                Buffer = self.ProcentInfo.ProcNum
                self.ProcentInfo.ProcNum = int(symbol)
                if self.ProcentInfo.AcceptProcentRedact() == False:
                    self.ProcentInfo.ProcNum = Buffer
                    return False
            elif self.type == "Let":
                Buffer = self.ProcentInfo.ProcLet
                self.ProcentInfo.ProcLet = int(symbol)
                if self.ProcentInfo.AcceptProcentRedact() == False:
                    self.ProcentInfo.ProcLet = Buffer
                    return False
            elif self.type == "Caps":
                Buffer = self.ProcentInfo.ProcCaps
                self.ProcentInfo.ProcCaps = int(symbol)
                if self.ProcentInfo.AcceptProcentRedact() == False:
                    self.ProcentInfo.ProcCaps = Buffer
                    return False
            elif self.type == "Symb":
                Buffer = self.ProcentInfo.SpecialSymbols
                self.ProcentInfo.SpecialSymbols = int(symbol)
                if self.ProcentInfo.AcceptProcentRedact() == False:
                    self.ProcentInfo.SpecialSymbols = Buffer
                    return False
        print(self.ProcentInfo.ProcNum,self.ProcentInfo.ProcCaps,self.ProcentInfo.ProcLet,self.ProcentInfo.SpecialSymbols)
        return symbol.isdigit() or symbol == ""

    def FillTotalProcent(self,Proc1,Proc2,Proc3):
        self.TotalProcent = Proc1+Proc2+Proc3