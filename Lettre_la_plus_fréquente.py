		Lettre la plus fréquente

On a découvert de vieilles archives au sein de la bibliothèque, de très nombreux manuscrits écrits dans diverses langues. On souhaite étudier plus en détails ces manuscrits mais comme tous les bibliothécaires ne parlent pas toutes ces langues, il faut d’abord déterminer la langue puis choisir le bon bibliothécaire.

Pour déterminer la langue de manière automatique, un des bibliothécaires propose de déterminer la lettre la plus fréquente dans chaque texte. Son hypothèse est que cette lettre sera différente selon les langues.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
La ligne de texte contient moins de 10 000 caractères.

Entrée
Une seule ligne de texte, composée uniquement de lettres minuscules ou majuscules non accentuées, et d'espaces.

On vous garantit que dans tous les tests, une seule lettre est la plus utilisée, il n'y a pas d'ex-aequo.

Sortie
Vous devez afficher une ligne sur la sortie, contenant la lettre de l'alphabet la plus présente dans le texte fourni en entrée.

Pour chaque lettre, vous devez compter à la fois ses apparitions en majuscule et en minuscule, mais afficher le résultat en majuscules. Vous devez ignorer les espaces.

Exemples
Exemple 1
entrée :

Le francais est une langue romane de la famille des langues indo europeennes
sortie :

E
Exemple 2
entrée :

A lingua portuguesa tambem designada portugues e uma lingua romanica flexiva originada no galego portugues falado no Reino da Galiza e no Norte de Portugal
sortie :

A
________________________________
def main():
    text= input().upper()
    tab=[0]*26
    for i in range (len(text)):
        if text[i] != ' ':
            indice=ord(text[i])-ord('A')
            tab[indice] += 1
        
        maaxx =-1000
        indice_max = 0
        
        for elem in range(len(tab)):
            if tab[elem]>maaxx:
                maaxx =tab[elem]
                indice_max = elem
        lettre =chr(indice_max + ord('A'))
    print(lettre)
        
main()


