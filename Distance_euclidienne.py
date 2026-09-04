Sur les feuilles à motifs que vous leur avez imprimées tout à l'heure, les jeunes gens souhaiteraient calculer la distance entre deux motifs, ce qui ce fait facilement si l'on perçoit la feuille comme un repère orthonormé.

Ce que doit faire votre programme :
Écrivez une fonction qui prend en paramètre les coordonnées (x1,y1)
 et (x2,y2)
 de deux points et retourne la distance euclidienne entre ces deux points. On rappelle que la distance euclidienne entre deux points est égale à :

(x2−x1)2+(y2−y1)2−−−−−−−−−−−−−−−−−−√
Utilisez ensuite cette fonction dans un programme qui lit quatre nombres décimaux x1
, y1
, x2
 et y2
 tapés au clavier, puis affiche la distance entre les deux points correspondants.

On pourra utiliser la fonction mathématique sqrt(x) qui retourne la racine carrée du paramètre x et qui s'importe avec cette ligne :

from math import *
Exemple
entrée :

22.5
46.8
4.25
7.22
sortie :

43.584847

______________________
from math import *

def distance (x1,y1,x2,y2):
    res=sqrt((x2-x1)**2 + (y2-y1)**2)
    return res
    
def main():
    x1=float(input())
    y1=float(input())
    x2=float(input())
    y2=float(input())
    euc=distance(x1,y1,x2,y2)
    print(euc)
main()
