from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime
now = datetime.datetime.now()
date_time = now.strftime('%Y-%m-%d %I:%M:%S %p')

window = Tk()
window.title("Juan Bikeri")
window.geometry("1400x1200")
window.configure(bg="#8e5431")
window.state("zoomed")

#Functions
def disable_editing(event):
    return "break"

def pay():
    try:
        if etyPay.get() is not None and etyTotal.get() == "":
            messagebox.showinfo("", "No items to process")
        elif float(etyPay.get()) >= float(etyTotal.get()):
            if etyDiscount.get() == "" or etyDiscount.get().upper() == "NO": 
                change = float(etyPay.get()) - float(etyTotal.get())
                vat = float(etyTotal.get()) - float(etyTax.get())
                etyChange.delete(0,END)
                etyChange.insert(0,round(change,2))
                textarea.insert(END,"========================RECEIPT=======================\n")
                textarea.insert(END,"----------------------JUAN BIKERI---------------------\n")
                textarea.insert(END,"                  OWNED AND OPERATED                  \n")
                textarea.insert(END,"          PAR, NICOL, GASCON, BITANCOR, JAVIER        \n")
                textarea.insert(END,"          CAVITE STATE UNIVERSITY IMUS, CAMPUS        \n")
                textarea.insert(END,"          REGISTERED VAT TIN. 091-234-567-890         \n")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,"NAME:                                                 \n")
                textarea.insert(END,"CASHIER: Python                                       \n")
                textarea.insert(END,"PROCESSED BY: Python                                  \n")
                textarea.insert(END,f"DATE: {date_time}                           ")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,"ITEM        QUANTITY        SUBTOTAL     \n")
                textarea.insert(END,f"Chocolate  -  {etychocolate.get():8}  -   {float(etychocolateprice)}\n")
                textarea.insert(END,f"Vanilla    -  {etyvanilla.get():8}  -   {float(etyvanillaprice)}\n")
                textarea.insert(END,f"Mocha      -  {etymocha.get():8}  -   {float(etymochaprice)}\n")
                textarea.insert(END,f"Redvelvet  -  {etyredvelvet.get():8}  -   {float(etyredvelvetprice)}\n")
                textarea.insert(END,f"Darkchoco  -  {etydarkchoco.get():8}  -   {float(etydarkchocoprice)}\n")
                textarea.insert(END,f"Carrot     -  {etycarrot.get():8}  -   {float(etycarrotprice)}\n")
                textarea.insert(END,f"Cheese     -  {etycheese.get():8}  -   {float(etycheeseprice)}\n")
                textarea.insert(END,f"Caramel    -  {etycaramel.get():8}  -   {float(etycaramelprice)}\n")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,f"TOTAL    :  {float(etyTotal.get())}                  \n")
                textarea.insert(END,f"CASH     :  {float(etyPay.get())}                    \n")
                textarea.insert(END,f"DISCOUNT :  0                                        \n")
                textarea.insert(END,f"CHANGE   :  {float(etyChange.get())}                 \n")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,f"VATable  :  {vat}                                    \n")
                textarea.insert(END,f"12% VAT  :  {float(etyTax.get())}                    \n")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,"                       THANK YOU!                     \n")
                textarea.insert(END,"              FOR PURCHASING AT JUAN BIKERI           \n")
                textarea.insert(END,"                  HOPE TO SEE YOU AGAIN               \n")
                textarea.insert(END,"                  DATE ISSUED: {date_time[0:10]}      \n")
                textarea.insert(END,"            TEL # 0912-345-6789 / (123)- 4567)        \n")
                textarea.insert(END,"======================================================\n")
            elif etyDiscount.get().upper() == "YES":
                change = (float(etyPay.get()) - float(etyTotal.get())) + (float(etyTotal.get()) * 0.05)
                discount = (float(etyTotal.get()) * 0.05)
                vat = float(etyTotal.get()) - float(etyTax.get())
                etyChange.delete(0,END)
                etyChange.insert(0,round(change,2))
                textarea.insert(END,"========================RECEIPT=======================\n")
                textarea.insert(END,"----------------------JUAN BIKERI---------------------\n")
                textarea.insert(END,"                  OWNED AND OPERATED                  \n")
                textarea.insert(END,"          PAR, NICOL, GASCON, BITANCOR, JAVIER        \n")
                textarea.insert(END,"          CAVITE STATE UNIVERSITY IMUS, CAMPUS        \n")
                textarea.insert(END,"          REGISTERED VAT TIN. 091-234-567-890         \n")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,"NAME:                                                 \n")
                textarea.insert(END,"PROCESSED BY: Python                                  \n")
                textarea.insert(END,f"DATE: {date_time}                           ")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,"ITEM        QUANTITY        SUBTOTAL     \n")
                textarea.insert(END,f"Chocolate  -  {etychocolate.get():8}  -   {etychocolateprice}\n")
                textarea.insert(END,f"Vanilla    -  {etyvanilla.get():8}  -   {etyvanillaprice}\n")
                textarea.insert(END,f"Mocha      -  {etymocha.get():8}  -   {etymochaprice}\n")
                textarea.insert(END,f"Redvelvet  -  {etyredvelvet.get():8}  -   {etyredvelvetprice}\n")
                textarea.insert(END,f"Darkchoco  -  {etydarkchoco.get():8}  -   {etydarkchocoprice}\n")
                textarea.insert(END,f"Carrot     -  {etycarrot.get():8}  -   {etycarrotprice}\n")
                textarea.insert(END,f"Cheese     -  {etycheese.get():8}  -   {etycheeseprice}\n")
                textarea.insert(END,f"Caramel    -  {etycaramel.get():8}  -   {etycaramelprice}\n")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,f"TOTAL    :  {float(etyTotal.get())}                  \n")
                textarea.insert(END,f"CASH     :  {float(etyPay.get())}                    \n")
                textarea.insert(END,f"DISCOUNT :  {discount}                               \n")
                textarea.insert(END,f"CHANGE   :  {float(etyChange.get())}                 \n")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,f"VATable  :  {vat}                                    \n")
                textarea.insert(END,f"12% VAT  :  {float(etyTax.get())}                    \n")
                textarea.insert(END,"------------------------------------------------------\n")
                textarea.insert(END,"                       THANK YOU!                     \n")
                textarea.insert(END,"              FOR PURCHASING AT JUAN BIKERI           \n")
                textarea.insert(END,"                  HOPE TO SEE YOU AGAIN               \n")
                textarea.insert(END,"                  DATE ISSUED: {date_time[0:10]}      \n")
                textarea.insert(END,"            TEL # 0912-345-6789 / (123)- 4567)        \n")
                textarea.insert(END,"======================================================\n")
            else:
                messagebox.showinfo("", "Choose a Discount")
        elif float(etyPay.get()) <= float(etyTotal.get()) or float(etyPay.get()) == "":
            messagebox.showinfo("Payment Invalid", "Invalid Payment")
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

