Soirée orageuse

Ce soir, un orage se déchaîne pas loin de chez vous et régulièrement vous voyez des éclairs puis, quelques secondes après, vous entendez le tonnerre. Vous aimeriez savoir à quelle distance se trouve l'orage, afin de savoir s'il se rapproche de vous ou, au contraire, s'éloigne.

Ce que doit faire votre programme :
Votre programme devra lire un décimal, le temps (en secondes) entre le moment où vous voyez l'éclair et le moment où vous entendez le tonnerre. Il devra calculer et afficher la distance entre vous et l'orage, arrondi au kilomètre près.

On supposera que la lumière se déplace instantanément. La vitesse du son dépend de paramètres comme l'altitude, la température...mais on supposera qu'en cette soirée elle vaut 340,29 mètres / seconde.

Exemple
entrée :

3.0
sortie :

1
__________________________

from math import *
def main():
    temps=float(input())
    vitesse=340.29
    distance=(vitesse*temps)/1000
    print(round(distance))
main()    

