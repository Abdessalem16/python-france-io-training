Lire ou ne pas lire, telle est la question

Les employés de la bibliothèque, constamment entourés de livres, n’ont jamais le temps de lire tous les livres qu’ils souhaiteraient. Chacun a donc mis au point son propre algorithme de sélection, et l’un d’entre eux a choisi un système basé sur la longueur des titres des livres !

Sur une étagère sont alignés tous les livres qui l’intéressent. Chaque mois, cette personne commence par lire le premier livre présent sur l’étagère, puis le second et ainsi de suite jusqu’à la fin. Seulement, elle ne lira un livre que si son titre est strictement plus long que ceux de tous les livres qu’elle a lus pendant le mois. Si ce n’est pas le cas, elle enlève le livre de l’étagère, sans le lire.

Étant donnée une liste de titres de livres possibles pour le mois suivant, donnés dans l’ordre où ils apparaissent dans l’étagère, vous devez déterminer lesquels elle va lire.

Contraintes
Chaque titre de livre contiendra au plus 1000 caractères.

Entrée
Sur la première ligne, un entier nbLivres, le nombre total de livres.

Les nbLivres lignes suivantes contiennent chacune un titre de livre.

Sortie
La liste des titres respectant la règle donnée dans l’énoncé.

Exemple
entrée :

6
Les Facheux
Le Malade imaginaire
Les Femmes savantes
Les Fourberies de Scapin
L'Avare
Le Bourgeois gentilhomme
sortie :

Les Facheux
Le Malade imaginaire
Les Fourberies de Scapin
__________________________________________________________________
def main():
   nbLivres=int(input())
   maxxi=-1000
   for i in range (nbLivres):
       titre=input()
       if len(titre)>maxxi:
           maxxi=len(titre)
           print(titre)
main()


