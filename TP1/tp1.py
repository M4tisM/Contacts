import tkinter as tk
from tkinter import messagebox
import pickle
from tkcalendar import Calendar

class TaskManager:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.geometry("1920x1080") 
        self.fenetre.title("Gestionnaire de tâches")
        
        self.tasks = []

        
        sujet_label = tk.Label(fenetre, text="Description :")
        sujet_label.pack()
        self.task_listbox = tk.Listbox(fenetre, selectmode=tk.SINGLE, height=20, width=300) 
        self.task_listbox.pack()

        sujet_label = tk.Label(fenetre, text="Sujet :")
        sujet_label.pack()
        self.add_task_entry = tk.Entry(fenetre, width=300)
        self.add_task_entry.pack()

        date = Calendar(fenetre, selctmode="day")
        date.pack()

        bouton_Ajout_List = tk.Button(fenetre, text="Ajouter une tâche", command=self.ajout_liste, padx=50)
        bouton_Ajout_List.pack()

        mark_done_button = tk.Button(fenetre, text="Marquer comme terminée", command=self.mark_done, padx=27)
        mark_done_button.pack()

        remove_task_button = tk.Button(fenetre, text="Supprimer la tâche", command=self.remove_task, padx=47)
        remove_task_button.pack()

        save_button = tk.Button(fenetre, text="Enregistrer", command=self.save_tasks, padx=69)
        save_button.pack()

        load_button = tk.Button(fenetre, text="Charger", command=self.load_tasks, padx=76)
        load_button.pack()

    def ajout_liste(self):
        liste = self.add_task_entry.get()
        if liste:
            self.tasks.append(liste)
            self.task_listbox.insert(tk.END, liste)
            self.add_task_entry.delete(0, tk.END)

    def mark_done(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_listbox.itemconfig(index, {'bg': 'green'})
            self.tasks[index] = f'[Done] {self.tasks[index]}'


    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.task_listbox.delete(index)
            del self.tasks[index]

    def save_tasks(self):
        with open("tasks.pickle", "wb") as file:
            pickle.dump(self.tasks, file)
        messagebox.showinfo("Enregistré", "Liste de tâches enregistrée avec succès.")

    def load_tasks(self):
        try:
            with open("tasks.pickle", "rb") as file:
                self.tasks = pickle.load(file)
            self.task_listbox.delete(0, tk.END)
            for task in self.tasks:
                self.task_listbox.insert(tk.END, task)
            messagebox.showinfo("Chargé", "Liste de tâches chargée avec succès.")
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Aucun fichier de liste de tâches trouvé.")

if __name__ == "__main__":
    fenetre = tk.Tk()
    app = TaskManager(fenetre)
    fenetre.mainloop()