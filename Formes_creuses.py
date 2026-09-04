				Formes creuses


Vos spectateurs veulent davantage de dessins.

Ce que doit faire votre programme :
Écrivez un programme qui affiche une ligne de « X », un rectangle de « # », et un triangle de « @ ». Les deux formes doivent être creuses (remplies avec des espaces).

L'entrée comporte quatre entiers, un par ligne :

le nombre de « X » de la ligne à afficher ;
le nombre de lignes du rectangle de « # » ;
le nombre de colonnes du rectangle ;
le nombre de lignes du triangle de « @ ».
Vous devez afficher les trois formes successivement, avec une ligne blanche entre chaque forme, comme le montre l'exemple.

Votre objectif doit être d'obtenir le code source le plus simple et clair possible, en le décomposant en fonctions.

Exemple
entrée :

15
5
12
6
sortie :

XXXXXXXXXXXXXXX

############
#          #
#          #
#          #
############

@
@@
@ @
@  @
@   @
@@@@@@
Commentaires
Attention : le nombre de lignes ou de colonnes peut être égal à 1.
______________________________________
def traingle(ligne):
    for i in range (ligne):
        for j in range(ligne):
            if j==0 or i ==ligne-1 or j==i:
                print("@",end="")
            else:    
                print(" ",end="")
        print()       
def rectangle(ligne,colonne):
    for i in range (ligne):
        for j in range(colonne):
            if j==0 or i ==ligne-1 or i==0 or j==colonne-1:
                print("#",end="")
            else:    
                print(" ",end="")
        print()       

def lligne(ligne1):
    for i in range(ligne1):  
        print("X",end="")
    print()       

def main():
    ligne =int(input())
    ligne2 =int(input())
    colonne =int(input())
    t =int(input())
    lligne(ligne)
    print()
    rectangle(ligne2,colonne)
    print()
    traingle(t)
main()






