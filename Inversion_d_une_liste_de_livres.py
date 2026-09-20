			Inversion d’une liste de livres

Souhaitant améliorer ses connaissances scientifiques, votre jeune assistante Ada, vous a demandé de lui créer une liste de livres « à lire absolument », en les classant par ordre de priorité, selon l'intérêt de chaque livre. Un peu distrait(e), vous avez bien créé cette fiche mais en les classant dans l’ordre inverse, du moins intéressant au plus intéressant !

Afin d’éviter de devoir tout refaire, vous décidez d’écrire un petit programme pour inverser rapidement cette liste.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
Chaque titre de livre contient au plus 100 caractères.

Entrée
La première ligne contient un entier nbLivres, le nombre de livres.

Les nbLivres lignes suivantes contiennent chacune un titre de livre.

Les livres sont classés du moins intéressant au plus intéressant.

Sortie
L’ensemble des titres de livres, un titre par ligne, triés du plus intéressant au moins intéressant.

Exemple
entrée :

7
Germinal
Le petit prince
Le meilleur des mondes
L'ecume des jours
L'Odyssee
Les miserables
Crime et Chatiment
sortie :

Crime et Chatiment
Les miserables
L'Odyssee
L'ecume des jours
Le meilleur des mondes
Le petit prince
Germinal
__________________
def main():
    nbLivres=int(input())
    titre=[""]*nbLivres
    for i in range(nbLivres):
        titre[i]=input()
    for elem in range(nbLivres-1,-1,-1):
        print(titre[elem])
main()

