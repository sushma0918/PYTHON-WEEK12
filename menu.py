#24331A05G8
import tkinter as tk
from tkinter import messagebox, filedialog
root = tk.Tk()
root.title("GUI Application")
root.geometry("400x400")
#  Listbox + Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)
scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(frame, yscrollcommand=scroll.set, width=30, height=10)
for i in range(1, 21):
    listbox.insert(tk.END, f"Item {i}")
listbox.pack(side=tk.LEFT)
scroll.config(command=listbox.yview)
# Messagebox
def show_msg():
    try:
        selected = listbox.get(listbox.curselection())
        messagebox.showinfo("Selected Item", selected)
    except:
        messagebox.showwarning("Warning", "No item selected!")
tk.Button(root, text="Show Selected", command=show_msg).pack(pady=5)
# Filedialog 
def open_file():
    file = filedialog.askopenfilename()
    if file:
        messagebox.showinfo("File Selected", file)
tk.Button(root, text="Open File", command=open_file).pack(pady=5)
# Menu
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
# Menubutton
def choose(option):
    messagebox.showinfo("Option Selected", option)
menubtn = tk.Menubutton(root, text="Options", relief=tk.RAISED)
menu2 = tk.Menu(menubtn, tearoff=0)
menu2.add_command(label="Option 1", command=lambda: choose("Option 1"))
menu2.add_command(label="Option 2", command=lambda: choose("Option 2"))
menu2.add_command(label="Option 3", command=lambda: choose("Option 3"))
menubtn.config(menu=menu2)
menubtn.pack(pady=10)
root.mainloop()
