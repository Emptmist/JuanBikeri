from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime
import random
now = datetime.datetime.now()
date_time = now.strftime('%d-%m-%Y $H:%M:%S')

window = Tk()
window.title("Juan Bikeri")
window.geometry("1200x650")
window.resizable(False, False)


item_quantities = {
    "Chocolate": 0,
    "Vanilla": 0,
    "Mocha": 0,
    "Redvelvet": 0,
    "Darkchoco": 0,
    "Carrot": 0,
    "Cheese": 0,
    "Caramel": 0
}

def get_entry_field(name):
    entry_fields = {
        "Chocolate": chocoety,
        "Vanilla": vanety,
        "Mocha": mochaety,
        "Redvelvet": redety,
        "Darkchoco": darkety,
        "Carrot": rotety,
        "Cheese": cheety,
        "Caramel": carety
    }

    
    return entry_fields.get(name)
def disable_editing(event):
    return "break"

def add_item(name, price, quantity):
    item_info = f"{name}: ₱{price} x {quantity}"
    current_text = textarea.get("1.0", END).strip()
    
    if current_text != "":
        # Split the current text by newline character and get the last line
        lines = current_text.split("\n")
        last_line = lines[-1]
        
        if last_line.startswith(f"{name}: ₱{price} x"):
            # If the last line starts with the item info, replace it with the updated quantity
            lines[-1] = item_info
        else:
            # Append the item info to the existing text
            lines.append(item_info)
            
        updated_text = "\n".join(lines)
        textarea.delete("1.0", END)
        textarea.insert(END, updated_text)
    else:
        # If the textarea is empty, directly insert the item info
        textarea.insert(END, item_info)

def subtract_from_bill(name, price):
    quantity = item_quantities[name]
    if quantity > 0:
        item_quantities[name] -= 1
        update_bill()

def decrement_quantity(entry, name):
    current_quantity = entry.get()
    if current_quantity.isdigit() and int(current_quantity) > 0:  # Check if the value is a valid integer and greater than 0
        current_quantity = int(current_quantity)
        entry.delete(0, END)
        entry.insert(0, str(current_quantity - 1))

        # Update the quantity in the item_quantities dictionary
        item_quantities[name] -= 1


def increment_quantity(entry, name):
    current_quantity = entry.get()
    if current_quantity.isdigit():  # Check if the value is a valid integer
        current_quantity = int(current_quantity)
    else:
        current_quantity = 0

    entry.delete(0, END)
    entry.insert(0, str(current_quantity + 1))

    # Update the quantity in the item_quantities dictionary
    item_quantities[name] += 1


def update_bill():
    total = 0
    textarea.delete("1.0", END)  # Clear the bill area

    for name, quantity in item_quantities.items():
        if quantity > 0:
            price = get_item_price(name)
            item_total = price * quantity
            total += item_total
            add_item(name, price, quantity)

    totalety.delete(0, END)
    totalety.insert(0, str(total))
    vatety.delete(0, END)
    vatety.insert(0, str(total * 0.12))
    taxety.delete(0, END)
    taxety.insert(0, str(total * 0.12))
    payety.delete(0, END)
    chgnety.delete(0, END)


def get_item_price(name):
    prices = {
        "Chocolate": 500,
        "Vanilla": 450,
        "Mocha": 400,
        "Redvelvet": 600,
        "Darkchoco": 700,
        "Carrot": 400,
        "Cheese": 300,
        "Caramel": 350
    }
    return prices.get(name, 0)


def add_to_bill(name, price):
    quantity = item_quantities[name]
    add_item(name, price, quantity)

    # Increment the quantity in the corresponding entry field
    if name == "Chocolate":
        increment_quantity(chocoety, "Chocolate")
    elif name == "Vanilla":
        increment_quantity(vanety, "Vanilla")
    elif name == "Mocha":
        increment_quantity(mochaety, "Mocha")
    elif name == "Redvelvet":
        increment_quantity(redety, "Redvelvet")
    elif name == "Darkchoco":
        increment_quantity(darkety, "Darkchoco")
    elif name == "Carrot":
        increment_quantity(rotety, "Carrot")
    elif name == "Cheese":
        increment_quantity(cheety, "Cheese")
    elif name == "Caramel":
        increment_quantity(carety, "Caramel")

