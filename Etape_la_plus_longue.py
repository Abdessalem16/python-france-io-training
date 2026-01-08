# Etape la plus longue
# Dans votre petit carnet de voyage, vous avez noté la distance
# Que vous avez parcourue chaque jour.
# Aujourd’hui, vous êtes particulièrement en forme 
# Et vous décidez donc de marcher plus que les jours précédents.
# Vous souhaitez utiliser un programme pour déterminer quel est votre
# Record pour l’instant.
# Ce que doit faire votre programme :
# Votre programme doit d’abord lire un entier strictement positif,
# Le nombre de jours de marche effectués jusqu’à présent .
# Il doit ensuite lire, pour chaque jour, la distance parcourue 
# Cr jour-là. Il doit alors afficher la distance maximale parcourue 
# En une journée.
# Code :
nombrejour = int(input())
maximum =-1
for loop in range(nombrejour):
    distance= int(input())
    if distance > maximum:
        maximum=distance
print(maximum)
