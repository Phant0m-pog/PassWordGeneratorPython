class ProcentInfo():
    def __init__(self):
        self.ProcNum = 0
        self.ProcLet = 0
        self.ProcCaps = 0
        self.SpecialSymbols = 0
        self.PrintTotal()

    def PrintTotal(self):
        print(self.ProcNum,self.ProcLet,self.ProcCaps,self.SpecialSymbols)

    def AcceptProcentRedact(self):
        if self.ProcNum+self.ProcLet+self.ProcCaps+self.SpecialSymbols <= 100:
            return True
        else:
            return False