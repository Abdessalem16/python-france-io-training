				Conférence et tics de langage


Aujourd’hui, comme tous les mois, un célèbre écrivain donne une conférence sur son œuvre. Guère captivé par ce qu’il explique, vous remarquez rapidement qu’il a un certain nombre de tics de langage, en particulier il utilise souvent les mêmes mots, comme “heu”, “je”...

Pour vous occuper, vous décidez de compter combien de fois certains mots sont utilisés dans son discours.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
Le texte du discours contient au plus 10 000 caractères.

Chacun des mots est au plus de longueur 50.

Entrée
Sur la première ligne, un mot. Sur la seconde ligne, le texte du discours.

Il n’y a pas de ponctuation, les mots et le texte sont uniquement constitués de lettres non accentuées et d’espaces. Par « mot », on entend, comme d’habitude, une suite de caractères ne contenant pas d’espace.

Sortie
Vous devez indiquer combien de fois le mot donné est présent dans le texte du discours.

Quelle que soit la casse du mot qu’on vous donne ou de ses apparitions dans le texte, vous devez toutes les compter !

Exemple
entrée :

heu
Je pense heu que heu ce livre est heu le meilleur que j ai ecrit heu depuis heu cinq ans Heu vous avez des questions
sortie :

6
-----------------------------------------------
def main():
    mot1 = input().lower()
    mot2=input().lower().split()
    compte=0
    for i in range (len(mot2)):
        if mot1== mot2[i]:
            compte+=1
    print(compte)        
main()