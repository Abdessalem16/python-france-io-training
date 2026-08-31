			Impression d’étiquettes

Les sous-sols de la bibliothèque municipale sont remplis de milliers de cartons d’archives. Afin d’éviter de passer leurs journées avec la tête tournée à 90 degrés pour pouvoir lire ce qui est écrit sur ces cartons, les bibliothécaires ont adopté un système d’étiquettes où les mots sont écrits de haut en bas avec une seule lettre par ligne.

Étant donné un texte écrit normalement, sur une seule ligne, vous devez afficher l’étiquette correspondante, avec un seul caractère par ligne.

Contraintes
La ligne de texte contiendra toujours moins de 50 caractères.

Entrée
Une seule ligne de texte.

Sortie
Les caractères du texte, affichés verticalement.

Exemple
entrée :

Don Quichotte
sortie :

D
o
n

Q
u
i
c
h
o
t
t
e
______________________________________
def main():
    texte = input()
    for i in texte:
        print(i)
main()




