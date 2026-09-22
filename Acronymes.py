Comme dans tout lieu de travail, les employés de la bibliothèque ont pris l’habitude d’utiliser des acronymes (exemples d’acronymes : IOI, RATP, BEPC, LOL...) pour les titres de livres les plus utilisés, ce qui leur permet de parler plus vite !

Seulement vous ne connaissez pas encore tous les acronymes, aussi lorsqu’on vous demande d’aller chercher un livre sans vous donner le titre complet, vous êtes bien embêté(e) !

Étant donné un acronyme, vous devez trouver tous les titres qui correspondent et les afficher "joliment".

Limites de temps et de mémoire (Python)
Temps : 0,1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
Tous les titres de livres ainsi que les acronymes contiennent au plus 200 caractères.

Entrée
Sur la première ligne, un acronyme, uniquement constitué de lettres majuscules.

Sur la seconde ligne, un entier nbLivres, le nombre de titres de livres.

Sur les nbLivres lignes suivantes les titres de livres, uniquement constitués de lettres ou d’espaces, sans accents.

Les mots de chaque titre sont toujours séparés par un seul espace.

Sortie
Vous devez afficher chaque titre de livre qui correspond à l’acronyme, en mettant toutes ses lettres en minuscules sauf la première lettre de chaque mot, qui doit être en majuscule.

Exemple
entrée :

PP
7
PEDro paramO
Poemes PALINDROMES
LA Condition HUMAINE
PERE et fils
petite
Promenade Au phare
peter pan
sortie :

Pedro Paramo
Poemes Palindromes
Peter Pan
______________________________________

def main():
    acronyme = input()
    nbLivres = int(input())
    tab = []
    for i in range(nbLivres):
        titre = input()
        mots = titre.split()
        initiales = ""
        for j in range(len(mots)):
            initiales += mots[j][0].upper()
        if initiales == acronyme:
            tab.append(titre.title())
    for titre in tab:
        print(titre)

main()
