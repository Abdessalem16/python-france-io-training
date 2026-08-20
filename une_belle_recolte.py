			Une belle récolte
Vous êtes chargé d'acheter des fruits pour un grand repas organisé pour fêter la dernière récolte qui a été très fructueuse. Les vendeurs proposent généralement leurs fruits par paquets. Vous souhaitez acheter un paquet dont le nombre de fruits soit un multiple du nombre de personnes conviées, de sorte que chaque invité ait le même nombre de fruits.

Ce que doit faire votre programme :
Votre programme doit commencer par lire un entier nbPersonnes puis un entier nbFruits. Il doit ensuite afficher "oui" si nbFruits est un multiple de nbPersonnes, et "non" dans le cas contraire.

Exemple
entrée :

12
156
sortie :

oui
_________________________

def main():
    nbPersonnes=int(input())
    nbFruit=int(input())
    if nbFruit%nbPersonnes==0:
        print("oui")
    else:
        print("non")
main()    