def Exit():
    window.destroy()
    
def calculate():
    etychocolatetax = (int(etychocolate.get()) * 500) * 0.12
    etyvanillatax = (int(etyvanilla.get()) * 450) * 0.12
    etymochatax = (int(etymocha.get()) * 400) * 0.12
    etyredvelvettax = (int(etyredvelvet.get()) * 600) * 0.12
    etydarkchocotax = (int(etydarkchoco.get()) * 700) * 0.12
    etycarrottax = (int(etycarrot.get()) * 400) * 0.12
    etycheesetax = (int(etycheese.get()) * 300) * 0.12
    etycarameltax = (int(etycaramel.get()) * 350) * 0.12

    global etychocolateprice
    etychocolateprice = int(etychocolate.get()) * (440 + (500 * 0.12))
    global etyvanillaprice
    etyvanillaprice = int(etyvanilla.get()) * (396 + (450 * 0.12))
    global etymochaprice
    etymochaprice = int(etymocha.get()) * (352 + (400 * 0.12))
    global etyredvelvetprice
    etyredvelvetprice = int(etyredvelvet.get()) * (528 + (600 * 0.12))
    global etydarkchocoprice
    etydarkchocoprice = int(etydarkchoco.get()) * (616 + (700 * 0.12))
    global etycarrotprice
    etycarrotprice = int(etycarrot.get()) * (352 + (400 * 0.12))
    global etycheeseprice
    etycheeseprice = int(etycheese.get()) * (264 + (300 * 0.12))
    global etycaramelprice
    etycaramelprice = int(etycaramel.get()) * (308 + (350 * 0.12))
    
    total = (etychocolateprice + etyvanillaprice + etymochaprice + etyredvelvetprice +
             etydarkchocoprice + etycarrotprice + etycheeseprice + etycaramelprice)
    etyTotal.delete(0,END)
    etyTotal.insert(0,float(total))

    tax = (etychocolatetax + etyvanillatax + etymochatax + etyredvelvettax +
           etydarkchocotax + etycarrottax + etycheesetax + etycarameltax)
    etyTax.delete(0,END)
    etyTax.insert(0,float(tax))

