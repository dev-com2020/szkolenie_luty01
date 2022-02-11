import tkinter as tk

window = tk.Tk()

text_box = tk.Text()
text_box.insert("1.0","Witaj!")
w = text_box.get("1.0")
print(w)
text_box.pack()
window.mainloop()