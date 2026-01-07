# Tarifs dégressifs
# L'auberge dans laquelle vous avez prévu de passer la nuit ce soir propose des tarifs très intéressants, pour peu que l'on n'arrive pas trop tard. En effet, plus on arrive tôt moins on devra payer. Vous essayez de construire un programme vous donnant directement le prix à payer en fonction de votre heure d'arrivée.
# Ce que doit faire votre programme :
# Votre programme lira un entier,  l’heure d’arrive, qui sera compris entre 0 et 12 inclus.
# 0 correspond à midi, 1 à 1h de l’après-midi, etc. et 12 à minuit.
# Le prix de la chambre est de 10 pièces à midi, et augmente de 5 pièces chaque heure après midi.
# Il est donc de 15 pièces à 13h, etc. il ne peut cependant pas dépasser 53 pièces.
# Votre programme devra afficher le prix à payer correspondant à l’heure d’arrivée donnée. 

# Code :
heureArrive = int(input())
if heureArrive == 0:
    print(10)
elif heureArrive == 1:
    print(15)
elif heureArrive == 2:
    print(20)
elif heureArrive == 3:
    print(25)
elif heureArrive == 4:
    print(30)
elif heureArrive == 5:
    print(35)
elif heureArrive == 6:
    print(40)
elif heureArrive == 7:
    print(45)
elif heureArrive == 8:
    print(50)
elif heureArrive >=9:
    print(53)
autre solution :
heureArrive = int(input())
t= heureArrive *5+10
if t > 53:
    print(53)
else:
    print(t)
