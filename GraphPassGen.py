from tkinter import *
from ProcentView import ProcentView
from main import PassGenerator
from ProcentInfo import ProcentInfo
import pyperclip
from datetime import datetime

def SaveFile():
    ThisTime = datetime.now()
    FileName = f'{ThisTime.year} {ThisTime.month} {ThisTime.day} {ThisTime.hour} {ThisTime.minute} {ThisTime.second}'
    with open(f'{FileName}.txt',"w") as PasswordFile:
        PasswordFile.write(PassGenerator.password)

def CopyPassword():
    pyperclip.copy(entryPass.get())

def CheckEntryPass(symbol):
    return CopyAccept

def checkText(symbol):
    global ErrorLenPass
    if len(symbol) > 3:
        return False
    if symbol == "0":
        if len(EntryPassLen.get()) == 0:
            return False
    if symbol.isdigit():
        if int(symbol) > 2 and ErrorLenPass is not None:
            ErrorLenPass.destroy()
            ErrorLenPass = None
    return symbol.isdigit() or symbol == ""

def ClickExtraOp():
    global IsExtraOptions,ExtraOptionsNum,ExtraOptionsLeters,ExtraOptionsCaps,ExtraOptionsSymbols
    IsExtraOptions = not IsExtraOptions
    if IsExtraOptions == False:
        ExtraOptions["text"] = "  Extra Options   "
        DestroyExtraOp(True)
    else:
        ExtraOptions["text"] = "Hide Extra Options"
        AddExtraOp()

def DestroyExtraOp(Value):
    global ExtraOptionsNum,ExtraOptionsLeters,ExtraOptionsCaps,ExtraOptionsSymbols
    if IsNum == Value and ExtraOptionsNum is not None:
        ExtraOptionsNum.Destroy()
        ExtraOptionsNum = None
    if IsLeters == Value and ExtraOptionsLeters is not None:
        ExtraOptionsLeters.Destroy()
        ExtraOptionsLeters = None
    if IsCaps == Value and ExtraOptionsCaps is not None:
        ExtraOptionsCaps.Destroy()
        ExtraOptionsCaps = None
    if IsSymvols == Value and ExtraOptionsSymbols is not None:
        ExtraOptionsSymbols.Destroy()
        ExtraOptionsSymbols = None

def AddExtraOp():
    global ExtraOptionsNum,ExtraOptionsLeters,ExtraOptionsCaps,ExtraOptionsSymbols
    if IsNum == True and ExtraOptionsNum is None:
        ExtraOptionsNum = ProcentView(window,canvas, 340,ProcentInfo,"Num")
    if IsLeters == True and ExtraOptionsLeters is None:
        ExtraOptionsLeters = ProcentView(window,canvas, 500,ProcentInfo,"Let")
    if IsCaps == True and ExtraOptionsCaps is None:
        ExtraOptionsCaps = ProcentView(window, canvas, 420, ProcentInfo, "Caps")
    if IsSymvols == True and ExtraOptionsSymbols is None:
        ExtraOptionsSymbols = ProcentView(window,canvas, 580,ProcentInfo,"Symb")


def RedactChekMark(CheckMark,canvas,IsValue):
    if IsValue == True:
        canvas.itemconfigure(CheckMark, image=Galochka)
        if IsExtraOptions:
            AddExtraOp()
    else:
        canvas.itemconfigure(CheckMark, image=WhiteGalochka)
        if IsExtraOptions:
            DestroyExtraOp(False)


def ClickChekMark(CheckMark,canvas,Value):
    global IsNum,IsLeters,IsCaps,IsSymvols
    if Value == 1:
        IsNum = not IsNum
        ProcentInfo.ProcNum = 0
        RedactChekMark(CheckMark, canvas, IsNum)
    elif Value == 2:
        IsLeters = not IsLeters
        ProcentInfo.ProcLet = 0
        RedactChekMark(CheckMark, canvas, IsLeters)
    elif Value == 3:
        IsCaps = not IsCaps
        ProcentInfo.ProcCaps = 0
        RedactChekMark(CheckMark, canvas, IsCaps)
    elif Value == 4:
        IsSymvols = not IsSymvols
        ProcentInfo.SpecialSymbols = 0
        RedactChekMark(CheckMark,canvas,IsSymvols)

def SubmitPass(event):
    global ErrorLenPass,CopyAccept

    if len(EntryPassLen.get()) == 0 or int(EntryPassLen.get()) < 3:
        ErrorLenPass = Label(canvas,text="Пороль может состоять из 3 и более символов",font=("Bips",22),bg = "black",fg="firebrick")
        ErrorLenPass.place(x = 160,y = 630)
        return
    PassGenerator.PassLen = int(EntryPassLen.get())
    Types = []
    if IsNum:
        Types.append(PassGenerator.Numbers)
    if IsLeters:
        Types.append(PassGenerator.Leter)
    if IsCaps:
        Types.append(PassGenerator.CAPSleter)
    if IsSymvols:
        Types.append(PassGenerator.specialSymbol)
    if IsExtraOptions == False:
        if len(Types) == 1:
            PassGenerator.OneSymbolsType(Types[0])
        if len(Types) == 2:
            PassGenerator.TwoSymbolsType(Types[0], Types[1])
        if len(Types) == 3:
            PassGenerator.ThreeSymbolsType(Types[0], Types[1], Types[2])
        if len(Types) == 4:
            PassGenerator.HardPass()
    else:
        if IsNum == False:
            PassGenerator.NumbersProcent = 0
        else:
            if len(ExtraOptionsNum.EntryProcent.get()) == 0:
                PassGenerator.NumbersProcent = 0
            else:
                PassGenerator.NumbersProcent = int(ExtraOptionsNum.EntryProcent.get())
        if IsLeters == False:
            PassGenerator.LeterProcent = 0
        else:
            if len(ExtraOptionsLeters.EntryProcent.get()) == 0:
                PassGenerator.LeterProcent = 0
            else:
                PassGenerator.LeterProcent = int(ExtraOptionsLeters.EntryProcent.get())
        if IsCaps == False:
            PassGenerator.CAPSleterProcent = 0
        else:
            if len(ExtraOptionsCaps.EntryProcent.get()) == 0:
                PassGenerator.CAPSleterProcent = 0
            else:
                PassGenerator.CAPSleterProcent = int(ExtraOptionsCaps.EntryProcent.get())
        if IsSymvols == False:
            PassGenerator.specialSymbolProcent = 0
        else:
            if len(ExtraOptionsSymbols.EntryProcent.get()) == 0:
                PassGenerator.specialSymbolProcent = 0
            else:
                PassGenerator.specialSymbolProcent = int(ExtraOptionsSymbols.EntryProcent.get())
        PassGenerator.GenBuffer()
    CopyAccept = True
    entryPass.delete(0, END)
    entryPass.insert(0, PassGenerator.password)
    CopyAccept = False

