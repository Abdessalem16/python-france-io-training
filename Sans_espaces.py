				Sans espaces
Ecrivez un programme qui lit une ligne tapée au clavier et l'affiche en remplaçant tous les espaces par le caractère "_".

Contraintes
La ligne de texte contient au plus 100 caractères.

Exemple
entrée :

Voici un exemple de texte avec des espaces.
sortie :

Voici_un_exemple_de_texte_avec_des_espaces.
______________________________________
def main():
    texte = input()
    change=list(texte)
    for i in range(len(change)):
        if change[i] ==' ':
            change[i]='_'
    
    texte="".join(change)
    print(texte)
main()

