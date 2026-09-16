			Titres palindromiques


En étudiant un vieux parchemin, on apprend que le livre qui nous intéresse dans la bibliothèque a un titre qui est un palindrome : il peut se lire de gauche à droite ou de droite à gauche (sans s’occuper des espaces).

Vous devez analyser les titres de tous les livres de la bibliothèque et sélectionner ceux qui sont des palindromes.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
Chaque titre de livre est au plus de longueur 100.

Entrée
La première ligne contient un entier nbLivres, le nombre total de livres.

Chacun des nbLivres lignes suivantes contient un titre de livre.

Les titres sont composés d’espaces et de lettres majuscules ou minuscules, non accentuées.

Sortie
Vous devez afficher chaque titre de livre qui est un palindrome.

Pour déterminer si un titre est un palindrome, on ne considérera ni les espaces, ni la casse (majuscule ou minuscule) des lettres.

Exemple
entrée :

3
Lieur a Rueil
Le chevalier delibere
Un roc si biscornu
sortie :

Lieur a Rueil
Un roc si biscornu
______________________________________________
def main():   
    nombre=int(input())
    tab=[]
    for loop in range(nombre):
        nom=input()
        test = nom.replace(" ", "").lower()
        taille=len(test)
        res=True
        for i in range(taille//2):
            if test[i]!=test[taille-1-i]:
                res=False
                break
        if res:
            tab.append(nom)
    for j in tab:
        print(j)
        
main()
