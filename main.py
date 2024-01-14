from tkinter import *

window = Tk()
window.minsize(height=250,width=250)
window.config(pady=20,padx=20)

label1 = Label(text="Miles")
label1.config(text="Miles")
label1.grid(row=0,column=2)

label2 = Label(text="is equal to ")
label2.config(text="is equal to ")
label2.grid(row=1,column=0)

result = Label(text=" ")
result.grid(row=1,column=1)

def calcalution():
    value = int(input.get())
    km  = value * 1.60934
    result.config(text=km)


button = Button(text="Calculate",command=calcalution)
button.grid(row=2,column=1)
label3 = Label(text="Km")
label3.config(text="Km")
label3.grid(row=1,column=2)

input = Entry(width=20)
input.grid(row=0,column=1)
input.get()
window.mainloop()