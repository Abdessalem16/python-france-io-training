# Construction d'une pyramide
# Les enfants de la classe de maternelle décident de construire une très grande tour à l'aide de petits cubes en bois. Ils savent exactement la forme qu'ils souhaitent pour leur tour, mais ils n'arrivent pas à savoir s'ils auront suffisamment de cubes pour la construire. Ils vous demandent de les aider à calculer le nombre de cubes nécessaires.
# Ce que doit faire votre programme :
# L'objectif est de construire une tour à l'aide de petits cubes en bois, sachant que la forme de cette tour consiste en un ensemble de grands cubes placés les uns au-dessus des autres. La base de la tour est un cube de taille 17×17×17, c'est-à-dire composé de 17×17×17 = 4 913 petits cubes. Sur ce cube est posé un autre cube de taille 15×15×15. Au-dessus de ce dernier se trouve un cube de 13×13×13. La tour continue ainsi jusqu'à atteindre le sommet, qui consiste en un cube de taille 1×1×1.
# Code :
Nombre =0
Nombre = 0
for loop in range(1,18,2) :
	Nombre = Nombre+loop*loop*loop
print(Nombre)
