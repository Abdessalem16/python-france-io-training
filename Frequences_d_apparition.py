			Fréquences d’apparition

On a découvert de vieilles archives au sein de la bibliothèque, de nombreux manuscrits écrits dans diverses langues. On souhaite étudier plus en détail ces manuscrits mais comme tous les bibliothécaires ne parlent pas toutes ces langues, il faut d’abord déterminer la langue pour pouvoir choisir le bon bibliothécaire.

Pour déterminer la langue de manière automatique, un des bibliothécaires vous propose de déterminer la lettre la plus fréquente dans chaque texte, mais vous savez que cette technique n’est pas assez précise pour donner de bon résultats.

Vous décidez donc plutôt de regarder à quelles fréquences apparaissent chacune des lettres de l’alphabet.

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
La ligne de texte contient moins de 10 000 caractères.

Entrée
Une seule ligne de texte, ne contenant pas de lettres accentuées, mais pouvant contenir des signes de ponctuation ou des chiffres.

Sortie
Pour chacune des lettres de l’alphabet, il faut afficher, sur une ligne, sa fréquence d’apparition dans le texte définie comme le nombre de fois où la lettre est présente, divisé par le nombre total de lettres du texte (et pas le nombre total de caractères).

Exemple
entrée :

Le francais est une langue romane, de la famille des langues indo-europeennes.
sortie :

0.109375
0.000000
0.015625
0.046875
0.203125
0.031250
0.031250
0.000000
0.046875
0.000000
0.000000
0.093750
0.031250
0.125000
0.046875
0.015625
0.000000
0.046875
0.078125
0.015625
0.062500
0.000000
0.000000
0.000000
0.000000
0.000000
_____________________________________________
def main():
    text = input().upper()
    tab = [0] * 26
    total = 0
    
    for i in range(len(text)):
        if 'A'<=text[i]<='Z':
            indice = ord(text[i])-ord('A')
            tab[indice] +=1
            total +=1
    for i in range(26):
        frequence = tab[i] /total
        print(f"{frequence :.6f}")

main()

