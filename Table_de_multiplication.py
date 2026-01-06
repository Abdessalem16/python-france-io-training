# Table de multiplication
# C’est l’heure du cours de mathématiques et aujourd’hui les enfants vont travailler
# La multiplication. Malheureusement, l’institutrice ne retrouve que la petite table de multiplication, qui va jusqu’à 5 fois 5, mais la grande
# Table, qui va jusqu’à 20 fois 20.
# Elle souhaiterait que vous lui imprimiez une nouvelle table allant jusqu’à 20 fois 20, pour qu’elle
# puisse l’afficher au mur.
# Ce que doit faire votre programme :
# Voici à quoi ressemble la table de multiplication allant jusqu’à 5 fois 5.
# Ecrivez un programme qui affiche une table de multiplication allant jusqu’à 20 fois 20.
for i in range(1,6):
    for j in range(1,6):
        print(j*i, end=" ")
    print()
