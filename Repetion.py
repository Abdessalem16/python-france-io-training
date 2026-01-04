# ce que doit faire votre programme :
# votre programme doit écrire 3 lignes, chacune contenant plusieurs fois de suite une lettre suivie
# du caractère « * » (un-descore en anglais) : la lettre « a » sur la première ligne, la lettre « b »
# sur la deuxième et la lettre « c » sur la troisième.
# Vous disposez déjà d’un modèle où chaque ligne contient 4 lettres :
 
# Cependant, vous vous dites qu’il serait mieux de mettre 30 lettres par ligne.
# Ecrivez un programme qui étend votre modèle. 
# Bien sur, vous utiliserez une boucle pour ne pas fatiguer à écrire vous-meme 30 fois chaque lettre
for aa in range(30):
    print("a",end="_")
print()
for bb in range(30):
    print("b",end="_")
print()
for cc in range(30):
    print("c",end="_")