CopyAccept = False
ProcentInfo = ProcentInfo()
PassGenerator = PassGenerator()
IsLeters = True
IsCaps = True
IsSymvols = True
IsNum = True
window = Tk()
canvas = Canvas(window,height=700,width = 1000,bg = "black")
canvas.pack()
window.geometry("1000x700+450+200")
window.title("Генератор паролей")
window.resizable(0,0)
ValidationEntryPass = window.register(CheckEntryPass)
canvas.create_text(300,20,text = "Генератор паролей",fill="white",font=("Bips",30),anchor=NW)
entryPass = Entry(canvas,font=("Bips",24),width=24,validate="key",validatecommand=(ValidationEntryPass,"%P"))
entryPass.place(x=230,y=100)
CanvasSubmit = Canvas(canvas,bg = "black",height=66,width=211,highlightthickness=0)
CanvasSubmit.place(x=370,y=170)
Submit = PhotoImage(file = "SubmitButton.png")
ImgSubmit = CanvasSubmit.create_image(0,0,anchor = NW,image = Submit)
CanvasSubmit.tag_bind(ImgSubmit,"<Button-1>",SubmitPass)
canvas.create_text(15,265,text = "Длинна пороля",fill="white",font=("Bips",24),anchor=NW)
Validation = window.register(checkText)
EntryPassLen = Entry(canvas,font=("Bips",24),width=3,validate="key",validatecommand=(Validation,"%P"))
EntryPassLen.place(x=280,y=265)
canvas.create_text(80,340,text = "Числа",fill="white",font=("Bips",24),anchor=NW)
CanvasNumbers = Canvas(canvas,bg = "white",height=50,width=66,highlightthickness=0)
CanvasNumbers.place(x=280,y=340)
Galochka = PhotoImage(file = "zelenaja-galochka.png")
WhiteGalochka = PhotoImage(file = "white.png")
ImgGalochkaNumbers = CanvasNumbers.create_image(10,3,anchor = NW,image = Galochka)
CanvasNumbers.tag_bind(ImgGalochkaNumbers,"<Button-1>",lambda event:ClickChekMark(ImgGalochkaNumbers,CanvasNumbers,1))
canvas.create_text(15,420,text = "Верхний регистр",fill="white",font=("Bips",24),anchor=NW)
CanvasCAPSLeters = Canvas(canvas,bg = "white",height=50,width=66,highlightthickness=0)
CanvasCAPSLeters.place(x=280,y=420)
ImgGalochkaCAPSLeters = CanvasCAPSLeters.create_image(10,3,anchor = NW,image = Galochka)
canvas.create_text(15,500,text = "Нижний регистр",fill="white",font=("Bips",24),anchor=NW)
CanvasLeters = Canvas(canvas,bg = "white",height=50,width=66,highlightthickness=0)
CanvasLeters.place(x=280,y=500)
ImgGalochkaLeters = CanvasLeters.create_image(10,3,anchor = NW,image = Galochka)
canvas.create_text(15,580,text = "Спец. символы",fill="white",font=("Bips",24),anchor=NW)
CanvaSymvols = Canvas(canvas,bg = "white",height=50,width=66,highlightthickness=0)
CanvaSymvols.place(x=280,y=580)
ErrorLenPass = None
ImgGalochkaSymvols = CanvaSymvols.create_image(10,3,anchor = NW,image = Galochka)
CanvasLeters.tag_bind(ImgGalochkaLeters,"<Button-1>",lambda event:ClickChekMark(ImgGalochkaLeters,CanvasLeters,2))
CanvasCAPSLeters.tag_bind(ImgGalochkaCAPSLeters,"<Button-1>",lambda event:ClickChekMark(ImgGalochkaCAPSLeters,CanvasCAPSLeters,3))
CanvaSymvols.tag_bind(ImgGalochkaSymvols,"<Button-1>",lambda event:ClickChekMark(ImgGalochkaSymvols,CanvaSymvols,4))
ExtraOptions = Button(canvas,text="  Extra Options   ",bg="white",fg="black",font=("Bips",22),command=ClickExtraOp)
ExtraOptions.place(x=650,y=170)
IsExtraOptions = False
ExtraOptionsNum = None
ExtraOptionsLeters = None
ExtraOptionsCaps = None
ExtraOptionsSymbols = None
BtnCopy = Button(canvas,text="Copy",font=("Bips",21),bg="white",fg="black",command=CopyPassword)
BtnCopy.place(x=80,y=90)
BtnSave = Button(canvas,text="Save to file",font=("Bips",21),bg="white",fg="black",command=SaveFile)
BtnSave.place(x=780,y=90)

window.mainloop()