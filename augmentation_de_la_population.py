Ces dernières années, la population de votre ville a très fortement augmenté, grâce à un fort taux de natalité. Cela pose cependant un certain nombre de problèmes, notamment une pénurie de logements ! Le maire a décidé de s'occuper du problème et souhaiterait estimer l'évolution future de la population.

Ce que doit faire votre programme :
Votre programme devra lire un entier, la population actuelle de la ville, puis un nombre décimal, la croissance prévue de la population, en pourcentage. Il devra alors afficher la nouvelle population de la ville sous la forme d'un nombre entier. On considérera, par convention, qu'une population de 31,4 habitants signifie qu'il y a 31 habitants, on ne compte donc que les habitants « entiers » !

Exemples
Exemple 1
entrée :

123
7.0
sortie :

131
Exemple 2
entrée :

456
-5.5
sortie :

430
______________________
from math import *
def main():
    population=int(input())
    pourcentage=float(input())
    res=0
    res=population*((pourcentage/100)+1)
    print(floor(res))    
main()    

