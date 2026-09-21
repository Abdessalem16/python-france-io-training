En ces périodes de restrictions budgétaires, il est important de disposer de statistiques détaillées sur la fréquentation de la bibliothèque, afin de justifier de son importance. Ainsi, et depuis plusieurs mois, les bibliothécaires se relaient afin de comptabiliser combien de personnes sont entrées à la bibliothèque à chaque heure de la journée.

À chaque ligne du registre correspond une journée, les entiers présents sur cette ligne représentant la fréquentation à chaque heure. Cela permet de faire des statistiques détaillées mais on aimerait savoir combien de personnes au total sont venues.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Entrée
Un nombre inconnu de lignes, chacune contenant un nombre inconnu d’entiers, ce nombre variant selon les lignes.

Les entiers sont séparés entre eux par un seul espace et il n’y a pas d’espace en fin de ligne.

Sortie
Vous devez indiquer la somme de tous les entiers.

Exemple
entrée :

5
2 2
4 4 4
6 6
3 3
sortie :

39
_______________________
def main():
    somme = 0
    while True:
        try:
            nombres = map(int, input().split())
            for nombre in nombres:
                somme += nombre
        except EOFError:
            break
    print(somme)
main()

