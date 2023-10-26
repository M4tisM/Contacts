import json
import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, nom, prenom, telephone, email):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
    
    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom, 
            "telephone": self.telephone,
            "email": self.email,
        }
    
    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.telephone} - {self.email}"

    @classmethod
    def from_dict(cls, data):
        return cls(data['nom'], data['prenom'], data['telephone'], data['email'],)

class GestionnaireDeContacts:
    def __init__(self, filename='contacts.json'):
        self.contacts = []
        self.filename = filename
        self.load_from_file()

    def ajouter_contact(self, contact):
        self.contacts.append(contact)
        self.save_to_file()

    def supprimer_contact(self, nom, prenom):
        for contact in self.contacts:
            if contact.nom == nom and contact.prenom == prenom:
                self.contacts.remove(contact)
                self.save_to_file()
                return True
        return False

    def afficher_contacts(self):
        for contact in self.contacts:
            print(contact)

    def rechercher_contact(self, nom, prenom):
        for contact in self.contacts:
            if contact.nom == nom and contact.prenom == prenom:
                return contact
        return None
    
    def save_to_file(self):
        with open(self.filename, 'w') as file:
            data = [contact.to_dict() for contact in self.contacts]
            json.dump(data, file)

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact.from_dict(item) for item in data]
        except FileNotFoundError:
            self.contacts = []

class Application(tk.Tk):

    def __init__(self, gestionnaire):
        super().__init__()
        self.gestionnaire = gestionnaire
        self.title("Gestionnaire de contacts")
        self.geometry("500x400")

        self.listbox = tk.Listbox(self, height=15, width=50)
        self.btn_ajouter = tk.Button(self, text="Ajouter", command=self.ajouter_contact)
        self.btn_supprimer = tk.Button(self, text="Supprimer", command=self.supprimer_contact)
        self.btn_rechercher = tk.Button(self, text="Rechercher", command=self.rechercher_contact)
        self.btn_afficher = tk.Button(self, text="Afficher tous", command=self.afficher_contacts)

        self.listbox.pack(pady=20)
        self.btn_ajouter.pack(fill=tk.X)
        self.btn_supprimer.pack(fill=tk.X)
        self.btn_rechercher.pack(fill=tk.X)
        self.btn_afficher.pack(fill=tk.X)

        self.afficher_contacts()

    def ajouter_contact(self):
        nom = simpledialog.askstring("Ajouter", "Nom:")
        prenom = simpledialog.askstring("Ajouter", "Prénom:")
        telephone = simpledialog.askstring("Ajouter", "Téléphone:")
        email = simpledialog.askstring("Ajouter", "Email:")

        if nom and prenom and telephone and email:
            contact = Contact(nom, prenom, telephone, email)
            self.gestionnaire.ajouter_contact(contact)
            self.afficher_contacts()

    def supprimer_contact(self):
        selection = self.listbox.curselection()
        if selection:
            nom, prenom = self.listbox.get(selection[0]).split()[0:2]
            self.gestionnaire.supprimer_contact(nom, prenom)
            self.afficher_contacts()

    def rechercher_contact(self):
        nom = simpledialog.askstring("Rechercher", "Nom:")
        prenom = simpledialog.askstring("Rechercher", "Prénom:")
        contact = self.gestionnaire.rechercher_contact(nom, prenom)
        if contact:
            messagebox.showinfo("Recherche", str(contact))
        else:
            messagebox.showwarning("Recherche", "Contact non trouvé!")

    def afficher_contacts(self):
        self.listbox.delete(0, tk.END)
        for contact in self.gestionnaire.contacts:
            self.listbox.insert(tk.END, f"{contact.nom} {contact.prenom} - {contact.telephone} - {contact.email}")


if __name__ == "__main__":
    gestionnaire = GestionnaireDeContacts()
    app = Application(gestionnaire)
    app.mainloop()