def subtract_from_bill(name, price):
    quantity = item_quantities[name]
    if quantity > 0:
        item_quantities[name] -= 1
        decrement_quantity(get_entry_field(name), name)
        update_bill()


#MAIN FRAMES
mainframe = Frame(window)
mainframe.pack()

#MENU FRAME
menuframe = LabelFrame(mainframe, width=450, height=500, bg="#8e5431", relief=GROOVE,
                       highlightthickness=2)
menuframe.grid(row=0,column=0,rowspan=2)

def add_to_bill(name, price):
    quantity = item_quantities[name]
    add_item(name, price, quantity)

    # Increment the quantity in the corresponding entry field
    if name == "Chocolate":
        increment_quantity(chocoety, "Chocolate")
    elif name == "Vanilla":
        increment_quantity(vanety, "Vanilla")
    elif name == "Mocha":
        increment_quantity(mochaety, "Mocha")
    elif name == "Redvelvet":
        increment_quantity(redety, "Redvelvet")
    elif name == "Darkchoco":
        increment_quantity(darkety, "Darkchoco")
    elif name == "Carrot":
        increment_quantity(rotety, "Carrot")
    elif name == "Cheese":
        increment_quantity(cheety, "Cheese")
    elif name == "Caramel":
        increment_quantity(carety, "Caramel")

chocolate = PhotoImage(file="chocolate.png")
vanilla = PhotoImage(file="vanilla.png")
ahcom = PhotoImage(file="mocha.png")
redvelvet = PhotoImage(file="redvelvet.png")
darkchoco = PhotoImage(file="darkchoco.png")
carrot = PhotoImage(file="carrot.png")
cheese = PhotoImage(file="cheese.png")
caramel = PhotoImage(file="caramel.png")

choco = Button(menuframe, width=110, height=95, image=chocolate)
choco.grid(row=0, column=0, rowspan=2, pady=11)
chocolbl = Label(menuframe, text="Chocolate:₱500", font="Arial 10 bold", bg="#8e5431", fg="#ffffff")
chocolbl.grid(row=0, column=1, columnspan=3)
chocominus = Button(menuframe, width=2, height=1, text="-", font="Arial 12 bold", bg="#efcead")
chocominus.grid(row=1, column=1)
chocobtn = Button(menuframe, width=2, height=1, text="C", font="Arial 12 bold", bg="#efcead")
chocobtn.grid(row=1, column=2)
choco_plus_btn = Button(menuframe, width=2, height=1, text="+", font="Arial 12 bold", bg="#efcead", command=lambda: add_to_bill("Chocolate", 500))
choco_plus_btn.grid(row=1, column=3)

van = Button(menuframe, width=110, height=95, image=vanilla)
van.grid(row=0, column=4, rowspan=2, pady=11)
vanlbl = Label(menuframe, text="Vanilla:₱450", font="Arial 10 bold", bg="#8e5431", fg="#ffffff")
vanlbl.grid(row=0, column=5, columnspan=3)
vanminus = Button(menuframe, width=2, height=1, text="-", font="Arial 12 bold", bg="#efcead")
vanminus.grid(row=1, column=5)
vanbtn = Button(menuframe, width=2, height=1, text="C", font="Arial 12 bold", bg="#efcead")
vanbtn.grid(row=1, column=6)
van_plus_btn = Button(menuframe, width=2, height=1, text="+", font="Arial 12 bold", bg="#efcead", command=lambda: add_to_bill("Vanilla", 450))
van_plus_btn.grid(row=1, column=7)

mocha = Button(menuframe, width=110, height=95, image=ahcom)
mocha.grid(row=2, column=0, rowspan=2, pady=11)
mochalbl = Label(menuframe, text="Mocha:₱400", font="Arial 10 bold", bg="#8e5431", fg="#ffffff")
mochalbl.grid(row=2, column=1, columnspan=3)
mochaminus = Button(menuframe, width=2, height=1, text="-", font="Arial 12 bold", bg="#efcead")
mochaminus.grid(row=3, column=1)
mochabtn = Button(menuframe, width=2, height=1, text="C", font="Arial 12 bold", bg="#efcead")
mochabtn.grid(row=3, column=2)
mocha_plus_btn = Button(menuframe, width=2, height=1, text="+", font="Arial 12 bold", bg="#efcead", command=lambda: add_to_bill("Mocha", 400))
mocha_plus_btn.grid(row=3, column=3)

