Écrivez un programme qui affiche tous les caractères de l'alphabet en majuscules, avec une espace entre chaque caractère.

On utilisera bien entendu une boucle !

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 1 000 ko.
Exemple
entrée :

sortie :

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
___________________________________________________
def main():
    for i in range(ord('A'),ord('Z')+1):
        print(chr(i),end=" ")
main()