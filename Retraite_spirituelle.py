# lecture de l’entrée

# Retraite spirituelle

# Une fois par an, tout habitant de plus de 15 ans doit effectuer une randonnée spirituelle, celle-ci pouvant durer plusieurs jours. La durée dépendra du temps nécessaire à chaque personne pour faire le bilan de l'année écoulée. Au cours de cette randonnée, la personne doit répéter encore et encore la même incantation, une fois par seconde. Vous vous demandez combien de fois au total l'incantation aura été répétée, selon la durée de la randonnée.
# Ce que doit faire votre programme :
# Votre programme devra lire un entier : le nombre de jours que dure la randonnée.
# Ensuite, il devra afficher le nombre de fois que l’indication est répétée,
# Sachant qu’elle est prononcée une fois par seconde pendant 
# 16 heures par jour (les 8 autres heures, en dort !)
# Comments
# En 2 jours(le nombre donné en entrée), l’incantation sera répétée 115200 fois
# Ecrivez à présent un programme qui fonctionne pour n’importe quel nombre de jours
# Code :
randonnejour = int(input())
Incantation = randonnejour*16*60*60 
print(Incantation)
