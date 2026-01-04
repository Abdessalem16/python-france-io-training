# le secret du Goma
# vous avez remparqueé un rituel assez étrange : tous les trois jours, les villageois
# passent la soirée à parsemer d’une sorte de gros grain de mais le long de l’alleé 
# centrale du village. Le lendemain, le grain a disparu, mais l’allée est pleine de ce qui 
# ressemble à petites mottes de terre noire que les villageois ramassent ?
# l’un des villageois vous explique que le grain est une offrande aux Borloks, de gros
# animaux qui leur laissent ces mottes en échange : ce que vous preniez pour des mottes
# de terre sont en fait des bouses de Borloks !
# vous etes prise de nausées en apprenant qu’ils les utilisent pour fabriquer le Goma, 
# cette sorte de pain noir qu’ils vous ont servi à chaque repas depuis votre arrivée…
# tout en cachant votre dégout de peur de vexer les villageois, vous décidez l’enqueter sur la composition exacte du Goma. Vous vous proposez donc pour aider à ramasser les bouses de Borloks qui jonchent l’allée.
# Ce que doit faire votre programme :
# L’allée centrale du village peut être représentée comme une série de 17 cases, dont 
# La plupart contiennent une bouse de borlok :

# Le robot se trouve initialement dans case de gauche. Il doit se déplacer case par case en allant
# Vers la droite, et ramasser sur chaque case la bouse qui s’y trouve. Enfin , votre robot
# Doit déposer tout ce qu’il a ramassé dans la boite
# Située sur la 17 e case, tout à droite.
# Votre programme ne doit pas faire okus d’une dizaine de lignes.
from robot import *
for loop in range(15):
	droit()
	ramasser()
droit()
deposer()



