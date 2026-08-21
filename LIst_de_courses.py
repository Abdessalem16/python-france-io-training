Les stocks des ingrédients nécessaires à la réalisation de l'onguent commencent à se vider et les savants vous chargent d'aller en ville acheter une certaine quantité de chaque ingrédient, afin de pouvoir continuer la production pendant le prochain mois.

Le comptable étant particulièrement pointilleux, il vous donnera exactement la quantité d'argent dont vous avez besoin, pas une pièce de plus. Heureusement vous savez à l'avance le prix de chaque ingrédient et la quantité dont vous avez besoin.

Ce que doit faire votre programme :
Il y a 10 ingrédients et ils ont tous un prix au kilo différent : 9, 5, 12, 15, 7, 42, 13, 10, 1 et 20.

Votre programme devra lire 10 entiers, le poids (en kilogrammes) qu'il faut acheter pour chaque ingrédient. Il devra calculer le coût total de ces achats.

Exemple
entrée :

1
1
1
1
1
1
1
1
1
1
sortie :

134
______________________________
def main():
    ingrédients=[9, 5, 12, 15, 7, 42, 13, 10, 1,20]
    achat=0
    for i in range (10):
        poid=int(input())
        achat=achat+(ingrédients[i]*poid)
    print(achat)        
main()    

