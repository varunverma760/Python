from tkinter import*
root = Tk()
root.geometry("600x600+100+50")
root.title("Instrument Page")

label_0 = Label(root, text="Instruments:",width="20",font=("bold", 22))
label_0.place(x=90,y=43)


label_1 = Label(root, text="Message: -",width ="20",height ="2",font =("calibri",13))
label_1.place(x="220",y="320")

# entry_1 = Entry(root)
# entry_1.place(x="260",y="235")

label_2 = Label(root, text="Enter Frequency: -",width="20",height="1",font=("calibri", 13))
label_2.place(x="200",y="154")

entry_2 = Entry(root)
entry_2.place(x="373",y="160")

Button(root, text='Guitar',width="20",bg='green',fg='white').place(x=20,y=150)
Button(root, text='Drum',width="20",bg='green',fg='white').place(x=20,y=100)
Button(root, text='Keyboard',width=20,bg='green',fg='white').place(x=20,y=200)
root.mainloop()

