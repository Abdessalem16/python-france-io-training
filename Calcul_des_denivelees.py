# Calcul des dénivelées

# Aujourd'hui c'est l'étape de montagne et vous allez devoir franchir plusieurs cols. Vous allez passer votre temps à monter, descendre, remonter, redescendre, etc... Vous décidez de noter les différentes variations d'altitudes, afin de pouvoir calculer à la fin de la journée quelle est la dénivelée totale que vous avez montée ainsi que la dénivelée totale que vous avez descendue (les deux valeurs peuvent être différentes car vous ne retournez pas à votre point de départ).
# Ce que doit faire votre programme :
# Votre programme lira d’abord un entier représentant le nombre de montées
# Et descentes que vous avez réalisées. 
# Pour chaque montée ou descente, il faut ensuite lire un entier
# Représentant la variation d’altitude, cet entier étant strictement
# Positif dans le cas d’une montée et strictement négatif dans le cas
# D’une descente (il n’y a rien à compter pour les tronçons qui
# Sont bien à plat).
# Votre programme devra afficher l’altitude totale montée
# Puis l’altitude totale descendue (ces deux nombres sont positifs).
# Code :
mouvement = int (input())
monter=0
descendre =0
for loop in range(mouvement):
    action=int(input())
    if action>0:
        monter+=action
    else:
        descendre -=action
print(monter)
print(descendre)
