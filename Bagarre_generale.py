#                                                                        Bagarre générale

# À peine arrivé dans le village, voilà qu'une bagarre générale est sur le point d'éclater ! Tout en vous mettant à l'abri, vous tâchez de savoir ce qui se passe. On vous explique que le village est principalement composé de deux grandes familles rivales qui ne se supportent pas. Tout sujet étant une source de discorde possible, ils avaient décidé que les superficies de leurs champs respectifs ne devaient pas être trop différentes afin de ne pas attiser la jalousie de la famille opposée. Mais voilà que le patriarche des Arignon suspecte qu'un des champs des Evaran est trop grand ! Vous décidez de les aider ; mais la tâche ne sera pas facile, chacun gardant jalousement secrète la superficie réelle de ses champs.
# Code :
Arignon = int(input())
Evaran = int(input())

if Arignon - Evaran>10:
    print("La famille Arignon a un champ trop grand")
elif Evaran - Arignon>10:
    print("La famille Evaran a un champ trop grand")
