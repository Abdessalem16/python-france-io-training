# le plus beau Karva
# Lors du concours général agricole, l'épreuve reine, celle que tout fermier rêve de remporter, est celle du plus beau Karva (l'équivalent de notre taureau). La compétition est basée sur des règles strictes : chaque animal reçoit une note en fonction de ses caractéristiques et celui qui a reçu la plus grande note est déclaré champion. Vous souhaiteriez connaître les résultats avant tout le monde ; aussi, vous décidez d'écrire un programme qui vous donnera la note de chacun des Karvas en compétition.
# Ce que doit faire votre programme :
# Votre programme doit d’abord lire le nombre de Karvas en compétition.
# Ensuite, pour chaque Karva, il doit :
# Lire 4 entiers : son poids, son âge, la longueur
# De ses cornes et la hauteur au garrot ;
# Afficher sa note , sachant qu’elle s’obtient en multipliant la longueur des cornes par la hauteur au garrot, valeur à laquelle on ajoute le poids.
# Code :
NombreKarvas = int(input())
for loop in range(NombreKarvas):
    Poid=int(input())
    age=int(input())
    Cornes=int(input())
    garrot = int(input())
    Result=Cornes*garrot+Poid
    print(Result)
