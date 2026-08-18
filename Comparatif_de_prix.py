
Comparatif de prix

Lors du marché hebdomadaire, de nombreux maraîchers viennent vendre de très gros légumes, en indiquant pour chacun trois informations : son poids, le nombre de jours qui se sont écoulés depuis sa cueillette, et son prix.

Il n'est vraiment pas évident de comparer les prix de légumes de différentes tailles, et des habitants vous demandent de les aider à répondre à cette question. Vous décidez d'écrire un programme qui calcule le prix au kg de chaque légume à partir des informations disponibles.

Ce que doit faire votre programme :
Votre programme doit d'abord lire le nombre de légumes mis en vente. Ensuite, pour chacun, il doit lire 3 nombres décimaux : son poids, son âge (en nombre de jours depuis la cueillette), et son prix de vente. Votre programme doit ensuite afficher pour chaque légume son prix au kg (au fur et à mesure que les légumes sont présentés).

Exemple
entrée :

2
7.0
5.0
14.0
9.5
2.3
7.6
sortie :

2.0
0.8

_______________

def main():
    legumes=int(input())
    for i in range(legumes):
        poids=float(input())
        age=float(input())
        prixVente=float(input())
        print(prixVente/poids)     
main()    

