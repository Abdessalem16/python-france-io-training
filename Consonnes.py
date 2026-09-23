				Consonnes
Ecrivez un programme qui affiche dans l'ordre alphabétique toutes les consonnes de l'alphabet en minuscules, en les séparant par des espaces.

On utilisera bien entendu une boucle !

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 32 000 ko.
___________________
def main():
    for i in range(ord('a'),ord('z')+1):
        if not(chr(i) in ['a','e','i','o','u','y']):
            print(chr(i),end=" ")
main()