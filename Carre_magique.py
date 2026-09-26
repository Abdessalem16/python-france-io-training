Un carré magique est une grille carrée dans laquelle des nombres sont placés de telle sorte que la somme des nombres de chaque colonne, chaque ligne et de chacune des deux diagonales soit la même. De plus, Le carré doit contenir une fois chaque nombre, de 1 au nombre de cases de la grille.
Ecrivez un programme qui vérifie si une grille de nombres est un carré magique.

Limites de temps et de mémoire (Python)
Temps : 1 s sur une machine à 1 GHz.
Mémoire : 1 000 ko.
Contraintes
1 <= N <= 20, où N est le nombre de lignes et de colonnes de la grille.
Entrée
La première ligne de l'entrée contient un entier N : le nombre de cases du côté de la grille de nombres.
Chacune des N lignes suivantes contient N entiers séparés par des espaces : les nombres d'une ligne de la grille.

Sortie
Vous devez afficher une ligne sur la sortie, contenant le mot "yes" si le carré fourni est un carré magique, et "no" sinon.
Exemple
entrée :

3
6 1 8
7 5 3
2 9 4
sortie :

yes
Commentaires
Chacun des chiffres de 1 à 9 apparaît exactement une fois dans la grille. De plus, toutes les colonnes, lignes et les deux diagonales de cette grille ont pour somme 15. En effet :
Lignes :
6 + 1 + 8 = 15
7 + 5 + 3 = 15
2 + 9 + 4 = 15

Colonnes :
6 + 7 + 2 = 15
1 + 5 + 9 = 15
8 + 3 + 4 = 15

Diagonales :
6 + 5 + 4 = 15
8 + 5 + 2 = 15


________________________
def main():
    N = int(input())
    grille = []
    somme =0
    for ligne in range (N):
        grille.append(list(map(int,input().split())))
    somme = sum (grille[0])
    res = True
    for i in range (N):
        if sum(grille[i])!=somme:
            res=False
    for colonne in range(N):
        somme_colonne =0
        for ligne in range (N):
            somme_colonne += grille[ligne][colonne]
        if somme_colonne != somme:
            res = False
    somme_diag1 =0
    for i in range (N):
        somme_diag1 +=grille[i][i]
    if somme_diag1 != somme:
        res = False
    somme_diag2 =0
    for i in range(N):
        somme_diag2 += grille[i][N - 1- i]
    if somme_diag2 !=somme:
        res= False
    nombres= []
    for ligne in range(N):
        for colonne in range(N):
            nombres.append(grille[ligne][colonne])
    nombres.sort()
    for i in range(N*N):
        if nombres[i] != i+1:
            res = False
    if res:
        print("yes")
    else:
        print("no")
        
main()

