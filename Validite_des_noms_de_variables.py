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
def is_majus(c):
    return ord(c)>=ord('A') and ord(c)<=ord('Z')
def is_minus(c):
    return ord(c)>=ord('a') and ord(c)<=ord('z')
def is_int(c):
    return ord(c)>=ord('0') and ord(c)<=ord('9')
def is_alpha(c):
    return is_majus(c) or is_minus(c)

def main():   
    n=int(input())
    for i in range(n):
        ch=input()
        first_char = ch[0]
        is_valide_name=is_alpha(first_char) or first_char =='_' 
        if not is_valide_name:
            print("NO")
            continue
        else:
            for i in ch:
                if not (is_alpha(i) or is_int(i) or i=='_'):
                    is_valide_name=False
                    break
        if not is_valide_name:
            print('NO')
        else:
            print('YES')
        
main()

