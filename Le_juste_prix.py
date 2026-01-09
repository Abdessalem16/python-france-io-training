# Le juste prix
# Vous arrivez dans un village le jour du marché, de nombreux marchands vendent la spécialité locale, de délicieuses petites galettes. Elles ont toutes l'air d'être identiques, donc vous décidez d'acheter les moins chères.
# Ce que doit faire votre programme :
# Votre programme doit lire un entier nbMarchands (non nul) puis les nbMarchands entiers suivants, qui indiquent le prix des galettes chez chaque marchand, de la position 1 à la position nbMarchands. Votre programme devra ensuite afficher la position du plus petit de ces prix. En cas d'égalité entre deux prix, on prendra la position la plus grande. Tous les prix et positions sont positifs et ne dépassent pas 1 million.
# Code :
nbMarchands = int (input())
moins =1000000
pos=0
for loop in range(1,nbMarchands+1):
    prix= int(input())
    if prix <=moins:
        moins = prix
        pos = loop
print(pos)
