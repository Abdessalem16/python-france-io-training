		Analyse de fréquence


En étudiant différents types de textes (romans, lois, article de journaux…), on se rend compte que non seulement les mots utilisés ne sont pas les mêmes mais aussi que leurs longueurs sont statistiquement différentes : par exemple, il est beaucoup plus fréquent de trouver de longs mots complexes dans un article de loi que dans un livre pour enfants.

Afin d’essayer de déterminer automatiquement à quelle catégorie appartient un livre, on souhaite déterminer le nombre de mots de 1 lettre, 2 lettres, 3 lettres… qu’il contient.

Contraintes
Le texte contient un ensemble de mots, séparés par des espaces, sans aucun signe de ponctuation.

Chaque mot contient au plus 100 caractères.

Entrée
La première ligne contient deux entiers : nbLignes et nbMots.

Chacune des nbLignes lignes suivantes contient nbMots mots.

Sortie
Pour chaque longueur de mot possible, et uniquement s’il y avait des mots de cette longueur dans le texte, vous devez afficher sur une ligne la longueur et le nombre de mots de cette longueur, séparés par un deux-points (il faut mettre un espace de chaque côté du deux-points).

Exemple
entrée :

2 7
Qui vole un oeuf vole un boeuf
Une abeille vaut mieux que mille mouches
sortie :

2 : 2
3 : 3
4 : 4
5 : 3
7 : 2
______________________________________________________
def main():
    nbLignes,nbMots= map(int,input().split(" "))
    tab=[0]*101
    for i in range (nbLignes):
        mot=input().split(" ")
        for elem in mot:
            tab[len(elem)]+=1
    for j in range(len(tab)):
        if tab[j]!=0:
            print("{} : {}".format(j,tab[j]))
main()
