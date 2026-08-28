	Fiches d’inscription


Au sein de la bibliothèque municipale, toutes les personnes souhaitant emprunter un livre doivent s'enregistrer en indiquant leurs noms et prénoms sur une fiche individuelle conservée à l'accueil.

L'habitude veut qu'ils écrivent d'abord leur nom puis leur prénom, ce qui permet de classer les fiches par ordre alphabétique et permet de rapidement retrouver la fiche qu'on cherche.

Malheureusement, depuis un mois, dans toutes les nouvelles fiches créées les personnes ont indiqué en premier leur prénom puis leur nom !

Votre travail consiste à lire ces couples de prénoms et noms et à les afficher dans le bon ordre.

Contraintes
Chaque nom et prénom est au plus de longueur 100 et ne contient pas d'espace.

Entrée
Sur la première ligne, un entier nbPersonnes : le nombre total de personnes concernées.

Sur chacune des nbPersonnes suivantes, un prénom et un nom, séparés par une espace.

Sortie
Pour chaque personne, vous devez écrire sur la même ligne son nom, puis son prénom, séparés par une espace.

Exemple
entrée :

4
Alan Turing
Ada Lovelace
Donald Knuth
Claude Shannon
sortie :

Turing Alan 
Lovelace Ada 
Knuth Donald
Shannon Claude
________________________________________
def main():
    nbPersonnes = int(input())
    tab=[]
    for i in range(nbPersonnes):
        ele = input().split()
        tab+=ele
    for i in range(len(tab)):
        if i%2==0:
            print()
            aux=tab[i]
            tab[i]=tab[i+1]
            tab[i+1]=aux
        print(tab[i],end=" ")
    print()
main()


