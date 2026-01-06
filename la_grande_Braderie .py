# la grande Braderie 
# chaque année, c’est la tradition, une grande braderie est 
# organisée dans le village et toute la région y participe.
# C’est l’occasion pour les habitants de vendre quelques 
# Petits objets qui trainent dans le grenier depuis des années.
# Afin que cela soit équitable, chaque vendeur doit avoir
# A sa disposition la même longueur de rue pour installer ses 
# Affaires.
# Pour délimiter les emplacements, des marques sont faites
# A la peinture à intervalles réguliers. 
# Les villageois vous demandent votre aide pour calculer
# Les positions (c’est-à-dire la distance par rapport au début de la rue)
# Auxquelles ces marques doivent être faites.
# Ce que doit faire votre programme :
# Il y a trois entiers à lire : position de départ positionDepart,
# La largeur d’un emplacement largeurEmplacement et 
# Le nombre de vendeurs nbVendeurs.
# Vous devez afficher une suite de nombres, partant de positionDepart
# Et augmentant de largeurEplacement à chaque fois.
# Il y a au total nbVendeurs augmentations à faire. 
# Vous devez afficher la valeur de chacun des nombres de la suite.
#Code :
positionDepart = int(input())
largeurEmplacement = int(input())
nbVendeurs =int(input())

for loop in range(nbVendeurs+1):
    print(positionDepart)
    positionDepart=positionDepart+largeurEmplacement


