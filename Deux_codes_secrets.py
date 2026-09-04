					Deux codes secrets

Cette fois-ci, vous souhaitez montrer aux jeunes recrues un programme qui demande deux codes secrets différents.

Ce que doit faire votre programme :
Vous choisissez 2121 comme deuxième mot de passe. Écrivez un programme qui attend successivement les codes 4242 puis 2121, en affichant cette fois « Premier code bon. » entre les deux, comme montré dans l'exemple.

Ici, écrivez une et une seule fonction pour demander successivement les deux codes.

Exemple
entrée :

12
42345
4242
123
2121
sortie :

Entrez le code :
Entrez le code :
Entrez le code :
Premier code bon.
Entrez le code :
Entrez le code :
Bravo.
_______________________________________________________________


def modd_epasse():
    choix = int(input("Entrez le code :"))
    print()
    while choix != 4242:
        choix = int(input("Entrez le code :"))
        print()
    print("Premier code bon.")
    while choix != 2121:
        choix = int(input("Entrez le code :"))
        print()
    print("Bravo.")
def main():
    modd_epasse()
main()
