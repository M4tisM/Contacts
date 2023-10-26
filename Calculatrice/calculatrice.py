import tkinter as tk

# Fonction pour mettre à jour l'affichage
def bouton_clic(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Fonction pour évaluer l'expression
def evaluer():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erreur")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculatrice")

# Entrée
entry = tk.Entry(fenetre, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Boutons
boutons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for bouton in boutons:
    tk.Button(fenetre, text=bouton, command=lambda b=bouton: bouton_clic(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Bouton "C"
tk.Button(fenetre, text='C', command=lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val)

# Bouton "Evaluer"
tk.Button(fenetre, text='=', command=evaluer).grid(row=row_val, column=col_val + 1)

# Exécution de la boucle principale de l'interface
fenetre.mainloop()
