		Résumés de livres

À la recherche de l'unique livre contenant les informations qui vous intéressent, vous souhaitez utiliser le grand index de la bibliothèque, celui dans lequel chaque livre est normalement référencé. En particulier, chaque titre de livre est accompagné d'un petit résumé de celui-ci, afin de pouvoir donner plus d'informations que le titre seul.

Or, le résumé de certains livres a parfois été fait très rapidement et ne contient pas suffisamment d'informations. Par exemple "Animaux" n'est pas un résumé correct !

Étant donnée la longueur minimale acceptable d'un résumé, vous décidez d'analyser l'index et de signaler automatiquement aux bibliothécaires les livres ayant des résumés trop courts, afin qu'ils puissent les compléter.

Contraintes
La longueur de chaque titre de livre et de chaque résumé n'excèdera jamais 1000 caractères.

Entrée
Sur la première ligne, un entier nbLivres, le nombre total de livres.

Sur la deuxième ligne, un entier longueurMinimale, la longueur minimale acceptable pour un résumé de livre.

Les 2 * nbLivres lignes suivantes contiennent, de manière alternée, un titre de livre et le résumé associé.

Sortie
Vous devez afficher, à raison d’un par ligne, le titre des livres dont le résumé n'est pas assez long, c'est-à-dire dont la longueur n'est pas au moins égale à longueurMinimale.

Exemple
entrée :

2
60
En attendant Godot
Deux clochards attendent Godot. Mais Godot ne vient pas.
Le Livre de la jungle
Moogli est eleve par les loups, Baloo l’ours, Bagheera la panthere. Shere Khan veut le manger, mais Moogli le tue. Il finit par vivre dans un village d'hommes.
sortie :

En attendant Godot
____________________________________
def main():
    nbLivres =int(input())
    longueurMinimal=int(input())
    mini=""
    for i in range (nbLivres):
        titre=input()
        resume=input()
        if len(resume)<longueurMinimal:
            mini=titre
            print(mini)         
main()


