Les jeunes attirent à présent votre attention sur des suites de nombres entiers qui semblent avoir certaines similitudes, surtout sur leurs terminaisons.

Dans cette suite, le nombre qui suit un nombre terme est :

si terme est pair, terme ÷ 2 ;
sinon, terme × 3 + 1.
Vos compagnons ont remarqué que, quel que soit le nombre dont on part, en allant d'un terme à l'autre en suivant ces propriétés, on finit toujours par tomber sur le nombre 1. Ainsi, ils souhaitent que leur écriviez une fonction qui, pour un terme, renvoie le terme suivant dans la suite.

Ce que doit faire votre programme :
Votre programme doit afficher les termes de la suite qui succèdent à celui fourni sur l'entrée, séparés par des espaces, jusqu'à ce que le nombre 1 soit atteint.

Important : vous devez utiliser une fonction qui prend un terme en paramètre, et retourne le suivant.

Exemple
entrée :

7
sortie :

22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
______________________________
def suite (terme):
    if terme %2==0:
        terme=terme//2
    else:
        terme=terme*3+1
    return terme
    
def main():
    terme=int(input())
    while terme!=1:
        terme=suite(terme)
        print(terme,end=" ")
    
main()