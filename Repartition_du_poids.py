	Répartition du poids

Après seulement quelques heures de route, au sein de cette longue caravane de marchands, certains chevaux montrent déjà des signes de fatigue alors que d'autres sont en pleine forme. En cherchant la raison de ce phénomène, vous vous rendez compte que certaines charrettes sont bien plus lourdes que les autres ! Vous décidez donc de mieux répartir le poids, afin que toutes les charrettes aient exactement le même poids.

Ce que doit faire votre programme :
On vous décrit les charrettes qui composent une caravane, en vous donnant pour chacune, le poids des marchandises qu'elle transporte.

Votre programme doit déterminer quel poids ajouter ou retirer à chaque charrette, pour qu'elles transportent toutes ensuite le même poids, et ce sans modifier le poids total transporté par l'ensemble des charrettes de la caravane.

Entrée
L'entrée commence par un entier nbCharrettes (nbCharrettes <= 3000) : le nombre de charrettes de la caravane.

Les nbCharrettes lignes suivantes décrivent chacune une charrette par un nombre décimal : le poids qu'elle transporte initialement.

Sortie
Vous devez afficher nbCharrettes nombres décimaux sur la sortie : le poids à ajouter à chaque charrette (ce qui revient à en retirer si ce nombre est négatif), dans le même ordre que celui de l'entrée. Il n'y a pas d'arrondis à faire.

Exemple
entrée :

5
40.0
12.0
20.0
5.0
33.0
sortie :

-18.0
10.0
2.0
17.0
-11.0
Commentaires
Dans cet exemple, on modifie toutes les charettes pour qu'elles transporte chacune un poids de 22.0, soit un total de 110 pour la caravane, comme au départ.
_________________________
def main():
    nbCharrettes=int(input())
    somme=0
    ancien=[0]*nbCharrettes
    for i in range (nbCharrettes):
        Poid=float(input())
        ancien[i]=Poid
        somme+=Poid
    moy=somme/nbCharrettes
    for elem in ancien:
        print(moy-elem)
main()    

