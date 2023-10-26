import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import * 


def ajout_contact():
    win = tk.Toplevel()
    win.wm_title("Nouveau contact")

    l = tk.Label(win, text="Input")
    l.grid(row=0, column=0)

    b = ttk.Button(win, text="Valider", command=win.destroy)
    b.grid(row=1, column=0)

def popup_showinfo():
    showinfo("Window", "Hello World!")

class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

        self.ajout_contact = ttk.Button(self, text="Ajouter contact", command=ajout_contact)
        self.ajout_contact.pack()

        self.button_showinfo = ttk.Button(self, text="Show Info", command=popup_showinfo)
        self.button_showinfo.pack()
        
    description_label = tk.Label(self, text="Description de la tâche:")
    description_label.pack()
    description_label.place(x=350, y=100)
    description_entry = tk.Entry(self,width=33)
    description_entry.pack()
    description_entry.place(x=300, y=140)

root = tk.Tk()

app = Application(root)

root.mainloop()