# Concours de tir à la corde
# Vous avez passé la nuit dans une auberge. Au petit matin, un championnat de tir à la corde y est organisé. Vous ne souhaitez pas participer, mais l'aubergiste insiste pour que vous soyez impliqué dans l'événement. Vous décidez alors de vous engager dans les paris qui se font sur les deux équipes qui concourent.
# Le championnat oppose deux équipes, contenant chacune autant de joueurs. Pour donner de l'allure et pimenter les paris, au début du championnat, tous les joueurs sont présentés, avec leur poids, avant d'aller tenir leur côté de la corde. Il est d'abord présenté un membre de la première équipe, puis de la deuxième, puis de la première, puis de la deuxième etc. jusqu'à ce que tous les joueurs soient passés. Afin de vous faire un premier pronostic, vous calculez le poids total de chaque équipe, avec votre robot
# Ce que doit faire votre programme :
# Votre programme devra lire un premier entier : le nombre de membres nbMembre qui constituent une équipe. Ensuite, il devra lire les poids (en kilogrammes), au total nbMembres * 2 , sachant que le premier poids est celui d’un joueur de la 1re équipe, le deuxième poids celui d’un joueur de la 2e équipe, le troisième la 1re équipe, le quatrième la 2e équipe, etc.
# Après avoir calculé le poids total de chaque équipe, vous devrez afficher le texte « l’équipe X a un avantage » (en remplaçant X par la valeur 1 ou 2), en considérant qu’une équipe est avantagée si elle a un poids s total supérieur à celui de l’autre.
# Vous afficherez ensuite le texte «  Poids total pour l’équipe 1 : » suivi  du poids de l’équipe 1, puis « Poids total pour l’équipe  2 : » suivi du poids de l’équipe 2 (voir l’exemple ci-dessous).
# On vous garantit que les deux équipes n’auront pas le même poids total.

# Code :
nbMembres = int(input())
equipe1 =0
equipe2 =0
EQU1=1
EQU2=2
for loop in range(nbMembres):
    Poid1=int(input())
    Poid2=int(input())
    if EQU1 ==1 :
        equipe1 +=Poid1
    if EQU2==2 :
        equipe2 +=Poid2
if equipe1 > equipe2:
    print("L'équipe ",EQU1 ,"a un avantage")
else:
    print("L'équipe ",EQU2 ,"a un avantage")
print("Poids total pour l'équipe ",EQU1 ,':',equipe1)
print("Poids total pour l'équipe ",EQU2 ,':',equipe2)
