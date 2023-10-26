import tkinter as tk
from tkinter import messagebox
import json


def ajouter_tache():
    description = description_entry.get()
    date = date_entry.get()
    if description and date:
        tache = {"description": description, "date": date, "terminee": False,}
        taches.append(tache)
        afficher_taches()
        description_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

def marquer_terminee():
    selected = tache_listbox.curselection()
    if selected:
        index = int(selected[0])
        taches[index]["terminee"] = True
        tache_listbox.itemconfig(index, {'bg': 'pale green'})
        afficher_taches()
    else:
        messagebox.showerror("Erreur", "Veuillez selectionner une tâche.")


def supprimer_tache():
    selected = tache_listbox.curselection()
    if selected:
        index = int(selected[0])
        del taches[index]
        afficher_taches()
    else:
        messagebox.showerror("Erreur", "Veuillez selectionner une tâche.")


def afficher_taches():
    tache_listbox.delete(0, tk.END)
    for tache in taches:
        description = tache["description"]
        date = tache["date"]
        terminee = " (Terminée)" if tache["terminee"] else ""
        # bg_color = 'pale green' if terminee else 'lightcoral'
        # test changer le backgroud pas concluant
        tache_listbox.insert(tk.END, f"{description} - {date}{terminee}")
        tache_listbox.update()

def enregistrer_liste():
    nom_fichier = nom_liste_entry.get()
    if nom_fichier:
        with open(f"{nom_fichier}.json", "w") as f:
            json.dump(taches, f)
        messagebox.showinfo("Sauvegarde", f"Liste de tâches '{nom_fichier}' enregistrée avec succès.")
        nom_liste_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez saisir un nom de liste.")

def charger_liste():
    nom_fichier = nom_liste_entry.get()
    if nom_fichier:
        try:
            with open(f"{nom_fichier}.json", "r") as f:
                taches.clear()
                taches.extend(json.load(f))
                afficher_taches()
                nom_liste_entry.delete(0, tk.END)
        except FileNotFoundError:
            messagebox.showwarning("Avertissement", "Aucun fichier de liste de tâches trouvé.")
    else:
        messagebox.showerror("Erreur", "Veuillez saisir un nom de liste.")

fenetre = tk.Tk()
fenetre.title("Gestion de tâches")

# Création de la liste de tâches
taches = []

# Création des widgets
description_label = tk.Label(fenetre, text="Description de la tâche:")
description_label.pack()
description_label.place(x=350, y=100)
description_entry = tk.Entry(fenetre,width=33)
description_entry.pack()
description_entry.place(x=300, y=140)

date_label = tk.Label(fenetre, text="Date d'échéance:")
date_label.pack()
date_label.place(x=350, y=180)
date_entry = tk.Entry(fenetre,width=33)
date_entry.pack()
date_entry.place(x=300, y=220)

ajouter_button = tk.Button(fenetre, text="Ajouter une tâche", command=ajouter_tache, padx=50)
ajouter_button.pack()
ajouter_button.place(x=300, y=260)

tache_listbox = tk.Listbox(fenetre, selectmode=tk.SINGLE, height=40,width=50)
tache_listbox.pack()
tache_listbox.place(x=1000, y=100)

marquer_button = tk.Button(fenetre, text="Marquer comme terminée", command=marquer_terminee,padx=27)
marquer_button.pack()
marquer_button.place(x=300, y=300)

supprimer_button = tk.Button(fenetre, text="Supprimer la tâche", command=supprimer_tache, padx=47)
supprimer_button.pack()
supprimer_button.place(x=300, y=340)

nom_liste_label = tk.Label(fenetre, text="Nom de la liste:")
nom_liste_label.pack()
nom_liste_label.place(x=350, y=380)
nom_liste_entry = tk.Entry(fenetre,width=33)
nom_liste_entry.pack()
nom_liste_entry.place(x=300, y=420)

enregistrer_button = tk.Button(fenetre, text="Enregistrer la liste", command=enregistrer_liste,padx=50)
enregistrer_button.pack()
enregistrer_button.place(x=300, y=460)

charger_button = tk.Button(fenetre, text="Charger la liste", command=charger_liste, padx=57)
charger_button.pack()
charger_button.place(x=300, y=500)

fenetre.geometry("1920x1080")
fenetre.mainloop()