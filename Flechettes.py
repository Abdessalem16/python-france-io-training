Au cours de votre périple, vous rencontrez un groupe d'amateurs de fléchettes. Ces joueurs sont de grands passionnés et aiment jouer sur des cibles de tailles variées. Cependant, leurs cibles se font vieilles et mériteraient bien d'être changées ! Vous profitez donc de votre passage parmi eux pour leur imprimer de nouvelles cibles.

Les cibles à imprimer sont de la forme suivante (ici avec 4 lettres) :


aaaaaaa
abbbbba
abcccba
abcdcba
abcccba
abbbbba
aaaaaaa
Ce que doit faire votre programme :
Votre programme doit lire un unique entier : le nombre de lettres nbLettres (1 <= nbLettres <= 26) à utiliser. Il doit ensuite afficher la cible correspondante (comme indiqué sur la figure ci-dessus).

Limites de temps et de mémoire (Python)
Temps : 1 s sur une machine à 1 GHz.
Mémoire : 8 000 ko.
Exemple
entrée :

5
sortie :

aaaaaaaaa
abbbbbbba
abcccccba
abcdddcba
abcdedcba
abcdddcba
abcccccba
abbbbbbba
aaaaaaaaa
___________________________________
def main():
      lettrenb=int(input())
      lettres=["a","b","c","d","e","f","g","h","i","j"
               ,"k","l","m","n","o","p","q","r","s","t"
               ,"u","v","w","x","y","z"]
      taille = 2 * lettrenb-1
      for i in range(taille):
          for j in range(taille):
              distance = min (i,j, taille-1-i,taille-1-j)
              print(lettres[distance],end="")
          print()
  
main()

