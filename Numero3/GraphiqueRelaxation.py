# -*- coding: utf-8 -*-

# Noms : Corinne Dumais, Élodie Lescure, Chloé Lavoie-Audet, Aricia Proulx

import numpy as np
import matplotlib.pyplot as plt
import time

Nh = 301  # nombre de noeuds horizontaux
Nv = 51  # nombre de noeuds verticaux

# initialisation de la matrice
cavite = np.zeros([51, 301])

# initialisation du potentiel sur la paroi supérieur
for n in range(20, 301):
    cavite[0, n] = 300

# initialisation du potentiel sur la paroi inférieur
for n in range(20, Nh):
    cavite[50, n] = 300

# initialisation du potentiel sur la paroi de droite
for n in range(Nv):
    cavite[n, 300] = 300

# initialisation du potentiel sur la paroi de gauche
for n in range(9):
    cavite[n, 20] = 300

for n in range(42, 51):
    cavite[n, 20] = 300

for n in range(15, 36):
    cavite[n, 0] = 300

for n in range(8, 16):
    cavite[n, 10] = 300

for n in range(35, 43):
    cavite[n, 10] = 300

for n in range(11):
    cavite[15, n] = 300

for n in range(10, 21):
    cavite[8, n] = 300

for n in range(11):
    cavite[35, n] = 300

for n in range(10, 21):
    cavite[42, n] = 300

# assignation d'une valeur au nombre d'itérations
nb_iterations = 250
n = 0
list_iterations = []
list_diff = []

temps_debut = time.time()

# calcul méthode de la relaxation
while n <= nb_iterations:
    cavite_modifiee = cavite.copy()
    for i in range(1, 50):
        for j in range(1, 300):
            if 22 < i < 28 and j > 14:
                continue
            if i < 9 and j < 21:
                continue
            if j < 11 and i < 16:
                continue
            if j < 21 and i > 41:
                continue
            if i > 34 and j < 11:
                continue
            else:
                cavite_modifiee[i, j] = 0.25*(cavite[i+1, j] + cavite[i-1, j] + cavite[i, j+1] + cavite[i, j-1])
    n += 1
    list_iterations.append(n)
    list_diff.append(np.mean((cavite_modifiee - cavite)**2)/14191)
    cavite = cavite_modifiee

    if n > 1:
        if ((list_diff[n-1] - list_diff[n-2])/list_diff[n-2])*100 < 1:
            temps_fin = time.time()

print(temps_fin-temps_debut)

# affichage du graphique pour la méthode de la relaxation
plt.plot(list_iterations, list_diff)
plt.xlabel("Nombre d'itérations")
plt.ylabel("Variation moyenne[V]")
plt.yscale('log')
plt.xlim(0, nb_iterations)
plt.ylim(0.000001, 1)
plt.title("Variation du potentiel en fonction du nombre d'itérations pour la méthode de la relaxation")
plt.show()

