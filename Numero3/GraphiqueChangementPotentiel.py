# -*- coding: utf-8 -*-

# Noms : Corinne Dumais, Élodie Lescure, Chloé Lavoie-Audet, Aricia Proulx

import numpy as np
import matplotlib.pyplot as plt

Nh = 301  # nombre de noeuds horizontaux
Nv = 51  # nombre de noeuds verticaux

# initialisation de la matrice
cavite = np.array([[0 for x in range(Nh)] for y in range(Nv)])

# initialisation du potentiel sur la paroi supérieur
for i in range(20, Nh):
    cavite[0][i] = 300

# initialisation du potentiel sur la paroi inférieur
for i in range(20, Nh):
    cavite[50][i] = 300

# initialisation du potentiel sur la paroi de droite
for i in range(Nv):
    cavite[i][300] = 300

# initialisation du potentiel sur la paroi de gauche
for i in range(9):
    cavite[i][20] = 300

for i in range(42, Nv):
    cavite[i][20] = 300

for i in range(15, 36):
    cavite[i][0] = 300

for i in range(8, 16):
    cavite[i][10] = 300

for i in range(11):
    cavite[15][i] = 300

for i in range(10, 21):
    cavite[8][i] = 300

for i in range(35, 43):
    cavite[i][10] = 300

for i in range(11):
    cavite[35][i] = 300

for i in range(10, 21):
    cavite[42][i] = 300

# assignation d'une valeur au nombre d'itérations
nb_iterations = 410
compteur_iterations = 0

# liste des valeurs en y
list_diff = []

# liste des valeurs en x
list_nb_iterations = []

# calcul méthode de la relaxation
while compteur_iterations <= nb_iterations:

    cavite_modifiee = cavite.copy()
    somme_diff_potentiel = 0
    compteur = 0

    for j in range(1, Nv - 1):
        for i in range(1, Nh - 1):
            if 22 < j < 28 and i > 15:
                cavite_modifiee[j][i] = 0
            elif j < 9 and i < 21:
                cavite_modifiee[j][i] = 0
            elif i < 11 and j < 16:
                cavite_modifiee[j][i] = 0
            elif i < 21 and j > 41:
                cavite_modifiee[j][i] = 0
            elif j > 34 and i < 11:
                cavite_modifiee[j][i] = 0
            else:
                cavite_modifiee[j][i] = 0.25*(cavite[j+1][i] + cavite[j-1][i] + cavite[j][i+1] + cavite[j][i-1])

            somme_diff_potentiel += (cavite_modifiee[j][i]-cavite[j][i])
            compteur += 1

    compteur_iterations += 1
    list_nb_iterations.append(compteur_iterations)
    list_diff.append(somme_diff_potentiel/compteur)
    cavite = cavite_modifiee

# affichage du graphique pour la méthode de la relaxation
plt.plot(list_nb_iterations, list_diff)
plt.yscale('log')
plt.show()

