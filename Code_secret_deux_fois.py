 							Code secret deux fois

Pour montrer aux jeunes Algoréens ce dont est capable votre robot, vous souhaitez écrire un programme qui demande deux fois le même mot de passe à son utilisateur.

Ce que doit faire votre programme :
Le mot de passe que vous choisissez est 4242. Écrivez un programme qui attend ce code une première fois, en le demandant de manière répétée par une ligne contenant « Entrez le code : », puis qui une fois ce code entré, affiche « Encore une fois. » et attend le code à nouveau, avant d'afficher « Bravo. » et de se terminer (vous trouverez sans doute cela plus clair avec l'exemple ci-dessous).

L'objectif de cet exercice est d'utiliser une fonction pour éviter de recopier deux fois les instructions qui permettent d'attendre le code 4242.

Exemple
entrée :

4241
4342
4242
2424
4242
sortie :

Entrez le code :
Entrez le code :
Entrez le code :
Encore une fois.
Entrez le code :
Entrez le code :
Bravo.
______________________________
def Secret():
    code11 = int(input("Entrez le code : "))
    print()

    while code11 != 4242:
        code11 = int(input("Entrez le code : "))
        print()


def main():
    Secret()
    print("Encore une fois.")
    Secret()
    print("Bravo.")

main()

