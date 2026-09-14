def main():
    prenoms=input().split()
    lettres="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    RES=[]
    for prenom in prenoms:
        nombre = 0
        for lettre in prenom:
            for i in range(26):
                if lettre == lettres[i]:
                    nombre+=i
        while nombre >= 10:
            somme =0
            while nombre > 0:
                chiffre = nombre % 10
                somme = somme + chiffre
                nombre = nombre // 10
            nombre = somme
        RES.append(nombre)
    print(RES[0], RES[1])
main()