def reset():
    retry = messagebox.askyesno("Retry?", "Do you want to try another transaction?")
    if retry:
        etychocolate.delete(0,END)
        etychocolate.insert(0,0)
        etyvanilla.delete(0,END)
        etyvanilla.insert(0,0)
        etymocha.delete(0,END)
        etymocha.insert(0,0)
        etyredvelvet.delete(0,END)
        etyredvelvet.insert(0,0)
        etydarkchoco.delete(0,END)
        etydarkchoco.insert(0,0)
        etycarrot.delete(0,END)
        etycarrot.insert(0,0)
        etycheese.delete(0,END)
        etycheese.insert(0,0)
        etycaramel.delete(0,END)
        etycaramel.insert(0,0)

        etyTotal.delete(0,END)
        etyChange.delete(0,END)
        etyTax.delete(0,END)
        etyDiscount.delete(0,END)
        etyPay.delete(0,END)
        textarea.delete("1.0",END)
    else:
        pass
    
    
#Logo
img = Image.open("Bikeri.png")
resized = img.resize((200,200))
image = ImageTk.PhotoImage(resized)
image_label = Label(window, bg="#8e5431", image=image, relief=GROOVE, bd=10,
                    width=1400, height=80)
image_label.pack()

#Container
mainframe = Frame(window, bg="#8e5431")
mainframe.pack()

#Menu
menu_container = LabelFrame(window,bg="#8e5431",fg="#FF834A",font=("helvetica", 17),relief=GROOVE,bd=10)
menu_container.place(x=0,y=100,width=885
                     ,height=479)

menu = Label(menu_container, text="MENU",fg="#FF834A", bg="black",font=("helvetica", 17))
menu.pack()

menuframe = LabelFrame(menu, bd=5, width=320, height=460,padx=5, pady=2, relief=RIDGE,
                       bg="#efcead", font=("Arial", 14, "bold"), text="MENU")
menuframe.pack()

chocolate = PhotoImage(file="chocolate.png")
vanilla = PhotoImage(file="vanilla.png")
mocha = PhotoImage(file="mocha.png")
redvelvet = PhotoImage(file="redvelvet.png")
darkchoco = PhotoImage(file="darkchoco.png")
carrot = PhotoImage(file="carrot.png")
cheese = PhotoImage(file="cheese.png")
caramel = PhotoImage(file="caramel.png")

lblchocolate = Label(menuframe, padx=2, image=chocolate, width=150, height=98, bd=2)
lblchocolate.grid(row=0, column=0, padx=4, pady=2, rowspan=2)
lblvanilla = Label(menuframe, padx=2, image=vanilla, width=150, height=98, bd=2)
lblvanilla.grid(row=0, column=2, padx=4, pady=2, rowspan=2)
lblmocha = Label(menuframe, padx=2, image=mocha, width=150, height=98, bd=2)
lblmocha.grid(row=2, column=0, padx=4, pady=2, rowspan=2)
lblredvelvet = Label(menuframe, padx=2, image=redvelvet, width=150, height=98, bd=2)
lblredvelvet.grid(row=2, column=2, padx=4, pady=2, rowspan=2)
lbldarkchoco = Label(menuframe, padx=2, image=darkchoco, width=150, height=98, bd=2)
lbldarkchoco.grid(row=4, column=0, padx=4, pady=2, rowspan=2)
lblcarrot = Label(menuframe, padx=2, image=carrot, width=150, height=98, bd=2)
lblcarrot.grid(row=4, column=2, padx=4, pady=2, rowspan=2)
lblcheese = Label(menuframe, padx=2, image=cheese, width=150, height=98, bd=2)
lblcheese.grid(row=6, column=0, padx=4, pady=2, rowspan=2)
lblcaramel = Label(menuframe, padx=2, image=caramel, width=150, height=98, bd=2)
lblcaramel.grid(row=6, column=2, padx=4, pady=2, rowspan=2)

