import tkinter as tk

window = tk.Tk()
window.title("Aplikacja testowa v.01.b")
window.geometry('350x200')

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(3):
        frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f'Komórka {i}\nKolumna {j}')
        label.pack(padx=5, pady=5)

window.mainloop()
