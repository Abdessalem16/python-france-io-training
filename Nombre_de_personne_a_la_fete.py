Le gouverneur a organisé une petite fête à laquelle tous les notables étaient invités. Il souhaiterait à présent faire réaliser une petite affiche vantant le succès de la fête et indiquant en particulier le nombre de personnes présentes au moment le plus intense de la fête.

Ce que doit faire votre programme :
On vous décrit les arrivées et départs des participants d'une fête, et votre programme doit afficher le nombre maximum de personnes qui ont été présentes au même moment. Chacun des invités est identifié par un numéro.

Le premier entier à lire est nbPersonnes : le nombre total de personnes qui se sont rendues à la fête. Ensuite, il y a 2 × nbPersonnes entiers à lire, dans l'ordre chronologique des arrivées et départs. Si l'entier est positif, c'est que la personne de numéro correspondant vient d'arriver, s'il est négatif, elle vient de partir. Une fois qu'une personne est partie, elle ne revient pas.

Votre programme doit déterminer puis afficher le nombre maximum de personnes qui étaient là simultanément.
___________________
def main():
    nbPersonne = int(input())
    personne=0
    maxx=-1
    for i in range(nbPersonne*2):
        participant = int(input())
        if participant >0:
            personne+=1      
        else:
            personne-=1
        if maxx<personne:
            maxx=personne
    print(maxx)               
main()
