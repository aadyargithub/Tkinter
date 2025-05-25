import tkinter as tk
window=tk.Tk()
window.title('Grid')
window.geometry('500x500')
for i in range(3):
    for j in range(3):
        frame=tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
        frame.grid(row=i,column=j,padx=5,pady=5)
        label=tk.Label(master=frame,text=f'Row{i+1}\nColumn{j+1}')
        label.pack()
window.mainloop()