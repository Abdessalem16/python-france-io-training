Des enfants découvrent les joies de l'origami (créer des objets en pliant une feuille de papier), et l'un d'eux s'amuse à replier sur elle-même une feuille le plus de fois possible. Il pense qu'il peut replier la feuille en deux 15 fois de suite !

Vous pressentez que cela risque fort d'être impossible. Pendant qu'il essaie, vous décidez de calculer l'épaisseur qu'aurait son pliage final si par hasard l'enfant arrivait à atteindre son objectif.

Ce que doit faire votre programme :
L'épaisseur d'une feuille de papier est de 110 micromètres c'est à dire 0,110 millimètres. Si on la plie 15 fois sur elle-même et que l'épaisseur double à chaque fois, quelle sera l'épaisseur finale si on l'exprime en centimètres ? Votre programme devra calculer et afficher cette valeur (qui n'est pas forcément entière).
_______________________________________
def main():
    epaisseur=0.0110
    for i in range (15):
        epaisseur*=2
    print(epaisseur)    
main()    