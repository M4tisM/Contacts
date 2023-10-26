import tkinter as tk

def valider_inscription():
    pseudo = champ_text1.get()
    email = champ_text2.get()
    mdp = champ_text3.get()
    
    if pseudo and email and mdp:
        print("Inscription validée !")
        print("Pseudo : ", pseudo)
        print("Email : ", email)
        print("MDP : ", mdp)
    else:
        print("Veuillez remplir tous les champs.")

fenetre = tk.Tk()
fenetre.title("Ma premiere interface graphique")

etiquette1 = tk.Label(fenetre, text="Pseudo")
etiquette1.pack()
champ_text1 = tk.Entry(fenetre)
champ_text1.pack()

etiquette2 = tk.Label(fenetre, text="Email")
etiquette2.pack()
champ_text2 = tk.Entry(fenetre)
champ_text2.pack()

etiquette3 = tk.Label(fenetre, text="MDP")
etiquette3.pack()
champ_text3 = tk.Entry(fenetre, show="*")
champ_text3.pack()

bouton = tk.Button(fenetre, text="Valider l'inscription", command=valider_inscription)
bouton.pack()


fenetre.geometry("400x300")

fenetre.mainloop()


