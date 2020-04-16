# -*- coding: utf-8 -*-

# Noms : Corinne Dumais, Élodie Lescure, Chloé Lavoie-Audet, Aricia Proulx

import numpy as np
import matplotlib.pyplot as plt

Nh = 301  # nombre de noeuds horizontaux
Nv = 51  # nombre de noeuds verticaux

# initialisation de la matrice
cavite = np.array([[0 for x in range(Nh)] for y in range(Nv)])

# initialisation du potentiel sur la paroi supérieur
for n in range(20, Nh):
    cavite[0][n] = 300

# initialisation du potentiel sur la paroi inférieur
for n in range(20, Nh):
    cavite[50][n] = 300

# initialisation du potentiel sur la paroi de droite
for n in range(Nv):
    cavite[n][300] = 300

# initialisation du potentiel sur la paroi de gauche
for n in range(9):
    cavite[n][20] = 300

for n in range(42, Nv):
    cavite[n][20] = 300

for n in range(15, 36):
    cavite[n][0] = 300

for n in range(8, 16):
    cavite[n][10] = 300

for n in range(35, 43):
    cavite[n][10] = 300

for n in range(11):
    cavite[15][n] = 300

for n in range(10, 21):
    cavite[8][n] = 300

for n in range(11):
    cavite[35][n] = 300

for n in range(10, 21):
    cavite[42][n] = 300

# assignation d'une valeur au nombre d'itérations
nb_iterations = 150
n = 0
cavite_initiale = cavite.copy()
list_iterations = []
list_diff = []

# calcul méthode de la relaxation
while n <= nb_iterations:
    cavite_modifiee = cavite.copy()
    somme_diff = 0
    for j in range(1, Nv - 1):
        for i in range(1, Nh - 1):
            if 22 < j < 28 and i > 14:
                continue
            elif j < 9 and i < 21:
                continue
            elif i < 11 and j < 16:
                continue
            elif i < 21 and j > 41:
                continue
            elif j > 34 and i < 11:
                continue
            else:
                cavite_modifiee[j][i] = 0.25*(cavite[j+1][i] + cavite[j-1][i] + cavite[j][i+1] + cavite[j][i-1])
                somme_diff += (cavite_modifiee[j][i]-cavite[j][i])
    n += 1
    list_iterations.append(n)
    list_diff.append(somme_diff/14191)
    cavite = cavite_modifiee

# affichage du graphique pour la méthode de la relaxation
plt.plot(list_iterations, list_diff)
plt.xlabel("Nombre d'itérations")
plt.ylabel("Variation moyenne[V]")
plt.show()