namechocolate = Label(menuframe, text="Chocolate: P500", font=("helvetica", 15, "bold"), bg="#efcead")
namechocolate.grid(row=0, column=1, padx=57)
namevanilla = Label(menuframe, text="Vanilla: P450", font=("helvetica", 15, "bold"), bg="#efcead")
namevanilla.grid(row=0, column=4, padx=57)
namemocha = Label(menuframe, text="Mocha: P400", font=("helvetica", 15, "bold"), bg="#efcead")
namemocha.grid(row=2, column=1, padx=57)
nameredvelvet = Label(menuframe, text="Redvelvet: P600", font=("helvetica", 15, "bold"), bg="#efcead")
nameredvelvet.grid(row=2, column=4, padx=57)
namedarkchoco = Label(menuframe, text="Darkchoco: P700", font=("helvetica", 15, "bold"), bg="#efcead")
namedarkchoco.grid(row=4, column=1, padx=57)
namecarrot = Label(menuframe, text="Carrot: P400", font=("helvetica", 15, "bold"), bg="#efcead")
namecarrot.grid(row=4, column=4, padx=57)
namecheese = Label(menuframe, text="Cheese: P300", font=("helvetica", 15, "bold"), bg="#efcead")
namecheese.grid(row=6, column=1, padx=57)
namecaramel = Label(menuframe, text="Caramel: P350", font=("helvetica", 15, "bold"), bg="#efcead")
namecaramel.grid(row=6, column=4, padx=57)

etychocolate = Entry(menuframe, width=15, font=("arial", 15, "bold"), justify=CENTER)
etychocolate.grid(row=1, column=1)
etychocolate.insert(0,0)
etyvanilla = Entry(menuframe, width=15, font=("arial", 15, "bold"), justify=CENTER)
etyvanilla.grid(row=1, column=4)
etyvanilla.insert(0,0)
etymocha = Entry(menuframe, width=15, font=("arial", 15, "bold"), justify=CENTER)
etymocha.grid(row=3, column=1)
etymocha.insert(0,0)
etyredvelvet = Entry(menuframe, width=15, font=("arial", 15, "bold"), justify=CENTER)
etyredvelvet.grid(row=3, column=4)
etyredvelvet.insert(0,0)
etydarkchoco = Entry(menuframe, width=15, font=("arial", 15, "bold"), justify=CENTER)
etydarkchoco.grid(row=5, column=1)
etydarkchoco.insert(0,0)
etycarrot = Entry(menuframe, width=15, font=("arial", 15, "bold"), justify=CENTER)
etycarrot.grid(row=5, column=4)
etycarrot.insert(0,0)
etycheese = Entry(menuframe, width=15, font=("arial", 15, "bold"), justify=CENTER)
etycheese.grid(row=7, column=1)
etycheese.insert(0,0)
etycaramel = Entry(menuframe, width=15, font=("arial", 15, "bold"), justify=CENTER)
etycaramel.grid(row=7, column=4)
etycaramel.insert(0,0)

#Receipt
receipt = LabelFrame(window,relief=GROOVE,bd=10)
receipt.place(x=885,y=100,width=480,height=479)
Label(receipt,text="BILL AREA",font="arial 16 bold",relief=GROOVE,bd=5).pack(fill=X)
scrlY = Scrollbar(receipt,orient=VERTICAL)
textarea = Text(receipt, yscrollcommand=scrlY)
scrlY.pack(side=RIGHT,fill=Y)
scrlY.config(command=textarea.yview)
textarea.bind("<Key>", disable_editing)
textarea.pack()


#Total, Change, Tax
tt = Frame(window, bd=10, width=425, height=140, relief=RIDGE, bg="#8e5431", pady=5)
tt.place(x=0,y=580)

