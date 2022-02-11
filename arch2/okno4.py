import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame2 = tk.Frame(master=window, width=75, height=75, bg="yellow")
frame3 = tk.Frame(master=window, width=30, height=30, bg="blue")

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
