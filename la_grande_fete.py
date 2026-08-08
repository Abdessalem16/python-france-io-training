Un espion était présent à la grande fête organisée la semaine dernière par le gouverneur. Bien qu'on n'ait pas pu l'identifier, on a réussi à intercepter son rapport et à estimer en fonction de ce qu'il a pu voir, à quelle période il a été présent. Sachant pour chaque invité sa date d'arrivée et de départ, on aimerait interroger tous les suspects potentiels. Vous souhaitez savoir combien de suspects il faudra interroger.

Ce que doit faire votre programme :
On vous donne une période de temps à étudier, et les dates d'arrivée et de départ d'un certain nombre d'invités d'une fête. Écrivez un programme qui détermine combien d'invités ont été présents à un moment de la période étudiée.

Votre programme doit d'abord lire deux entiers : la date de début et la date de fin de la période étudiée. L'entier suivant, nbInvites, est le nombre total d'invités. Pour chaque invité, votre programme doit ensuite lire deux entiers : sa date d'arrivée et de départ. Un invité est suspect si la période à laquelle il a été présent intersecte la période étudiée. Votre programme doit afficher le nombre d'invités suspects.
____________________________

def main():
    datedebut=int(input())
    datefin=int(input())
    nbInvites=int(input())
    invitAumomtemps=0
    for i in range (nbInvites):
        dd=int(input())
        df=int(input())
        if not(dd>datefin or df<datedebut):
            invitAumomtemps+=1
    print(invitAumomtemps)
main()    