red = Button(menuframe, width=110, height=95, image=redvelvet)
red.grid(row=2, column=4, rowspan=2, pady=11)
redlbl = Label(menuframe, text="Redvelvet:₱600", font="Arial 10 bold", bg="#8e5431", fg="#ffffff")
redlbl.grid(row=2, column=5, columnspan=3)
redminus = Button(menuframe, width=2, height=1, text="-", font="Arial 12 bold", bg="#efcead")
redminus.grid(row=3, column=5)
redbtn = Button(menuframe, width=2, height=1, text="C", font="Arial 12 bold", bg="#efcead")
redbtn.grid(row=3, column=6)
red_plus_btn = Button(menuframe, width=2, height=1, text="+", font="Arial 12 bold", bg="#efcead", command=lambda: add_to_bill("Redvelvet", 600))
red_plus_btn.grid(row=3, column=7)

dark = Button(menuframe, width=110, height=95, image=darkchoco)
dark.grid(row=4, column=0, rowspan=2, pady=11)
darklbl = Label(menuframe, text="Darkchoco:₱700", font="Arial 10 bold", bg="#8e5431", fg="#ffffff")
darklbl.grid(row=4, column=1, columnspan=3)
darkminus = Button(menuframe, width=2, height=1, text="-", font="Arial 12 bold", bg="#efcead")
darkminus.grid(row=5, column=1)
darkbtn = Button(menuframe, width=2, height=1, text="C", font="Arial 12 bold", bg="#efcead")
darkbtn.grid(row=5, column=2)
dark_plus_btn = Button(menuframe, width=2, height=1, text="+", font="Arial 12 bold", bg="#efcead", command=lambda: add_to_bill("Darkchoco", 700))
dark_plus_btn.grid(row=5, column=3)

rot = Button(menuframe, width=110, height=95, image=carrot)
rot.grid(row=4, column=4, rowspan=2, pady=11)
rotlbl = Label(menuframe, text="Carrot:₱400", font="Arial 10 bold", bg="#8e5431", fg="#ffffff")
rotlbl.grid(row=4, column=5, columnspan=3)
rotminus = Button(menuframe, width=2, height=1, text="-", font="Arial 12 bold", bg="#efcead")
rotminus.grid(row=5, column=5)
rotbtn = Button(menuframe, width=2, height=1, text="C", font="Arial 12 bold", bg="#efcead")
rotbtn.grid(row=5, column=6)
rot_plus_btn = Button(menuframe, width=2, height=1, text="+", font="Arial 12 bold", bg="#efcead", command=lambda: add_to_bill("Carrot", 400))
rot_plus_btn.grid(row=5, column=7)

che = Button(menuframe, width=110, height=95, image=cheese)
che.grid(row=6, column=0, rowspan=2, pady=11)
chelbl = Label(menuframe, text="Cheese:₱300", font="Arial 10 bold", bg="#8e5431", fg="#ffffff")
chelbl.grid(row=6, column=1, columnspan=3)
cheminus = Button(menuframe, width=2, height=1, text="-", font="Arial 12 bold", bg="#efcead")
cheminus.grid(row=7, column=1)
chebtn = Button(menuframe, width=2, height=1, text="C", font="Arial 12 bold", bg="#efcead")
chebtn.grid(row=7, column=2)
che_plus_btn = Button(menuframe, width=2, height=1, text="+", font="Arial 12 bold", bg="#efcead", command=lambda: add_to_bill("Cheese", 300))
che_plus_btn.grid(row=7, column=3)

