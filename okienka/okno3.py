import tkinter as tk

window = tk.Tk()

border = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE
}

for rn, r in border.items():
    frame = tk.Frame(master=window, relief=r, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=rn)
    label.pack()

# frame = tk.Frame()
# frame2 = tk.Frame()
#
# label = tk.Label(master=frame, text="Jestem numer 1")
# label2 = tk.Label(master=frame2, text="Jestem numer 2")
#
# label.pack()
# label2.pack()
# frame.pack()
# frame2.pack()

window.mainloop()
