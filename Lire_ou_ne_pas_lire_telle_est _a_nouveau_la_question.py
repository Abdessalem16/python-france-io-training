	Lire ou ne pas lire, telle est (à nouveau) la question

Un des employés de la bibliothèque avait mis au point son propre algorithme de sélection des livres à lire, basé sur la longueur des titres des livres. Il s’en est lassé et se base maintenant sur l'ordre alphabétique des titres des livres.

Sur une étagère sont alignés tous les livres qui l’intéressent. Chaque mois, cette personne prend le premier livre de l’étagère, puis le second et ainsi de suite jusqu’à la fin. Seulement, elle ne lira un livre que si son titre est situé, selon l’ordre alphabétique, après chacun des livres qu’elle a lus pendant le mois. Si ce n’est pas le cas, elle enlève le livre de l’étagère, sans le lire.

Étant donnée la liste de titres de livres possibles pour le mois suivant, donnés dans l’ordre où ils apparaissent dans l’étagère, vous devez déterminer lesquels elle va lire.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
Chaque titre de livre contiendra au plus 100 caractères.

Entrée
Sur la première ligne, un entier nbLivres, le nombre total de livres.

Les nbLivres lignes suivantes contiennent chacune un titre de livre.

Les titres ne contiennent que des lettres majuscules ou des espaces.

Sortie
La liste des titres respectant la règle donnée dans l’énoncé.

Exemple
entrée :

8
ANNA KARENINE
JACQUES LE FATALISTE ET SON MAITRE
DIX PETITS NEGRES
CENT ANS DE SOLITUDE
LA PESTE
LA FERME DES ANIMAUX
SUR LA ROUTE
SA MAJESTE DES MOUCHES
sortie :

ANNA KARENINE
JACQUES LE FATALISTE ET SON MAITRE
LA PESTE
SUR LA ROUTE
_______________________________________
def main():
    nbLivres = int(input())
    dernier=""
    for i in range(nbLivres):
        titre=input().upper()
        if titre>dernier:
            print(titre)
            dernier = titre
main()


