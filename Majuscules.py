             Majuscules

Ecrivez un programme qui lit une ligne de texte au clavier et qui affiche le contenu de cette ligne en transformant en majuscules tous les caractères minuscules qu'elle contient, et en réaffichant les autres caractères tels-quels.

Limites de temps et de mémoire (Python)
Temps : 0,2 s sur une machine à 1 GHz.
Mémoire : 1 000 ko.
Contraintes
La ligne ne contient pas plus de 10 000 caractères.

Elle ne contient aucun caractère accentué.

Exemple
entrée :

Ceci est un texte sans accents, qui sert d'exemple.
sortie :

CECI EST UN TEXTE SANS ACCENTS, QUI SERT D'EXEMPLE.
___________________________________
def is_majus(pp):
    return ord(pp)>=ord('A') and ord(pp)<=ord('Z')
def is_minin(mm):
    return ord(mm)>=ord('a') and ord(mm)<=ord('z')
def is_int(c):
    return ord(c)>=ord('0') and ord(c)<=ord('9')
def Uppper(pp):
    a=""
    for i in pp:
        if is_minin(i):
            a+=chr(ord(i)-(ord('a')-ord('A')))
        else:
            a+=i
    return a
def lowwer(pp):
    a=""
    for i in pp:
        if is_majus(i):
            a+=chr(ord(i)+(ord('a')-ord('A')))
        else:
            a+=i
    return a
def main():
    pp=input()
    print(Uppper(pp))
    
    
main()
