Le but de ce sujet est d'implémenter une opération classique de traitement d'images appelée "érosion", qui consiste en gros à faire décroître légèrement la taille d'une forme donnée dessinée en noir sur un fond blanc. Le principe est d'effacer (i.e. rendre blanc) tous les pixels de l'image qui ne sont pas entourés de quatre pixels noirs (au-dessus, en-dessous, à droite et à gauche). Dans ce sujet, on répète ce processus d'érosion un certain nombre de fois afin que la transformation soit bien visible.


Remarque : les pixels se trouvant sur le bord de l'image d'origine ne peuvent jamais être entourés par quatre pixels noirs, donc sont toujours blancs sur l'image obtenue.

Limites de temps et de mémoire (Python)
Temps : 3 s sur une machine à 1 GHz.
Mémoire : 32 000 ko.
Contraintes
1 <= N <= 50, où N est le nombre de fois qu'il faut appliquer le processus d'érosion sur toute l'image.
1 <= H,L <= 250, où H et L sont la hauteur et la largeur de l'image.
Entrée
La première ligne contient un entier : N.
La seconde ligne contient deux entiers séparés par des espaces décrivant les dimensions de l'image : H et L.
Chacune des H lignes suivantes contient L caractères qui sont des ‘.’ ou des ‘#’, et qui décrivent l'image. Les '.' correspondent aux pixels blancs, et les '#' aux pixels noirs.
Sortie
Vous devez afficher l'état final de l'image, sous forme d'une grille de ‘.’ et de ‘#’.

Exemple
entrée :

2
12 16
...########.....
..#########.....
.##########.....
################
################
######..#######.
.######.#######.
..############..
...###########..
....#########...
......#######...
........####....
sortie :

................
................
...######.......
..####..##......
..###....##.....
..##......###...
...##.....###...
....##...###....
......#.####....
........###.....
................
................
Commentaires
L'exemple ci-dessus est un rectangle de 12 lignes et 16 colonnes, contenant une forme connexe trouée, que l'on doit éroder 2 fois.

Voici un aperçu d'un exemple plus grand, affiché avec une toute petite police de caractères. L'image de droite est une version érodée 2 fois de celle de gauche :

  ___________________________
def main():
    N = int(input())
    H, L = map(int, input().split())
    image = []
    for i in range(H):
        image.append(list(input()))
    for _ in range(N):
        nouvelle = []
        for i in range(H):
            ligne = []
            for j in range(L):
                if (i == 0 or i == H - 1 or j == 0 or j == L - 1):
                    ligne.append('.')
                elif (image[i][j] == '#' and
                      image[i-1][j] == '#' and
                      image[i + 1][j] == '#' and
                      image[i][j - 1] == '#' and
                      image[i][j + 1] == '#'):
                    ligne.append('#')
                else:
                    ligne.append('.')
            nouvelle.append(ligne)
        image = nouvelle
    for i in image:
        print(''.join(i))

main()
