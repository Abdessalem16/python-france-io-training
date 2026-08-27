					Petites fiches et gros travail


Afin de faciliter la recherche d’un livre particulier, la bibliothèque municipale s’est dotée d’un système très perfectionné, à base de fiches en carton. Malheureusement, un bibliothécaire stagiaire s’est trompé dans la création des fiches et, à chaque fois, il a écrit le nom de l’auteur avant le titre du livre, au lieu de faire l’inverse !

Votre travail consiste à lire le contenu d’une fiche et à remettre les informations dans l’ordre.

Contraintes
Il y a toujours 6 titres de livres (et donc 6 noms d’auteurs) sur chaque fiche.

Les titres de livres et les noms d’auteurs font toujours moins de 200 caractères de long.

Entrée
Pour chacun des 6 livres, une ligne contenant le nom de l’auteur, et une ligne contenant le titre du livre.

Sortie
Pour chacun des livres, vous devez afficher sur une ligne le titre du livre, puis sur la ligne suivante le nom de l’auteur.

Exemple
entrée :

George ORWELL
1984
Pierre BOULLE
La planete des singes
Isaac ASIMOV
Les robots
Rene BARJAVEL
La nuit des temps
Arthur C. CLARKE
2001 : L'odyssee de l'espace
H.G. WELLS
La guerre des mondes
sortie :

1984
George ORWELL
La planete des singes
Pierre BOULLE
Les robots
Isaac ASIMOV
La nuit des temps
Rene BARJAVEL
2001 : L'odyssee de l'espace
Arthur C. CLARKE
La guerre des mondes
H.G. WELLS
___________________________________

def main():
    nom_auteur=[0]*6
    titre_livre=[0]*6
    for i in range(6):
        nom_auteur[i]=input()
        titre_livre[i]=input()
    for i in range(6):
        print(titre_livre[i])
        print(nom_auteur[i])   
main()
