# Kermesse

# Ce que doit faire votre programme :
# Toucher la cible au premier tir rapporte un bonbon, toucher la cible au deuxième tir rapporte deux bonbons de plus, la toucher au troisième tir rapporte encore trois bonbons de plus, etc. Écrivez un programme qui affiche sur la première ligne le nombre total de bonbons obtenus si l'on ne réussit qu'1 tir, puis qui affiche sur la deuxième ligne le nombre de bonbons récupérés si l'on réussit 2 tirs de suite, puis sur la troisième ligne le nombre de bonbons récupérés si l'on réussit 3 tirs de suite, etc. jusqu'à la valeur que l'on peut récupérer si l'on réussit 50 tirs de suite.
# Par exemple, si votre programme s'arrêtait à 5 et non à 50, il devrait afficher ceci 
nbBonbonTir=0
for loop in range(1,51):
    nbBonbonTir=nbBonbonTir+loop
    print(nbBonbonTir)
