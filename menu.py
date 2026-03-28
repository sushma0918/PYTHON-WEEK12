#24331A05G8
import tkinter as tk
from tkinter import messagebox, filedialog
root = tk.Tk()
scroll = tk.Scrollbar(root)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(root, yscrollcommand=scroll.set)
for i in range(20):
    listbox.insert(tk.END, f"Item {i}")
listbox.pack()
scroll.config(command=listbox.yview)
def show_msg():
    messagebox.showinfo("Info", "Hello!")
tk.Button(root, text="Show Message", command=show_msg).pack()
def open_file():
    filedialog.askopenfilename()
tk.Button(root, text="Open File", command=open_file).pack()
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)
root.mainloop()