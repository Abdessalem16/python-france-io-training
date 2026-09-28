Le Gomoku est un jeu de plateau à deux joueurs, dans lequel pour gagner, chaque joueur doit réussir à aligner 5 pions sur des cases consécutives d'un plateau, horizontalement, verticalement ou en diagonale. Le plateau est une grille carrée, de dimension quelconque.
Ecrivez un programme qui lit en entrée le contenu d'une partie de Gomoku, et détermine si l'un des joueurs a gagné.

Limites de temps et de mémoire (Python)
Temps : 1 s sur une machine à 1 GHz.
Mémoire : 1 000 ko.
Contraintes
1 <= N <= 40, où N est le nombre de lignes/colonnes du plateau utilisé pour la partie.
Entrée
La première ligne de l'entrée contient un entier N : le nombre de colonnes et de lignes du plateau de Gomoku.
Chacune des N lignes suivantes contient N entiers, séparés par des espaces, correspondant au contenu des cases d'une ligne du plateau. L'entier vaut 0 si la case est vide, 1 si elle contient un pion du joueur 1, et 2 pour un pion du joueur 2.

Sortie
Votre programme doit afficher une ligne contenant un entier : le numéro du joueur gagnant (1 ou 2), ou 0 si aucun des joueurs n'a aligné 5 pions.
Exemple
entrée :

6
0 0 2 0 1 0
0 1 2 2 2 1
0 0 2 0 1 0
0 0 2 1 0 0
0 0 1 0 0 0
0 1 0 0 0 0
sortie :

1
________________________
def main():
    N = int(input())

    grille = []

    for i in range(N):
        grille.append(list(map(int, input().split())))
    for ligne in range(N):
        for colonne in range(N - 4):
            if grille[ligne][colonne] != 0:
                joueur = grille[ligne][colonne]

                if (grille[ligne][colonne + 1] == joueur and
                    grille[ligne][colonne + 2] == joueur and
                    grille[ligne][colonne + 3] == joueur and
                    grille[ligne][colonne + 4] == joueur):

                    print(joueur)
                    return
    for ligne in range(N - 4):
        for colonne in range(N):

            if grille[ligne][colonne] != 0:
                joueur = grille[ligne][colonne]

                if (grille[ligne + 1][colonne] == joueur and
                    grille[ligne + 2][colonne] == joueur and
                    grille[ligne + 3][colonne] == joueur and
                    grille[ligne + 4][colonne] == joueur):

                    print(joueur)
                    return
    for ligne in range(N - 4):
        for colonne in range(N - 4):

            if grille[ligne][colonne] != 0:
                joueur = grille[ligne][colonne]

                if (grille[ligne + 1][colonne + 1] == joueur and
                    grille[ligne + 2][colonne + 2] == joueur and
                    grille[ligne + 3][colonne + 3] == joueur and
                    grille[ligne + 4][colonne + 4] == joueur):

                    print(joueur)
                    return
    for ligne in range(N - 4):
        for colonne in range(4, N):

            if grille[ligne][colonne] != 0:
                joueur = grille[ligne][colonne]

                if (grille[ligne + 1][colonne - 1] == joueur and
                    grille[ligne + 2][colonne - 2] == joueur and
                    grille[ligne + 3][colonne - 3] == joueur and
                    grille[ligne + 4][colonne - 4] == joueur):

                    print(joueur)
                    return
    print(0)


main()




