# Traversée du pont

# Vous arrivez devant un pont que vous devez absolument emprunter pour arriver avant la nuit au village situé de l'autre côté de la rivière. Cependant, la traversée du pont n'est pas gratuite et le tarif dépend de votre chance au jeu. En effet, le gardien vous demande de lancer deux dés et le prix dépendra des valeurs que vous obtiendrez. Vous décidez d'écrire un programme pour vérifier qu'il applique bien le bon tarif.
# Ce que doit faire votre programme :
# Votre programme doit lire deux entiers, compris
# Entre 1 et 6, la valeur de chaque dé.
# Si la somme est supérieure ou égale à 10, alors
# Vous devez payer une taxe spéciale (36 pièces).
# Sinon, vous payez deux fois la somme des valeurs
# Des deux dés. 
# Votre programme devra afficher selon le cas le texte
# « taxe spéciale ! » ou bien « taxe régulière », puis la somme à payer 
# (sans indiquer l’unité )

# _____________________
# Code :
nombre1= int(input())
nombre2=int(input())
Somme = nombre1+nombre2
if Somme >=10:
    print("Taxe spéciale ! ")
    print(36)
else:
    print("Taxe régulière")
    print(Somme*2)
