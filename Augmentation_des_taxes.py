Augmentation des taxes

Pour faire face à des difficultés financières du gouvernement, la taxe sur les fruits et légumes a été augmentée. Il faut donc recalculer tous les prix afin de prendre en compte cette nouvelle taxe, que les commerçants vont bien entendu répercuter sur les clients.

Ce que doit faire votre programme :
Votre programme doit lire trois nombres décimaux : la valeur actuelle de la taxe sur les fruits et légumes (en pourcentage), la nouvelle valeur de la taxe (en pourcentage), puis le prix actuel d'un légume, taxes comprises, en euros. Il devra calculer et afficher le prix du légume avec la nouvelle valeur de la taxe, arrondi au centime près.

Exemples
Exemple 1
entrée :

5.5
19.6
24.9
sortie :

28.23
Exemple 2
entrée :

21.5
21.5
19.99
sortie :

19.99
Commentaires
On rappelle qu'une taxe de 15% signifie que pour un prix hors-taxe de 100 euros, le prix avec taxe sera de 115 euros.

_________________________
from math import *
def main():
    taxe_actuelle =float(input())
    nouvelle_taxe=float(input())
    Prix_actuel_TTC=float(input())
    Prix_HT=Prix_actuel_TTC/(1+taxe_actuelle/100)
    Nouveau_prix_TTC=Prix_HT*(1+nouvelle_taxe/100)
    print( round(Nouveau_prix_TTC,2))
main()    


