Banquet municipal
_____________
certo, le maire décide de vous inviter au grand banquet qu'il organise. Le maire se charge lui-même de faire le plan de table mais il change toujours d'avis et les serveurs doivent constamment changer de place les petites affiches sur lesquelles sont indiqués les noms des personnes.

Afin de l'aider, vous lui proposez d'utiliser votre robot pour déterminer la position de chaque personne après tous les changements décidés par le maire.

Afin de simplifier le problème, on suppose que chaque personne est identifiée par un numéro et qu'il n'y a qu'une seule très grande table.

Ce que doit faire votre programme :
Votre programme devra lire deux entiers : le nombre total de positions sur la table (au maximum 1000) et le nombre de changements de positions. Il devra ensuite lire, pour chaque position, un entier : le numéro de la personne qui doit, actuellement, s'installer à cette position.

Il faut lire ensuite les changements exprimés sous la forme de deux entiers chacun : position1 et position2. Un changement (position1, position2) signifie que les deux personnes qui étaient à ses positions doivent échanger leurs places (les positions sont indexées à partir de 0).

Vous devrez afficher, pour chaque position, le numéro de la personne qui s'y trouve une fois tous les changements faits.

Exemple
entrée :

5
3
1
2
3
4
5
1
2
1
3
4
0
sortie :

5
4
2
3
1
Commentaires
Evolution des numéros dans l'exemple :

Au début : 1,2,3,4,5
Après le changement (1, 2) : 1,3,2,4,5
Après le changement (1, 3) : 1,4,2,3,5
Après le changement (4, 0) : 5,4,2,3,1
_______________________________________
def main():
    nbpositions=int(input())
    nbchangements = int(input())
    numpersonne=[0]*nbpositions
    for i in range (nbpositions):
        numpersonne[i]=int(input())
    for i in range (nbchangements):
        change1=int(input())
        change2=int(input())
        aux=numpersonne[change1]
        numpersonne[change1]=numpersonne[change2]
        numpersonne[change2]=aux
    for elem in numpersonne:
        print(elem)
    print()     
main()


