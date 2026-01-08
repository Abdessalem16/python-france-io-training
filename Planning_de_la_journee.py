#                                                                               Planning de la journée
# vous venez d’arriver au bord d’un grand lac que vous devez
# contourner, par un coté ou l’autre, peu importe.
# Vous avez réussi à trouver une carte décrivant la position 
# Exacte de tous les villages le long de la route qui 
# Longe la rive du lac.
# Sachant que vous pouvez marcher 50 km dans la journée,
# Vous aimeriez savoir dans combien de villages différents vous pourriez
# Dormir la nuit prochaine.
# Ce que doit faire votre programme :
# Votre programme doit d’abord lire un entier décrivant votre position
# Actuelle sur la route, sous la forme d’un nombre de kilomètres
# Par rapport au début de la route.
# Ensuite, il doit lire un entier donnant le nombre de villages.
# Pour chaque village, il doit lire un entier décrivant la position 
# De ce village le long de cette même route. 
# Votre programme doit alors afficher le nombre de villages qui se trouvent 
# A une distance inférieure ou égale à 50 km de votre position actuelle .
# Code :
myPosition = int(input())
nombredeville = int(input())
res=0
for loop in range(nombredeville):
    PosVille = int(input())
    if PosVille>myPosition:
        if PosVille - myPosition <=50:
            res +=1 
    else:
        if myPosition - PosVille <=50:
            res +=1 
print(res)
