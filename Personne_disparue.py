
Personne disparue

Un personnage important de la cité n'est pas rentré chez lui hier soir et tout le monde est à sa recherche. Or tout habitant de la ville a un numéro unique qui lui est associé et doit signer une sorte de registre quand il sort de la ville. Vous souhaitez savoir si le registre a été signé, auquel cas il faudra étendre les recherches à l'extérieur de la ville.

Ce que doit faire votre programme :
On vous donne un entier, le numéro d'une personne recherchée, puis un entier tailleListe, et enfin tailleListe entiers parmi lesquels vous devez chercher le numéro de la personne. Si le numéro est présent dans la liste (il peut l'être plusieurs fois) vous devez afficher le texte "Sorti de la ville" sinon "Encore dans la ville".
____________
def main():
    numérorecherche =int(input())
    tailleListe=int(input())
    res=False
    for i in range (tailleListe):
        essayer=int(input())
        if essayer ==numérorecherche :
           res=True
           break
        else:
            res=False
    if res:
        print("Sorti de la ville")
    else:
        print("Encore dans la ville")
main()
