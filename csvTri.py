import csv
import codecs
fichier = codecs.open("Communes.csv",'r','utf-8')
# On transforme le fichier csv en une liste de dictionnaire
lecteur = list(csv.DictReader(fichier))
liste=[] # on créé la liste vide pouvoir la trier après
# boucle for pour stocker les valeurs dans une liste
asso=[]
for i in range (len(liste)):
    asso.append(liste)
for i in range (len(lecteur)):
    liste.append(lecteur[i]["PTOT"])
index_mini=0
# for i in lecteur:
for i in range(len(liste)):
    # On prend comme valeur minimale le premier élément de la partie non triée de la liste
    index_mini = i
    # On recherche dans la partie non triée le plus petit élément
    for j in range(i+1,len(liste)):
        # Si l’élément regardé est plus petit que celui enregistré
        if liste[j] < liste[index_mini]:
            # On enregistre la position de cet élément
            index_mini = j
    # On enregistre temporairement la première valeur de la partie non triée de la liste
    tmp = liste[i]
    # ON échange la première valeur de la partie non triée de la liste avec la plus valeur valeur de la partie non triée
    liste[i]=liste[index_mini]
    # On replace la valeur enregistrée dans la partie non triée de la liste
    liste[index_mini]=tmp
# bon une fois qu'on a tout trier on peut passer a la partie où il faut associer chaque ville avec sa PTOT
# print(liste)