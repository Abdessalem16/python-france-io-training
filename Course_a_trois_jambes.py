Course à trois jambes

En parallèle du grand marché de la ville auquel vous accompagnez vos amis marchands, un ensemble de jeux sont organisés pour les habitants, en particulier la fameuse « course à trois jambes » : cette course se déroule par équipes de deux personnes dont deux des jambes sont attachées par une corde :


Afin de constituer les équipes au hasard, un tirage au sort est organisé. Comme c'est une opération longue à faire manuellement et que vous êtes impatient, vous décidez d'aider les organisateurs avec votre robot.

Ce que doit faire votre programme :
Le premier entier à lire est le nombre de participants (au plus 3 000) qui sera toujours pair. Ensuite il faut lire, pour chaque participant, un entier qu'il a choisi librement.

Les équipes sont constituées ainsi : la personne ayant choisi le plus petit entier est avec celle ayant choisi le plus grand, celle ayant choisi le deuxième plus petit est avec celle ayant choisi le deuxième plus grand, et ainsi de suite.

Vous devrez afficher la composition de chacune des équipes, dans l'ordre : d'abord celle dont le plus petit numéro fait partie, puis celle dont le second plus petit numéro fait partie, et ainsi de suite. Au sein de chaque équipe on affichera d'abord le plus petit numéro puis le plus grand.

On vous garantit que tous les numéros sont différents.

Exemple
entrée :

10
80
1000
5
154
130
847
450
42
35
789
sortie :

5 1000
35 847
42 789
80 450
130 154

________________
def main():
    participants=int(input())
    tab=[0]*participants
    for i in range(participants):
        tab[i]=int(input())
    tab.sort()
    for i in range((participants+1)//2):
        croi=tab[i]
        descroi=tab[participants-1-i]
        print("{} {}".format(croi,descroi))
main()
