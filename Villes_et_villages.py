# 6.structures avancées
# Villes et villages
# Au cours de votre périple, vous traversez de nombreux lieux habités. Pour chacun d'entre eux, vous notez soigneusement sa population. Après quelques semaines de voyage, vous avez vraiment l'impression qu'il y beaucoup de villages et très peu de villes.
# Ce que doit faire votre programme :
# On vous donne le nombre d'habitants d'un certain nombre de lieux que vous visitez.
# Une ville étant un lieu dont la population est strictement supérieure à 10 000 habitants, déterminez combien de lieux sont des villes.
# Votre programme doit lire un entier : le nombre de lieux. Il doit ensuite lire, pour chaque lieu, un entier donnant le nombre de gens qui y habitent. Votre programme doit alors afficher le nombre de villes.
# Code :
nombreLieux = int(input())
lieux=0
for loop in range(nombreLieux):
    population = int(input())
    if population> 10000:
        lieux+=1
print(lieux)
