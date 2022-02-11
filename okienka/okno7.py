import tkinter as tk

window = tk.Tk()
window.title("Aplikacja testowa v.01.b")
# window.geometry('350x200')
window.columnconfigure(0, minsize=150)
window.rowconfigure([0, 1, 2, 3], minsize=150)

label1 = tk.Label(text='A', bg="blue")
label1.grid(row=0, column=0)

label2 = tk.Label(text='B', bg="blue")
label2.grid(row=0, column=1, sticky="ew")

label3 = tk.Label(text='C', bg="blue")
label3.grid(row=0, column=2, sticky="ns")

label4 = tk.Label(text='D', bg="blue")
label4.grid(row=0, column=3, sticky="nsew")

window.mainloop()
