Construction de maisons

Pour la construction de votre nouvelle maison, vous avez calculé la quantité de ciment nécessaire pour construire les fondations. De nature économe, vous souhaitez acheter exactement la quantité nécessaire mais malheureusement le magasin ne vend le ciment qu'en gros sacs. Vous souhaitez calculer combien tout cela va vous coûter.

Ce que doit faire votre programme :
Votre programme devra lire un nombre décimal, la quantité de ciment nécessaire pour les fondations de votre nouvelle maison, en kilos. Sachant que le ciment n'est vendu qu'en sacs de 60 kilos et que un sac coûte 45 euros, votre programme devra afficher le coût total du ciment.

Exemple
entrée :

145.8
sortie :

135
_____________________________________________
from math import *
def main():
    quantiteCiment=float(input())
    indiv=ceil(quantiteCiment/60)
    coute=indiv*45
    print(coute)
main() 
