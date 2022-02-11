import tkinter as tk

window = tk.Tk()

powitanie = tk.Label(text="Witaj Programisto!",
                     foreground="white",
                     background="black",
                     width=25,
                     height=10)
button = tk.Button(text="Kliknij mnie!",
                   width=25,
                   height=5,
                   fg="blue",
                   bg="yellow"
                   )
entry = tk.Entry(fg="yellow", bg="blue", width=50)
name = entry.get()
print(name)

button.pack()
powitanie.pack()
entry.pack()

window.mainloop()
