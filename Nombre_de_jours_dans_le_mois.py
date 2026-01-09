# Nombre de jours dans le mois
# Les soldats de la garnison de la ville sont payés à la journée et pas au mois, ce qui fait que leur salaire n'est pas le même selon le mois. Le trésorier étant malade et les soldats voulant être payés vous vous proposez pour le remplacer. Certains soldats revenant de mission à l'extérieur, ils doivent recevoir leur paye pour les mois précédents également. Afin de ne pas faire d'erreur, vous décidez d'écrire un programme pour vous aider.
# Ce que doit faire votre programme :
# Écrivez un programme qui lit un numéro de mois algoréen, et affiche le nombre de jours de celui-ci. Les Algoréens disposent de leur propre calendrier. Voici les informations dont vous avez besoin :
 
# Code :
Ma = int(input())
if Ma ==4 or Ma ==5 or Ma ==6 or Ma ==10:
    print("31")
elif Ma == 11:
    print("29")
else:
    print("30")
