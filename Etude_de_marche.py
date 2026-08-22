Étude de marché

Afin de partir dans un long voyage, à la recherche de produits exotiques, les marchands prévoient toujours d'emmener avec eux des produits locaux afin de les vendre au cours du trajet. Pour décider quels produits emmener, ils ont fait une petite étude de marché auprès de la population, en demandant à chaque personne d'indiquer LE produit qu'elle serait prête à acheter (celui qu'elle préfère donc).

Ce que doit faire votre programme :
On vous donne le numéro du produit préféré par différentes personnes. Écrivez un programme qui indique pour chaque numéro de produit, le nombre de personnes dont c'est le produit préféré.

Entrée
Les deux premiers entiers à lire sont le nombre total de produits nbProduits et le nombre de personnes nbPersonnes (nbPersonnes <= 1000) ayant exprimé leur souhait.

On lit ensuite nbPersonnes entiers : les numéros des produits préférés des différentes personnes. Les produits sont numérotés de 0 à nbProduits - 1.

Sortie
Vous devez afficher nbProduits entiers : pour chaque produit dans l'ordre de leur numéro, affichez le nombre de personnes qui le préfèrent.

Exemple
entrée :

4
10
0
2
2
1
2
2
0
2
3
0
sortie :

3
1
5
1
________________________
def main():
    nbProduits=int(input())
    nbPersonne=int(input())
    produit=[0]*nbProduits
    for i in range (nbPersonne):
        prefere=int(input())
        produit[prefere]+=1
    for elem in produit:
        print(elem)  
main()    
 
