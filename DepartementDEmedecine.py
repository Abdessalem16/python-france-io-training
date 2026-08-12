Département de médecine : contrôle d'une épidémie
Afin de pouvoir mieux combattre les différentes épidémies, parfois très graves, qui se développent régulièrement dans la région, le département de médecine de l'université a lancé une grande étude. En particulier, les chercheurs s'intéressent à la vitesse de propagation d'une épidémie et donc à la vitesse à laquelle des mesures sanitaires doivent êtres mises en place.

Ce que doit faire votre programme :
Votre programme doit d'abord lire un entier, la population totale de la ville. Sachant qu'une personne était malade au jour 1 et que chaque malade contamine deux nouvelles personnes le jour suivant (et chacun des jours qui suivent), vous devez calculer à partir de quel jour toute la population de la ville sera malade.
_______________
def main():
    personne=int(input())
    maladie=1
    jour=1
    while maladie<personne:
        jour+=1
        maladie+=maladie*2
    print(jour)    
main()    
