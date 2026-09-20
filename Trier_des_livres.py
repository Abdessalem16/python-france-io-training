Un enfant un peu turbulent a complètement renversé une étagère pleine de livres ! Tous les livres sont désormais à terre, en vrac, et c’est à vous de tout remettre sur l’étagère dans le bon ordre.

À vous donc de trier ces livres par ordre alphabétique.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
Chaque titre de livre contient au plus 100 caractères.

Entrée
La première ligne contient un entier nbLivres, le nombre de livres.

Les nbLivres lignes suivantes contiennent chacune un titre de livre.

Les titres ne contiennent que des lettres majuscules ou des espaces.

Sortie
L’ensemble des titres de livres, un titre par ligne, triés selon l’ordre alphabétique.

Exemple
entrée :

7
LE ROUGE ET LE NOIR
DES SOURIS ET DES HOMMES
GUERRE ET PAIX
LE PARFUM
ALICE AU PAYS DES MERVEILLES
NOTRE DAME DE PARIS
LE VIEIL HOMME ET LA MER
sortie :

ALICE AU PAYS DES MERVEILLES
DES SOURIS ET DES HOMMES
GUERRE ET PAIX
LE PARFUM
LE ROUGE ET LE NOIR
LE VIEIL HOMME ET LA MER
NOTRE DAME DE PARIS
______________________________
def main():
    nbLivres=int(input())
    titre=[""]*nbLivres
    for i in range(nbLivres):
        titre[i]=input().upper()
    titre.sort()
    for elem in range(nbLivres):
        print(titre[elem])
main()


