À présent, vos spectateurs ont envie que votre robot imprime un motif sur une feuille rectangulaire de n'importe quelle taille, car cela leur sert pour des jeux de géométrie.

Ce que doit faire votre programme :
Votre programme doit lire le nombre de lignes et de colonnes de la feuille, puis le motif à afficher sous la forme d'un caractère. Il doit alors afficher le motif de sorte qu'il remplisse chaque cellule de la feuille.

Exemples
Exemple 1
entrée :

4
9
F
sortie :

FFFFFFFFF
FFFFFFFFF
FFFFFFFFF
FFFFFFFFF
Exemple 2
entrée :

8
3
P
sortie :

PPP
PPP
PPP
PPP
PPP
PPP
PPP
PPP
___________________________________
def feuille(ligne,colonne,motif):
    for i in range(ligne):
        for j in range(colonne):
            print(motif,end="")
        print()

def main():
    ligne=int(input())
    colonne=int(input())
    motif=input()
    feuille(ligne,colonne,motif)      
main()






