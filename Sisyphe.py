# Sisyphe


# ce que doit faire votre programme :
# Programmez votre robot pour qu’il mène le rocher tout en haut des 
# Programmez votre robot pour qu’il mène le rocher tout en haut des 21 marches de la pyramide et redescende ensuite tout en bas. 
# Par exemple, si la pyramide  ne faisait que deux marches de haut,  votre robot
#  Devrait effectuer le trajet illustré ci-dessous : haut droite, haut, droite, gauche, bas, gauche,bas
from robot import * 
for haute in range(21) :
	haut()
	droite()
for base in range(21) :
	gauche()
    bas()
