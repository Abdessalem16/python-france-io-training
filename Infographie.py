En infographie, lorsque l'on désire créer l'image associée à une scène 3D, il est nécessaire de dessiner les faces qui la composent dans le bon ordre. En effet, certaines faces en recouvrent d'autres et doivent donc être dessinées après ces dernières.

Vous travaillez sur un moteur de rendu simplifié pour lequel les faces à dessiner sont des rectangles dont les côtés sont parallèles aux bords de l'image. Vous connaissez l'ordre dans lequel ces faces rectangulaires doivent être dessinées ainsi que la couleur de chacun et souhaitez écrire un programme qui crée l'image tant attendue.

L'image a nbLignes lignes et nbColonnes colonnes. Les lignes sont indexées de 0 à nbLignes − 1 et les colonnes de 0 à nbColonnes − 1. La couleur de chaque rectangle est définie par un caractère. Par défaut, chaque pixel est de la couleur ..

Limites de temps et de mémoire (Python)
Temps : 0,5 s sur une machine à 1 GHz.
Mémoire : 16 000 ko.
Contraintes
1 <= nbLignes, nbColonnes <= 100, le nombre de lignes et de colonnes de l'image.
0 <= nbRectangles <= 100, le nombre de rectangles à dessiner.
Entrée
La première ligne de l'entrée contient deux entiers : nbLignes et nbColonnes.

La seconde ligne contient un unique entier : nbRectangles.

Les nbRectangles lignes suivantes contiennent chacune quatre entiers iLig1, iCol1, iLig2 et iCol2 décrivant les coordonnées des bords respectivement en haut, à gauche, en bas et à droite du rectangle considéré, ainsi qu'un caractère couleur indiquant la couleur du rectangle.

Les rectangles doivent être dessinés dans l'ordre dans lequel ils sont donnés en entrée.

Sortie
Votre programme doit afficher nbLignes lignes de nbColonnes caractères chacune décrivant l'image obtenue.

Exemple
entrée :

9 19
4
1 3 7 5 o
5 2 6 16 -
1 12 7 14 u
2 1 2 16 s
sortie :

...................
...ooo......uuu....
.ssssssssssssssss..
...ooo......uuu....
...ooo......uuu....
..----------uuu--..
..----------uuu--..
...ooo......uuu....
...................
___________________________________________________________________
def main():
    nbLignes,nbColonnes = map(int,input().split())
    nbRectangles = int(input())
    image = []
    for i in range (nbLignes):
        image.append(['.'] * nbColonnes)
    for i in range(nbRectangles):
        ilig1 , icol1 ,ilig2 , icol2 ,couleur = input().split()
        ilig1 = int(ilig1)
        icol1 = int(icol1)
        ilig2 = int(ilig2)
        icol2 = int(icol2)
        for ligne in range(ilig1, ilig2 +1):
            for colonne in range(icol1,icol2 +1):
                image[ligne][colonne] = couleur
    for ligne in image:
        print(''.join(ligne))    
    
main()


