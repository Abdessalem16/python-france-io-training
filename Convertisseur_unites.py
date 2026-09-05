                            Convertisseur d'unités

Ce que doit faire votre programme :
Écrivez un programme qui convertit des valeurs du système métrique en valeurs du système de mesure américain. On fournit des mesures à votre programme, en mètres, grammes ou degrés Celsius et vous devez les convertir respectivement en pieds, livres et degrés Fahrenheit.

Voici les règles de conversion à utiliser :

1 pied = 0,3048 mètres ;
1 gramme = 0,002205 livres ;
température en degrés Fahrenheit = 32 + 1,8 × température en degrés Celsius.
On vous donne sur la première ligne le nombre de conversions à effectuer, puis sur les lignes suivantes la valeur à convertir, et son unité : m, g ou c (avec une espace entre les deux).

Affichez en sortie les valeurs converties, suivies d'une espace et de leur unité : p, l ou f.

Il n'est en fait pas judicieux d'écrire des fonctions pour résoudre cet exercice : le mieux est de définir des constantes. Vous pouvez aussi profiter de cet exercice pour expérimenter l'instruction « selon », switch dans certains langages.

Exemple
entrée :

4
12.3 m
1245.243 g
37.2 c
23 g
sortie :

40.354331 p
2.745761 l
98.960000 f
0.050715 l
Commentaires
L'entrée indique qu'il y a quatre valeurs à convertir. La première est 12,3 mètres, ce qui, une fois converti, donne approximativement 40,354331 pieds. La deuxième est 1245,243 grammes, soit environ 2,745761 livres, la troisième est 37,2 degrés Celsius, soit 98,96 degrés Farenheit, et la quatrième est 23 grammes, soit 0,050715 livres.
_________________________________________
def main():
    mesure=int(input())
    for i in range (mesure):
        valeur,unite = input().split()
        valeur=float(valeur)
        if unite == "m":
            res=valeur/0.3048
            print(res,"p")
        elif unite =="g":
            res=valeur*0.002205
            print(res,"l")
        elif unite=="c":    
            res=32+(1.8*valeur)
            print(res,"f")
        
main()

