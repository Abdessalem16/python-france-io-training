Vous êtes dans la boutique du plus grand marchand de la ville, à la recherche d'un certain nombre d'ingrédients. Malheureusement pour vous, c'est la période du grand inventaire et cela peut durer très longtemps ! Vous décidez de les aider. À partir du livre de comptes, sur lequel sont indiqués toutes les ventes et achats de chaque produit, vous allez pouvoir rapidement vérifier si les quantités restantes dans les étalages sont bien les bonnes et s'il n'y a pas eu de vols.

Ce que doit faire votre programme :
Un livre de comptes décrit les achats et ventes successives de 10 produits numérotés de 1 à 10. Le livre décrit les opérations depuis une situation où le stock de chacun des produits était de zéro.

Chaque ligne du livre de comptes décrit l'achat (augmentation du stock) ou la vente (réduction du stock) d'une certaine quantité de l'un des produits.

Votre objectif est de déterminer pour chaque produit, la quantité restant dans le stock à l'issue de l'ensemble de ces achats et ventes.

Entrée
La première ligne contient un entier nbOperations : le nombre d'opérations décrites dans le livre de comptes.

Suivent ensuite nbOperations paires d'entiers, où le premier entier de chaque paire est le numéro de l'ingrédient concerné par l'opération, et le deuxième est la quantité. Si la quantité est négative, l'opération est une vente, et si elle est positive, l'opération est un achat du produit indiqué.

Sortie
Vous devez afficher 10 entiers sur la sortie : la quantité restante pour chacun des produits dans l'ordre de leur numéro, une fois l'ensemble des opérations décrites dans le livre effectuées.

Exemple
entrée :

5
1
100
2
50
1
-50
3
20
2
-10
sortie :

50
40
20
0
0
0
0
0
0
0
Commentaires
Faites bien attention au fait que les produits sont numérotés à partir de 1, tandis que l'indice d'un tableau commence à 0.
_____________________________
def main():
    nbOperations=int(input())
    ingrédient=[0]*11
    for i in range(nbOperations):
        numero=int(input())
        quantite=int(input())
        ingrédient[numero]+=quantite
    for elem in range (1,len(ingrédient)):
        print(ingrédient[elem])  
main()    
