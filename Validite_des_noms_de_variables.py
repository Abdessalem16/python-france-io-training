                Validité des noms de variables


La jeune Ada, fascinée par votre robot, a écrit plusieurs programmes, mais elle a souvent des difficultés avec les noms de variables : elle a du mal à savoir si un nom de variable est correct ou pas.

Ada utilise, elle, le langage C++ pour programmer et la règle pour les noms de variables dans ce langage est la suivante : le nom de variable doit commencer par une lettre non accentuée ou un caractère '_', et chacune des lettres suivantes est soit une lettre non accentuée, soit un '_', soit un chiffre.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 1 000 ko.
Contraintes
La longueur de chaque nom proposé ne dépassera pas 100 caractères.

Entrée
La première ligne contient l’entier nbNoms. Les nbNoms lignes suivantes contiennent chacune un nom de variable possible.

Aucun des noms de variable possibles ne sera un mot-clef du langage. Vous n’avez donc pas à vous en occuper.

Sortie
Vous devez afficher nbNoms lignes sur la sortie, indiquant dans l'ordre où ils sont donnés en entrée, si les noms proposés sont valides.

Affichez le texte "YES" pour un identifiant valide et "NO" pour un identifiant invalide.

Exemple
entrée :

5
Bonjour32
r~ussi
_toto_
passe-partout
2_fois
sortie :

YES
NO
YES
NO
NO
_____________________
def main():
    nbNoms=int(input())
    for j in range (nbNoms):
        nom=input()
        test=True
        if not ('a'<=nom[0]<='z' or 'A'<=nom[0]<='Z' or nom[0]=='_'):
            test=False
        for i in range (1,len(nom)):
            if not ('a'<=nom[i]<='z' or 'A'<=nom[i]<='Z' or nom[i]=='_' or '0'<=nom[i]<='9') :
                test=False
        if test:
            print("YES")
        else:
            print("NO")

main()


