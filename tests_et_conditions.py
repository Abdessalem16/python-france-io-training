# tests et conditions 
# Transport des bagages
# Alors que vous quittez le village, les villageois vous offrent de nombreux cadeaux :
# Provisions, vêtements, chauds, boissons …
# Vous ne pourrez jamais porter tout cela tout seul ;
# Vous décidez donc de donner une partie de ces objets à votre robot,
# Après les avoir rassemblés en de gros paquets, tous de même masse.
# Aura-t-il la force de tout porter ?
# Ce que doit faire votre programme :

# Votre programme lira deux entiers : 
# Le nombre de paquets et le poids d’un paquet. 
# Si le poids total est strictement supérieur  à 105 kg.
# Votre programme devra alors afficher le texte « Surcharge ! » 
# Code :
NombrePaquet = int(input())
PoidPaquet = int(input())
PoidTotal = NombrePaquet*PoidPaquet
if PoidTotal >105:
    print("Surcharge !")
