from tkinter import *
window=Tk()
window.title('Window')
#window.geometry('200x300')
greeting=Label(text='My name is Aadya',fg='white',bg='black')
greeting.pack()
button=Button(text='Click me!',fg='green',bg='pink')
button.pack()
entry=Entry(fg='red',bg='blue',width=50)
entry.pack()
frame=Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
label=Label(master=frame,text='HI')
label.pack()
textbox=Text(fg='yellow',bg='orange')
textbox.pack()
window.mainloop()