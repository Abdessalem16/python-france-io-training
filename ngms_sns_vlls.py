					ngms sns vlls
Les personnes travaillant à la bibliothèque aiment particulièrement se poser des petites énigmes, d’inspiration littéraires. Cette fois-ci, Agrarelle a décidé de créer des énigmes basées sur des titres de livres : elle va supprimer l’ensemble des voyelles (et les espaces) d’un titre et du nom de son auteur et ses collègues devront retrouver le titre original (ainsi que le nom de l’auteur).

Contraintes
Le titre et le nom de l’auteur font chacun moins de 100 caractères.

Ils ne contiennent que des lettres majuscules et des espaces.

Entrée
Sur la première ligne, le titre du livre.

Sur la seconde ligne, le nom de l’auteur.

Sortie
Sur la première ligne, le titre du livre, sans aucune voyelle, ni espace.

Sur la seconde ligne, le nom de l’auteur, sans aucune voyelle, ni espace.

Exemple
entrée :

AUTANT EN EMPORTE LE VENT
MARGARET MITCHELL
sortie :

TNTNMPRTLVNT
MRGRTMTCHLL
__________________________________
def main():
     titre_livre=input()
     nom_auteur=input()
     for i in range (len(titre_livre)):
         if not(titre_livre[i] in ['A','E','I','O','U','Y',' ']):
             print(titre_livre[i],end="")
     print()        
     for j in range (len(nom_auteur)):
         if not(nom_auteur[j] in ['A','E','I','O','U','Y',' ']):
             print(nom_auteur[j],end="")        
             
main()

