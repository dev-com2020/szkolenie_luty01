import tkinter as tk

window = tk.Tk()

text_box = tk.Text()
text_box.insert("2.5", "Witaj!")
text_box.insert("1.2", "Programisto!")
# w = text_box.get("1.0")
w = text_box.get("1.0", tk.END)
print(w)
text_box.pack()
window.mainloop()
