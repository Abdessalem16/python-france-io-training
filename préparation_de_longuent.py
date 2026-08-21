	Préparation de l'onguent
Parmi les chimistes de l'université, le plus expérimenté est Alcophante et c'est donc lui qui a la charge de la préparation de l'onguent guérisseur. Malheureusement, il connait quelques problèmes de mémoire et ne se souvient jamais quelle quantité de chaque ingrédient il faut mettre ! Afin de l'aider, vous décidez de programmer votre robot pour qu'il puisse répondre à Alcophante, à chaque fois que celui-ci en aura besoin.

Ce que doit faire votre programme :
Il y a 10 ingrédients dans la recette et les quantités nécessaires pour chacun sont (en grammes) : 500, 180, 650, 25, 666, 42, 421, 1, 370 et 211.

Votre programme doit lire un entier, le numéro d'un ingrédient (compris entre 0 et 9) et afficher la quantité associée à cet ingrédient.

Exemple
entrée :

3
sortie :

25
__________________________________
def main():
    ingrédient=[500,180,650,25,666,42,421,1,370,211]
    indice=int(input())
    print(ingrédient[indice])
main()    
