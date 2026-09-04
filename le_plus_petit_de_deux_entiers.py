Vos apprentis ont remarqué dans votre manuel une fonction min, qui prend deux valeurs en paramètre et fournit la plus petite des deux. Ils se demandent comment est codée cette fonction.

Ce que doit faire votre programme :
Écrivez une fonction nommée min2, qui prend deux entiers en paramètres et retourne le plus petit. Pour démontrer l'utilisation de cette fonction, vous lirez 10 entiers sur l'entrée, utiliserez votre fonction pour conserver uniquement le plus petit des 10, puis vous l'afficherez à la fin.

Exemple
entrée :

4
3
6
2
6
8
9
8
5
4
sortie :

2
___________________________________________________________
def min2(En1,En2):
    petit=En2
    if En1<En2:
        petit=En1
    elif En1>En2:
        petit=En2
    return petit
def main():
    mini=10000000
    mini2=10000000
    for i in range (5):
        n1=int(input())
        n2=int(input())
        mini=min2(n1,n2)
        if mini<mini2:
            mini2=mini
    print(mini2)
main()

