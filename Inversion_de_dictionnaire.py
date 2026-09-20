La bibliothèque contient de nombreux dictionnaires, mais pour certains couples de langues, elle ne dispose que du dictionnaire permettant d’aller de la première langue vers la seconde, et pas du dictionnaire permettant de faire l’inverse.

Étant donné un dictionnaire bilingue, vous devez l’inverser pour construire le dictionnaire inverse.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
Chaque mot contient au plus 50 caractères.

Entrée
La première ligne contient l’entier nbMots.

Les nbMots lignes suivantes contiennent chacune deux mots séparés par un espace : un mot dans la première langue et un mot dans la seconde.

Les mots ne contiennent pas d’espaces et sont constitués uniquement de lettres minuscules.

Les couples de mots sont triés selon l’ordre alphabétique des mots de la première langue.

Sortie
Vous devez afficher l’ensemble des couples de mots inversés (d’abord le mot de la seconde langue, puis le mot de la première) triés selon l’ordre alphabétique des mots de la seconde langue.

Exemple
entrée :

2
travail work
verite truth
sortie :

truth verite
work travail
________________________________________________
def main():
    nbMots=int(input())
    mot=[]
    for i in range (nbMots):
        mot1,mot2=input().split()
        mot.append([mot2,mot1])
    for i in range(len(mot)):
        minn =i
        for t in range(i,len(mot)):
            if mot[t]<mot[minn]:
                minn=t
        aux=mot[minn]
        mot[minn]=mot[i]
        mot[i]=aux
    for elem in mot:
        print(elem[0],elem[1])
        
        
main()