lblTotal = Label(tt,height=1, font=("arial", 14, "bold"), text="Total", bd=5, bg="#8e5431")
lblTotal.grid(row=0, column=0, sticky=W, padx=10)
etyTotal = Entry(tt, font=("arial", 14, "bold"), bd=2, width=23, justify='left',bg="#efcead")
etyTotal.grid(row=0, column=1, padx=15)
etyTotal.bind("<Key>", disable_editing)
etyTotal.insert(0,"")

lblChange = Label(tt,height=1, font=("arial", 14, "bold"), text="Change", bd=5, bg="#8e5431")
lblChange.grid(row=2, column=0, sticky=W, padx=10)
etyChange = Entry(tt, font=("arial", 14, "bold"), bd=2, width=23, bg="#efcead")
etyChange.grid(row=2, column=1, sticky=W, padx=15)
etyChange.bind("<Key>", disable_editing)
etyChange.insert(0,"")

lblTax = Label(tt,height=1, font=("arial", 14, "bold"), text="12% Tax", bd=5, bg="#8e5431")
lblTax.grid(row=1, column=0, sticky=W, padx=10)
etyTax = Entry(tt, font=("arial", 14, "bold"), bd=2, width=23, bg="#efcead")
etyTax.grid(row=1, column=1, sticky=W, padx=15)
etyTax.bind("<Key>", disable_editing)
etyTax.insert(0,"")

#Pay, Print, Reset, Calculate
pprc = Frame(window, bd=10, width=425, height=240, pady=4, relief=RIDGE, bg="#8e5431")
pprc.place(x=885,y=580)

btnCalculate = Button(pprc, padx=2, font=("arial", 13, "bold"), text="Process items",
                width=21, height=1, bd=2, bg="#efcead", command=calculate)
btnCalculate.grid(row=0, column=0, padx=4, pady=2)
btnPay = Button(pprc, padx=2, font=("arial", 13, "bold"),text="Pay/Print",
                  width=21, height=1, bd=2, bg="#efcead", command=pay)
btnPay.grid(row=0, column=1, padx=4, pady=2)
btnReset = Button(pprc, padx=2, font=("arial", 13, "bold"), text="Reset",
                      width=21, height=1, bd=2, bg="#efcead", command=reset)
btnReset.grid(row=1, column=0, padx=4, pady=2)
btnExit = Button(pprc, padx=2, font=("arial", 13, "bold"), text="Exit",
                  width=21, height=1, bd=2, bg="#efcead", command=Exit)
btnExit.grid(row=1, column=1, padx=4, pady=2)

#Method, Discount, Payment
paymentframe = Frame(window, bd=10, width=300, height=140, pady=2, relief=RIDGE, bg="#8e5431")
paymentframe.place(x=412,y=580)
        
lblMethod = Label(paymentframe,height=1, font=("arial", 14, "bold" ),
                  bg="#8e5431", text= "Payment Method", bd=2)
lblMethod.grid(row=0, column=0,sticky=W, padx=1, pady=4)
cboMethod = ttk.Combobox(paymentframe, width=24, font=("arial", 14, "bold"),
                         state="readonly", justify=RIGHT)

cboMethod["values"] = ("Cash", "Gcash", "Paymaya", "Visa", "Master Card") 
cboMethod.current(0)
cboMethod.grid(row=0, column=1, pady=4, padx=2)

lblDiscount = Label(paymentframe,height=1, font=("arial", 14, "bold" ),
                    bg="#8e5431", text= "PWD/Senior? (5%)", bd=2)
lblDiscount.grid(row=1, column=0, sticky=W, padx=1, pady=4)
etyDiscount = Entry(paymentframe, font=("arial", 14, "bold"), bd=2, width=24,
                  bg="#efcead", justify=RIGHT)
etyDiscount.grid(row=1, column=1, pady=4)

lblPay = Label(paymentframe,height=1, font=("arial", 14, "bold" ),
               bg="#8e5431", text= "Amount Pay", bd=5)
lblPay.grid(row=2, column=0, sticky=W, padx=1, pady=4)
etyPay = Entry(paymentframe, font=("arial", 14, "bold"), bd=2, width=24,
               bg="#efcead", justify=RIGHT)
etyPay.grid(row=2, column=1, pady=4)


window.mainloop()
