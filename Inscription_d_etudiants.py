		Inscription d’étudiants
Comme chaque année, lors de la rentrée universitaire, de nombreux étudiants viennent s’inscrire à la bibliothèque et une longue file d’attente se forme. Afin d’essayer d'accélérer les choses, les fiches d’inscription de tous les étudiants ont déjà été préparées et ils n’ont plus qu’à les récupérer.

Trois personnes sont en charge de distribuer les fiches : la première s’occupe des étudiants dont le nom commence par une lettre comprise entre A et F (inclus), la seconde personne des étudiants dont le nom commence par une lettre comprise entre G et P (inclus) et la troisième du reste des étudiants.

Quand un nouvel étudiant arrive, il donne son nom et il faut lui indiquer quelle personne il doit aller voir.

Contraintes
Les noms des étudiants font moins de 50 caractères de long et commencent par une lettre majuscule.

Entrée
Un nom d’étudiant.

Sortie
Un entier, 1, 2 ou 3, selon que l’étudiant doit aller voir la première, la seconde ou la troisième personne.

Exemples
Exemple 1
entrée :

Donald
sortie :

1
Exemple 2
entrée :

Picsou
sortie :

2
__________________________
def main():
    nom_Etudiant=input()
    if 'A'<=nom_Etudiant[0]<='F':
        print(1)
    elif 'G'<=nom_Etudiant[0]<='P':
        print(2)
    else:
        print(3)
main()

