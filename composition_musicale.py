Ecouter de la musique peut être très agréable mais lorsqu'un morceau est vraiment très répétitif, il arrive parfois qu'on s'ennuie un peu. Aussi le professeur de composition musicale du conservatoire a décidé d'imposer une règle très stricte : quand il relit les morceaux composés par ses élèves, dès qu'il voit deux notes identiques côte à côte, il les efface toutes les deux ! Il continue ainsi d'effacer tant qu'il existe deux notes égales consécutives.

Ce travail étant long et fastidieux, il se demande s'il n'est pas possible de l'automatiser.

Ce que doit faire votre programme :
Les notes de musiques sont représentées par les lettres 'a', 'b', 'c', 'd', 'e', 'f' et 'g'.

Votre programme doit lire une seule ligne de texte représentant le morceau de musique (composé de moins de 500 notes) et doit afficher la version du morceau "corrigée" où tous les doublons sont supprimés tant qu'il en existe.

Exemple
entrée :

baaabbacddc
sortie :

b
Commentaires
Sur l'exemple donné une suite possible d'élimination des doublons est la suivante :

baaabbacddc
baaabbacc
babbacc
babba
baa
b
_____________________________
def main():
      note =input()
      j=0
      while j < len(note) -1 :
          if note[j] == note[j+1]:
              note = note[:j] + note[j+2:]
              print(note)
              j=0
          else:
              j+=1
      print(note)
  
main()


