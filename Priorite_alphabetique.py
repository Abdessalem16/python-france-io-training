			Priorité alphabétique
La plupart des livres de la bibliothèque dorment sagement sur les étagères, sans que personne ne les ouvre pendant de longs mois, voire des années. Mais il y a toujours quelques livres très demandés et, parfois, un même livre est demandé en même temps par deux personnes !

Afin d’éviter les soupçons de favoritisme, la règle suivante a été mise en place : si deux personnes demandent simultanément le même ouvrage, alors la personne qui l’aura est celle dont le nom est alphabétiquement le plus petit.

Vous devez écrire un programme permettant de résoudre automatiquement les éventuels litiges.

Contraintes
Chaque nom est composé uniquement de lettres majuscules, sans espaces.

Sa longueur sera au plus égale à 50.

Entrée
Sur la première ligne, le nom de la première personne.

Sur la seconde ligne, le nom de la seconde personne.

Sortie
Le nom le plus petit selon l’ordre alphabétique, c’est-à-dire le nom qui vient en premier selon cet ordre.

Si les deux noms sont égaux, il ne faut rien afficher car la personne a voulu tricher en faisant deux demandes d’un seul coup.

Exemples
Exemple 1
entrée :

KANT
DESCARTES
sortie :

DESCARTES
Exemple 2
entrée :

ROUSSEAU
VOLTAIRE
sortie :

ROUSSEAU
________________________________________
def main():
    nompremier = input()
    nomsecond = input()
    if nompremier<nomsecond:
        print(nompremier)
    if  nompremier>nomsecond:
        print(nomsecond)     
main()

