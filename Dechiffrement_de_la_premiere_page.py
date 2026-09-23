Vous avez enfin trouvé le livre que vous cherchiez depuis des jours, mais il vous est impossible de lire : toutes les pages semblent cryptées ! Une analyse plus poussée vous révèle que la première page est encodée avec un système de cryptage très classique, et toujours utilisé actuellement.

Dans ce système de cryptage, on remplace chaque lettre du message par une autre, à l'aide d'une grille de cryptage. Pour décrypter le message, il suffit de faire pareil mais avec la grille inverse (la grille de décryptage) et on retrouvera le texte original.

Vous avez plusieurs idées pour cette fameuse clé de décryptage mais comme il serait trop long de tester à la main, vous décidez d’écrire un programme pour décoder automatiquement un texte, étant donnée la clé.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
Le texte crypté contient au plus 1000 caractères.

Entrée
La première ligne de l'entrée contient la grille de décryptage, composée de 26 caractères minuscules. La première lettre correspond à la lettre par laquelle il faut remplacer tous les 'a' du texte crypté, la deuxième tous les 'b', etc.

La deuxième ligne de l'entrée contient le texte crypté.

Il n’y a pas d’accents, mais il peut y avoir des espaces, de la ponctuation, etc.

Sortie
Vous devez afficher une ligne sur la sortie : le texte décrypté.

Chaque lettre cryptée doit être remplacée par la lettre décryptée. Les autres caractères (ponctuation, '_', espaces, chiffres), sont laissés tels quels.

Vous devez respecter la casse : si une lettre était en majuscule (ou minuscule), elle doit le rester !

Exemple
entrée :

qwertyuiopasdfghjklzxcvbnm
Xiyqigd !
sortie :

Bonjour !
_____________________________
def main():
    list2=input()
    mot=input()
    tab=""
    for i in mot:
        if i.isalpha():
            pos=ord(i.lower())-ord('a')
            lettre = list2[pos]
            
            if i.isupper():
                lettre = lettre.upper()
            tab+=lettre
        else:
            tab+=i
    print(tab)            
    
main()

