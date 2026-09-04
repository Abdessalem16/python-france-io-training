Vos spectateurs aiment beaucoup la dentelle comportant une ligne de « X », une ligne de dièses « # » et une ligne de « i ». Ils voudraient que vous écriviez un programme pour leur en fournir la quantité qu'ils désirent.

Ce que doit faire votre programme :
Votre programme doit lire la longueur de la dentelle, puis l'afficher sous la forme de trois lignes remplies respectivement de « X », de « # » et de « i ».

Exemple
entrée :

5
sortie :

XXXXX
#####
iiiii
__________________________
def dentelle(nombre):
    for x in range(nombre):
        print('X',end="")
    print()
    for o in range(nombre):
        print('#',end="")
    print()
    for i in range(nombre):
        print('i',end="")  

def main():
    nombre=int(input())
    dentelle(nombre)      
main()