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