car = Button(menuframe, width=110, height=95, image=caramel)
car.grid(row=6, column=4, rowspan=2, pady=11)
carlbl = Label(menuframe, text="Caramel:₱350", font="Arial 10 bold", bg="#8e5431", fg="#ffffff")
carlbl.grid(row=6, column=5, columnspan=3)
carminus = Button(menuframe, width=2, height=1, text="-", font="Arial 12 bold", bg="#efcead")
carminus.grid(row=7, column=5)
carbtn = Button(menuframe, width=2, height=1, text="C", font="Arial 12 bold", bg="#efcead")
carbtn.grid(row=7, column=6)
car_plus_btn = Button(menuframe, width=2, height=1, text="+", font="Arial 12 bold", bg="#efcead", command=lambda: add_to_bill("Caramel", 350))
car_plus_btn.grid(row=7, column=7)

#INFORMATION FRAME
infoframe = LabelFrame(mainframe, width=375, height=150, bg="#8e5431", relief=GROOVE,
                       highlightthickness=2)
infoframe.grid(row=0,column=1)

namelbl = Label(infoframe, text="Name:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
namelbl.place(x=20,y=20)

nameety = Entry(infoframe, width=25,  font="Arial 13 bold")
nameety.place(x=110,y=20)

tinlbl = Label(infoframe, text="Tin No.:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
tinlbl.place(x=20,y=60)

tinety = Entry(infoframe, width=25,  font="Arial 13 bold")
tinety.place(x=110,y=60)

addlbl = Label(infoframe, text="Address:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
addlbl.place(x=20,y=100)

addety = Entry(infoframe, width=25,  font="Arial 13 bold")
addety.place(x=110,y=100)

#RECEIPT FRAME
recframe = LabelFrame(mainframe, width=375, height=500, bg="#8e5431", relief=GROOVE,
                      highlightthickness=2)
recframe.grid(row=0,column=2,rowspan=2)

receipt = LabelFrame(recframe,relief=GROOVE,bd=10)
receipt.place(x=-1,y=-1,width=375,height=500)
Label(receipt,text="RECEIPT FRAME",font="arial 16 bold",relief="raise",bd=5).pack(fill=X)
scrlY = Scrollbar(receipt,orient=VERTICAL)
textarea = Text(receipt, yscrollcommand=scrlY)
scrlY.pack(side=RIGHT,fill=Y)
scrlY.config(command=textarea.yview)
textarea.bind("<Key>", disable_editing)
textarea.pack()

#BILL AREA FRAME
posframe = LabelFrame(mainframe, width=375, height=350, bg="#8e5431", relief=GROOVE,
                      highlightthickness=2)
posframe.grid(row=1,column=1)

F4 = LabelFrame(posframe,relief=GROOVE,bd=10)
F4.place(x=-1,y=-1,width=370,height=345)
Label(F4,text="BILL AREA",font="arial 16 bold",relief="raise",bd=5).pack(fill=X)
scrlY = Scrollbar(F4,orient=VERTICAL)
textarea = Text(F4, yscrollcommand=scrlY,bg="#000000",fg="#ffffff")
scrlY.pack(side=RIGHT,fill=Y)
scrlY.config(command=textarea.yview)
textarea.bind("<Key>")
textarea.pack()



#INPUT FRAME
inframe = LabelFrame(mainframe, width=825, height=150, bg="#8e5431", relief=GROOVE,
                      highlightthickness=2)
inframe.grid(row=2,column=0,columnspan=2)

totallbl = Label(inframe, text="Total:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
totallbl.place(x=20,y=20)

totalety = Entry(inframe, width=15,  font="Arial 13 bold")
totalety.place(x=110,y=20)
totalety.bind("<Key>", disable_editing)

vatlbl = Label(inframe, text="Vat:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
vatlbl.place(x=20,y=60)

vatety = Entry(inframe, width=15,  font="Arial 13 bold")
vatety.place(x=110,y=60)
vatety.bind("<Key>", disable_editing)

taxlbl = Label(inframe, text="Tax 12%:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
taxlbl.place(x=20,y=100)

taxety = Entry(inframe, width=15,  font="Arial 13 bold")
taxety.place(x=110,y=100)
taxety.bind("<Key>", disable_editing)

lblMethod = Label(inframe, text="Method:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
lblMethod.place(x=270,y=20)

cboMethod = ttk.Combobox(inframe, width=13, font=("arial", 13, "bold"),
                         state="readonly", justify=RIGHT)
cboMethod["values"] = ("Cash", "Gcash") 
cboMethod.current(0)
cboMethod.place(x=360,y=20)

paylbl = Label(inframe, text="Payment:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
paylbl.place(x=520,y=20)

payety = Entry(inframe, width=15,  font="Arial 13 bold")
payety.place(x=620,y=20)

chgnlbl = Label(inframe, text="Change:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
chgnlbl.place(x=270,y=100)

chgnety = Entry(inframe, width=15,  font="Arial 13 bold")
chgnety.place(x=360,y=100)
chgnety.bind("<Key>", disable_editing)

lbldisc = Label(inframe, text="Discount:", font="Arial 13 bold", bg="#8e5431", fg="#ffffff")
lbldisc.place(x=270,y=60)

cbodisc = ttk.Combobox(inframe, width=13, font=("arial", 13, "bold"),
                         state="readonly", justify=RIGHT)
cbodisc["values"] = ("Regular", "PWD/Senior 5%") 
cbodisc.current(0)
cbodisc.place(x=360,y=60)

removebtn = Button(inframe, text="remove", width=30, font="Arial 10 bold", bg="#efcead")
removebtn.place(x=520,y=60)

resetbtn = Button(inframe, text="reset", width=30, font="Arial 10 bold", bg="#efcead")
resetbtn.place(x=520,y=100)

#KEYPAD FRAME
keyframe = LabelFrame(mainframe, width=375, height=150, bg="#8e5431", relief=GROOVE,
                      highlightthickness=2)
keyframe.grid(row=2,column=2)

onebtn = Button(keyframe, width=3, height=1, text="1", font="Arial 15 bold", bg="#efcead")
onebtn.grid(row=0,column=0,pady=3,padx=2)

twobtn = Button(keyframe, width=3, height=1, text="2", font="Arial 15 bold", bg="#efcead")
twobtn.grid(row=0,column=1,pady=3,padx=2)

threebtn = Button(keyframe, width=3, height=1, text="3", font="Arial 15 bold", bg="#efcead")
threebtn.grid(row=0,column=2,pady=3,padx=2)

fourbtn = Button(keyframe, width=3, height=1, text="4", font="Arial 15 bold", bg="#efcead")
fourbtn.grid(row=1,column=0,pady=3,padx=2)

fivebtn = Button(keyframe, width=3, height=1, text="5", font="Arial 15 bold", bg="#efcead")
fivebtn.grid(row=1,column=1,pady=3,padx=2)

sixbtn = Button(keyframe, width=3, height=1, text="6", font="Arial 15 bold", bg="#efcead")
sixbtn.grid(row=1,column=2,pady=3,padx=2)

sevenbtn = Button(keyframe, width=3, height=1, text="7", font="Arial 15 bold", bg="#efcead")
sevenbtn.grid(row=2,column=0,pady=3,padx=2)

eightbtn = Button(keyframe, width=3, height=1, text="8", font="Arial 15 bold", bg="#efcead")
eightbtn.grid(row=2,column=1,pady=3,padx=2)

ninebtn = Button(keyframe, width=3, height=1, text="9", font="Arial 15 bold", bg="#efcead")
ninebtn.grid(row=2,column=2,pady=3,padx=2)

clearbtn = Button(keyframe, width=8, height=3, text="Clear", font="Arial 14 bold", bg="#efcead")
clearbtn.grid(row=0,column=3,rowspan=2,pady=3,padx=2)

removebtn = Button(keyframe, width=8, height=3, text="←", font="Arial 14 bold", bg="#efcead")
removebtn.grid(row=0,column=4,rowspan=2,pady=3,padx=2)

zerobtn = Button(keyframe, width=8, height=1, text="0", font="Arial 15 bold", bg="#efcead")
zerobtn.grid(row=2,column=3,pady=3,padx=2)

decbtn = Button(keyframe, width=8, height=1, text=".", font="Arial 15 bold", bg="#efcead")
decbtn.grid(row=2,column=4,pady=3,padx=2)


window.mainloop()
