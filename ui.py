from tkinter import *
from tkinter.tix import TEXT
from turtle import end_fill, right, width

window = Tk()
l = 500
t = 400
x = 500
y = 100
#window.resizable(0,0)
window.minsize(l, t)
window.maxsize(l, t)
window.title("Form Pengisian Data Penduduk")
screenwidh = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

newx = int((screenwidh/2) - (l/2))
newy = int((screenheight/2) - (t/2) - 100)

window.geometry(f"{l}x{t}+{newx}+{newy}")

#def fungsi entry 1
def tombol_save():
    print(entry1.get())
    print(button3.get("1.0", END))
    
#Label 1-sekian NAMA
label1 = Label(text = "Nama Lengkap :", fg = "#fff", bg = "#ff0000")
label1.pack(anchor = "nw",side = "left", pady = "10")

#pakai entry untuk pengisian setiap label
entry1 = Entry(window, width = 60)
entry1.pack(pady="10", side=TOP)

#Label 1-sekian ALAMAT
label2 = Label(text = "Alamat :", fg = "#fff", bg = "#ff0000")
label2.pack(anchor = "nw",side = LEFT)

#text 1
button3 = Text(window, bd=2, width=50, height=1)
button3.pack(ipady="20", side=TOP)

f = open("data.txt", "a")
f.writeline(label1+label2)
f.close
#pakai entry untuk pengisian setiap label
#entry2 = Entry(window, width = 50)
#entry2.pack(side=TOP, ipady = "20")

#side = TOP(default), BOTTOM, LEFT, dan RIGHT
#fill = NONE(default), X (Fill Horizontal), Y (Fill vertikal), BOTH
#expand = YES(center ke windowsnya) dan NO
#padx, pady, ipadx, ipady
button1 = Button(text = "Save", command = tombol_save)
button1.pack(pady="30", side = BOTTOM)

window.mainloop()