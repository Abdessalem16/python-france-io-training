Zones de couleurs

Un espion a été démasqué dans la ville où vous vous trouvez. Son interrogatoire n'a pas été très fructueux : la seule chose que vous savez, c'est qu'il espionnait les savants de l'université, une puissance étrangère étant intéressée par leurs recherches. Vous vous rendez donc à l'université pour discuter avec les chercheurs mais à peine arrivé, vous êtes recruté comme assistant par le laboratoire d'étude du comportement humain.

Celui-ci réalise une expérience consistant à demander à plusieurs personnes de placer chacune un jeton sur une table contenant des zones de différentes couleurs. Les chercheurs souhaitent ainsi étudier si le choix de la zone où une personne place son jeton est lié à la couleur des vêtements qu'elle porte.

Ce que doit faire votre programme :
Sur une table est placée une feuille de papier rectangulaire de 90 cm de large et 70 cm de haut, composée de zones de différentes couleurs, comme le décrit la figure ci-dessous. Un certain nombre de personnes placent l'une après l'autre un jeton où elles le souhaitent sur la table, à l'exception des frontières entre les différentes zones.
____________
On vous donne en entrée le nombre de jetons qui ont été déposés, puis, pour chaque jeton, ses coordonnées sur la feuille par rapport à l'origine en haut à gauche, sous la forme d'une abscisse et d'une ordonnée entre −1 000 et 1 000.

Votre programme devra qualifier chaque jeton avec l'un des textes suivants, en fonction de la couleur sur laquelle il se trouve :

« En dehors de la feuille »
« Dans une zone jaune »
« Dans une zone bleue »
« Dans une zone rouge »
Essayez d'écrire votre programme de sorte qu'il y ait au maximum une condition par possibilité de texte affiché.
___________________
def main():
    personne=int(input())
    for i in range(personne):
        large=int(input())
        haut=int(input())
        if 10<haut<55 and ((10<large<25  or 50<large<85 )or (25<large<50 and not(20<haut<45))):
            print("Dans une zone bleue")
        elif  60<haut<70 and (15<large<45 or 60<large<85):
            print("Dans une zone rouge")
        elif large <0 or large >90 or haut<0 or haut >70 :
            print("En dehors de la feuille")
        else:
            print("Dans une zone jaune ")
main()

