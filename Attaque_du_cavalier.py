Vous devez écrire un programme qui détermine dans une partie d'échecs, si un cavalier peut prendre une pièce de l'adversaire.
Rappelons que les échecs se jouent sur un plateau carré de 8 cases par 8. Un cavalier se déplace en avancant d'une case horizontalement ou verticalement, puis en allant en diagonale, sans revenir en arrière. Le cavalier peut se déplacer même si la case intermédiaire de son déplacement contient une pièce (amie ou ennemie). La figure suivante montre toutes les possibilités de déplacements de deux cavaliers :



Limites de temps et de mémoire (Python)
Temps : 1 s sur une machine à 1 GHz.
Mémoire : 1 000 ko.
Entrée
On vous donne la description d'un plateau de jeu sous la forme de 8 lignes de 8 caractères. Les lettres majuscules représentent les pièces blanches, les minuscules les pièces noires, et les '.' représentent les cases vides. Les cavaliers sont représentés par la lettre 'c' (ou 'C'), et les autres pièces par d'autres lettres de l'alphabet.
Sortie
Votre programme doit afficher "yes" si un cavalier blanc peut se déplacer vers une case contenant une pièce noire (donc la prendre) et "no" dans le cas contraire.
Exemples
Exemple 1
entrée :

tc.drf.t
ppp.pppp
...p...c
.....f..
..C..P..
..P.D.P.
PP.....P
T.F.RFCT
sortie :

yes
Exemple 2
entrée :

.......R
........
..C.....
........
........
.....p..
........
r.......
sortie :

no
Commentaires
Dans l'exemple 1, le cavalier blanc situé vers le centre peut prendre le pion noir ('p') situé deux cases au dessus, et une case à droite.
Dans l'exemple 2, il n'y a qu'un seul cavalier blanc, qui ne peut pas prendre de pièce noire.

Remarque : on considère le roi noir comme n'importe-autre quelle pièce, même si dans les règles des échecs, on ne peut pas "prendre" le roi.



____________________________________________________________________________________
def main():
    grille=[]
    for i in range(8):
        grille.append(input())
    for j in range(8):
        for t in range(8):
            if grille[j][t]=='C':
                pos=[
                    (-2,-1),(-2,1),
                    (2,-1),(2,1),
                    (-1,-2),(-1,2),
                    (1,-2),(1,2)
                ]
                for dl, dc in pos:
                    new_l=j+dl
                    new_c=t+dc
                    if 0 <= new_l < 8 and 0 <= new_c < 8:
                        case1=grille[new_l][new_c]
                        if case1.islower() and case1 !='.':
                            print("yes")
                            return
    print("no")
main()
