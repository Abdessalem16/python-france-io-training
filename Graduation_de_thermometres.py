#                                                                 Graduation de thermomètres
# Les habitants du village utilisent beaucoup de thermomètres différents : certains pour l'été, d'autres pour l'hiver, d'autres pour la température de l'eau, etc. Ce qui change d'un thermomètre à l'autre, ce sont les valeurs de la température minimale et de la température maximale lisibles sur la graduation. Les habitants aimeraient pouvoir imprimer facilement la graduation des températures possibles pour chaque thermomètre.
# Ce que doit faire votre programme :
# Étant données deux températures entières tempMin et tempMax, votre programme doit afficher toutes les températures comprises entre les deux, bornes incluses.
# Code :
tempMin = int(input())
tempMax =int(input())
for loop in range(tempMin,tempMax+1):
    print(loop)

