			Écriture en miroir
Alors que vous parcourez de très vieux livres, à la recherche d’indications sur le livre qui vous intéresse en particulier, vous tombez sur un langage que vous ne connaissez pas !

À y regarder de plus près, il s’agit des mêmes mots que ceux que vous utilisez tous les jours, mais tout le texte est écrit "en miroir" : toutes les lettres sont écrites de droite à gauche.

Bien que vous arriviez à déchiffrer les textes présents dans ces livres, cela vous prend beaucoup de temps et vous fatigue beaucoup. Vous décidez d’écrire un programme pour remettre automatiquement dans l’ordre les textes.

Contraintes
Chaque ligne de texte contient moins de 1000 caractères.

Entrée
Sur la première ligne, un entier nbLignes, le nombre de lignes du texte.

Les nbLignes suivantes contiennent chacune une ligne de texte qu’il faut inverser.

Sortie
Pour chaque ligne du texte original, vous devez l’afficher de manière inversée.

Exemple
entrée :

2
tniop a ritrap tuaf li riruoc ed tres en neiR
egangiomet nu tnos ne eutroT al te erveiL eL
sortie :

Rien ne sert de courir il faut partir a point
Le Lievre et la Tortue en sont un temoignage
__________________________________________________
def main():
     nbLignes =int(input())
     for i in range (nbLignes):
         texte=input()
         for i in range (len(texte)-1,-1,-1):
             print(texte[i],end="")
         print()
main()

