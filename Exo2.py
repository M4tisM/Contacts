prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom de famille : ").upper()
age = input("Entrez votre âge : ")
taille = input("Entrez votre taille (en cm) : ")

fruits = input("Entrez vos fruits préférés, séparés par des virgules : ")
fruits_preferes = fruits.split()


print("Bonjour ", prenom, " ", nom, ", " + "vous avez ", age, " " + "ans" + " " + "et mesurez ", taille, " " + "cm.")
print(fruits_preferes)

produit = input("Nom du produit : ")
prix = input("Prix du prouit : ")

print("Produit : ", produit)
print("Prix : ", prix, "€")
