
					Achat de livres

Vous commencez à apprendre une nouvelle langue et décidez d'acheter quelques livres pour vous entraîner. Vous trouvez un vendeur qui propose de nombreux livres à des prix avantageux. Vous disposez d'une certaine somme d'argent et vous vous demandez combien de livres vous pouvez acheter, sachant qu'ils sont tous au même prix.

Ce que doit faire votre programme :
Votre programme doit commencer par lire la somme d'argent dont vous disposez et lira ensuite le prix d'un livre. Il devra ensuite afficher un entier, le plus grand nombre de livres qu'il vous est possible d'acheter avec cette somme d'argent.

Exemple
entrée :

27
5
sortie :

5
_______________

def main():
    budget=int(input())
    prix=int(input())
    print(budget//prix)
main()    

