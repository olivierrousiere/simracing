# ouvrir fichier data/heart/data_cleaned_up.csv
# compter combien de passants ont num=0 et num=1
# calculer le ratio sexe/num ==> pour num = 1 quel est le ration sex=0 et sex =1: calculer le nom de malade H/nbre malades totaux: compter le nbre de lignes, compter chaque cas, faire ratio

import csv

fm = 0
hm = 0
c = 0

with open("data/heart/data_cleaned_up.csv") as f:
    with open("data/house/out_heart.csv", "w") as g:
        reader = csv.DictReader(f)  #DicReader : lit mais considère la 1ere ligne comme une entête (et non une ligne de data) alors que reader prend tout en data
        for row in reader:
            if int(row["num"]) == 1:
                c +=1
                if int(row["sex"]) == 0:
                    fm += 1
                else:
                    hm += 1
            g.write
        print(fm, hm, c)
        print(100*fm/c, 100*hm/c)




