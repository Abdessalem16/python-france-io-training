Alors que vous avez enfin trouvé le livre que vous cherchiez, il s’avère qu’il était complétement chiffré. Vous avez réussi à déchiffrer la première page du livre, et celle-ci vous a indiqué un système de chiffrement utilisé dans le reste du livre. Sauf que cela ne marchait pas pour la dernière page du texte, celle qui vous intéresse le plus, car elle indique l’emplacement de la plante secrète !

Le système de chiffrement utilisé est le même que celui des pages précédentes : La clé de chiffrement est ici un simple nombre, qu’on appelle D, pour « décalage ». Alors, on remplace chaque lettre de l’alphabet par la lettre située D places plus loin dans l’alphabet, considéré de manière circulaire.

Ainsi, si le décalage est de 2, alors

A devient C
B devient D
...
X devient Z
Y devient A
Z devient B
Seulement, vous ne connaissez pas la clé, aucun indice de vous permet de la trouver !

La seule chose que vous savez, c’est qu’il s’agit d’un texte normal (c’est-à-dire non piégé), et qu’il est écrit en français. À vous d’utiliser les connaissances que vous avez sur ce langage afin de trouver la bonne clé !

Limites de temps et de mémoire (Python)
Temps : 0,3 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Contraintes
La ligne de texte contient au plus 10 000 caractères.

Entrée
Une ligne de texte à décrypter.

Le texte peut contenir des lettres, chiffres ou caractères de ponctuation, mais pas d’accents.

Sortie
Vous devez afficher le texte décrypté.

Chaque lettre codée doit être remplacée par la lettre décodée. Les autres caractères (ponctuation, '_', espaces, chiffres), sont laissés tels quels.

Vous devez respecter la casse : si une lettre était en majuscule (ou minuscule), elle doit le rester !

Exemple
entrée :

Np epiep fetwtdp fy opnlwlrp op zykp nlclnepcpd.
sortie :

Ce texte utilise un decalage de onze caracteres.
__________________
def main():
    texte =input()
    mots = [
        "le", "la", "les", "de", "des", "du",
        "un", "une", "et", "est", "en", "dans",
        "que", "qui", "pour", "pas", "sur",
        "avec", "ce", "se", "je", "il", "elle",
        "nous", "vous", "ils", "elles",
        "mais", "ou", "au", "aux", "son", "sa",
        "ses", "mon", "ma", "mes", "bien", "tout",
        "plus", "ne", "me", "te", "on", "comme"
    ]
    mtexte =""
    mscore =-1
    for D in range(26):
        res=""
        for c in texte:
            if c.isalpha():
                pos=ord(c.lower())-ord('a')
                new_pos=(pos - D) %26
                lettre=chr(new_pos + ord('a'))
                if c.isupper():
                    lettre=lettre.upper()
                res+= lettre
            else:
                res+= c
        score=0
        mot=res.lower().split()
        for mt in mot:
            if mt in mots:
                score += 1
        if score > mscore:
            mscore = score
            mtexte = res
    print(mtexte)
main()
