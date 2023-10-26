import tkinter as tk
import json
from tkinter import messagebox

# Fonction pour ajouter un contact à la liste
def ajouter_contact():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    telephone = entry_telephone.get()
    contact = f"{nom} {prenom} - {telephone}"
    contact_listbox.insert(tk.END, contact)
    contacts.append(contact)
    popup.destroy()

# Fonction pour afficher la fenêtre pop-up
def afficher_popup():
    global popup, entry_nom, entry_prenom, entry_telephone
    popup = tk.Toplevel(fenetre)
    popup.title("Ajouter un contact")
    
    label_nom = tk.Label(popup, text="Nom:")
    label_nom.pack()
    entry_nom = tk.Entry(popup)
    entry_nom.pack()
    
    label_prenom = tk.Label(popup, text="Prénom:")
    label_prenom.pack()
    entry_prenom = tk.Entry(popup)
    entry_prenom.pack()
    
    label_telephone = tk.Label(popup, text="Téléphone:")
    label_telephone.pack()
    entry_telephone = tk.Entry(popup)
    entry_telephone.pack()
    
    valider_button = tk.Button(popup, text="Valider", command=ajouter_contact)
    valider_button.pack()
    popup.geometry("300x200")

def sauvegarder_en_json():
    nom_fichier = contact_listbox.curselection()
    if nom_fichier:
        with open(f"{nom_fichier}.json", "w") as f:
            json.dump(contacts, f)
        messagebox.showinfo("Sauvegarde", f"Liste de tâches '{nom_fichier}' enregistrée avec succès.")
    else:
        messagebox.showerror("Erreur", "Veuillez saisir un nom de liste.")


# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion de contacts")

contacts = []

ajouter_button = tk.Button(fenetre, text="Ajouter un contact", command=afficher_popup, padx=50)
ajouter_button.pack()
ajouter_button.place(x=125, y=25)


contact_listbox = tk.Listbox(fenetre, selectmode=tk.SINGLE, height=40,width=50)
contact_listbox.pack()
contact_listbox.place(x=75, y=75)


supprimer_button = tk.Button(fenetre, text="Supprimer le contact", padx=47)
supprimer_button.pack()
supprimer_button.place(x=125, y=725)


sauvegarder_button = tk.Button(fenetre, text="Sauvegarder en JSON", command=sauvegarder_en_json, padx=30)
sauvegarder_button.pack()
sauvegarder_button.place(x=125, y=755)

fenetre.geometry("550x1080")
fenetre.mainloop()