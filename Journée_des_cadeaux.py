Journée des cadeaux

Dans la ville de Largition, la tradition veut que, une fois par mois, les habitants les plus riches fassent un cadeau aux habitants les moins riches. Cela permet de maintenir une bonne ambiance malgré les inévitables différences de richesses.

Un habitant est considéré comme riche si sa fortune est plus grande que celle de la moitié de la population. Calculer, chaque mois, qui est riche ou pas est un long travail, aussi lorsque le maire a entendu parlé de vos talents, il vous a demandé votre aide.

Ce que doit faire votre programme :
Il devra lire un premier entier, le nombre d'habitants (au plus 1000) puis, pour chaque habitant il devra lire sa fortune, un entier. Il devra calculer puis afficher une valeur permettant de dire facilement si une personne est riche ou pas, simplement en regardant si la fortune de cette personne est plus grande ou plus petite que cette valeur.

Deux cas peuvent se présenter :

Si le nombre d'habitants est impair, par exemple si leurs fortunes sont 10, 5, 12, 8, 3 alors la valeur recherchée est 8. En effet, il y aura alors 2 personnes "riches" (10 et 12), 2 "moins riches" (3 et 5) et 1 juste au milieu (8) qui ne donnera ni recevra de cadeau.
Si le nombre d'habitants est pair, par exemple si leurs fortunes sont 10, 5, 12, 8, 3, 9 alors la valeur recherchée est entre 8 et 9. Il y a en effet 3 personnes "riches" (9, 10 et 12) et 3 "moins riches" (3, 5 et 8). Par convention on prendra la valeur 8.5, c'est-à-dire la moyenne de 8 et 9.
Exemples
Exemple 1
entrée :

5
10
5
12
8
3
sortie :

8
Exemple 2
entrée :

6
10
5
12
8
3
9
sortie :

8.5
________________________
def main():
    nbhabitant=int(input())
    tab=[0]*nbhabitant
    for i in range (nbhabitant):
        tab[i]=int(input())
    tab.sort()
    res=0
    if not (nbhabitant % 2 == 0 ):
        print(tab[nbhabitant//2])
    else:
        print((tab[nbhabitant//2]+tab[nbhabitant//2-1])/2)    
main()

