Comme dans tout métier, certains soldats sont devenus amis, et on peut facilement dire si deux soldats sont amis : si à un moment ils sont de garde en même temps alors ils sont amis, sinon ils ne le sont pas. Afin de développer les relations amicales entre les soldats, le colonel en charge des tours de garde souhaiterait autant que possible mettre en binôme des soldats qui ne sont pas encore amis. Il vous demande votre aide pour déterminer si deux soldats sont amis ou pas.

Ce que doit faire votre programme :
Vous devez écrire un programme qui détermine si deux soldats ont été de garde en même temps.

Votre programme doit lire quatre entiers : la date du début et la date de fin (incluse) du service du premier soldat puis celles du second soldat.

Si les deux soldats ont, à un moment (même une seule seconde), été de garde en même temps le programme devra écrire "Amis" et sinon "Pas amis".


--------------------------------
def main():
    date_debut1 = int(input())
    date_fin1 =int(input())
    date_debut2 = int(input())
    date_fin2 =int(input())
    if date_debut2<=date_debut1<=date_fin2 or date_debut2<=date_fin1<=date_fin2 or date_debut1<=date_debut2<=date_fin1 or date_debut1<=date_fin2<=date_fin1:
        print("Amis")
    else:
        print("Pas amis")
           
main()
