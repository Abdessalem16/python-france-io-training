Lors de l'examen final à la fin de leurs études, la tradition veut que les élèves tirent un sujet au hasard. Tirer un numéro dans un chapeau n'étant pas très amusant, ils utilisent une roue comme celle-ci, qu'ils peuvent faire tourner dans un sens ou dans l'autre.


Les enseignants, par expérience, arrivent toujours à estimer de combien de "zones" la roue va tourner et peuvent aller chercher le sujet et revenir, pendant que la roue tourne encore. Il faut, pour cela, calculer rapidement sur quelle zone le curseur va s'arrêter, en fonction du nombre de zones dont la roue va tourner. A vous de jouer !

Ce que doit faire votre programme :
Votre programme doit commencer par lire un entier nbZones. Sachant que la roue va tourner de nbZones zones, vous devez calculer (puis afficher) sur quelle zone le curseur va arriver.

Ainsi, si la route tourne de +2 zones alors le curseur arrive sur la zone 2, et si la roue tourne de -2 zones, alors le curseur arrive sur la zone 22.

Exemples
Exemple 1
entrée :

25
sortie :

1
Exemple 2
entrée :

-50
sortie :

22
_________________
def main():
    curseur=int(input())
    print(curseur%24)
main()    

