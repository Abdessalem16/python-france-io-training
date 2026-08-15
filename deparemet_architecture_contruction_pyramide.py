Les habitants adorent les constructions en forme de pyramide ; de nombreux bâtiments officiels ont d'ailleurs cette forme. Pour fêter les 150 ans de la construction de la ville, le gouverneur a demandé la construction d'une grande et majestueuse pyramide à l'entrée de la ville. Malheureusement, en ces périodes de rigueur budgétaire, il y a peu d'argent pour ce projet. Les architectes souhaitent cependant construire la plus grande pyramide possible étant donné le budget prévu.


Trois exemples de pyramides, de hauteur 1, 2 et 3
Ce que doit faire votre programme :
Votre programme doit d'abord lire un entier : le nombre maximum de pierres dont pourra être composée la pyramide. Il devra ensuite calculer et afficher un entier : la hauteur de la plus grande pyramide qui pourra être construite, ainsi que le nombre de pierres qui sera nécessaire.

Exemples
Exemple 1
entrée :

20
sortie :

3
14
Exemple 2
entrée :

26042
sortie :

42
25585
________________________________
def main():
    Pierre=int(input())
    somme=0
    etage=0
    while somme+(etage*etage)<=Pierre:
        somme+=etage*etage
        etage+=1
    print(etage-1)
    print(somme)
main()    

