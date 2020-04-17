# -*- coding: utf-8 -*-

# Noms : Corinne Dumais, Élodie Lescure, Chloé Lavoie-Audet, Aricia Proulx

import numpy as np
import matplotlib.pyplot as plt

Nh = 301  # nombre de noeuds horizontaux
Nv = 51  # nombre de noeuds verticaux

# initialisation de la matrice
cavite = np.zeros([51, 301])

cavite[:, 300] = 300
cavite[0, 20:] = 300
cavite[50, 20:] = 300
cavite[:, 0] = 0
cavite[15:36, 0] = 300
cavite[23:28, 15:301] = 0
cavite[0:8, 0:20] = 0
cavite[0:15, 0:10] = 0
cavite[36:51, 0:10] = 0
cavite[43:51, 0:20] = 0
cavite[:9, 20] = 300
cavite[42:, 20] = 300
cavite[8:16, 10] = 300
cavite[35:43, 10] = 300
cavite[8, 10:21] = 300
cavite[42, 10:21] = 300
cavite[15, :11] = 300
cavite[35, :11] = 300

# assignation d'une valeur au nombre d'itérations
nb_iterations = 200
n = 0

colonne_zeros = np.zeros((51, 1))
ligne_zeros = np.zeros((1, 301))

ancienne_cavite = cavite.copy()
list_iterations = []
list_diff = []

# calcul avec méthode matricielle
while n <= nb_iterations:
    cavite = 0.25*(np.vstack((ancienne_cavite[1:, 0:], ligne_zeros))
                            + np.vstack((ligne_zeros, ancienne_cavite[:50, 0:]))
                            + np.hstack((ancienne_cavite[0:, 1:], colonne_zeros))
                            + np.hstack((colonne_zeros, ancienne_cavite[0:, :300])))
    cavite[:, 300] = 300
    cavite[0, 20:] = 300
    cavite[50, 20:] = 300
    cavite[:, 0] = 0
    cavite[15:36, 0] = 300
    cavite[23:28, 15:301] = 0
    cavite[0:8, 0:20] = 0
    cavite[0:15, 0:10] = 0
    cavite[36:51, 0:10] = 0
    cavite[43:51, 0:20] = 0
    cavite[:9, 20] = 300
    cavite[42:, 20] = 300
    cavite[8:16, 10] = 300
    cavite[35:43, 10] = 300
    cavite[8, 10:21] = 300
    cavite[42, 10:21] = 300
    cavite[15, :11] = 300
    cavite[35, :11] = 300

    n += 1
    list_iterations.append(n)
    list_diff.append(np.mean((cavite - ancienne_cavite) ** 2) / 14191)
    ancienne_cavite = cavite


# affichage du graphique pour la méthode de
plt.plot(list_iterations, list_diff)
plt.xlabel("Nombre d'itérations")
plt.ylabel("Variation moyenne[V]")
plt.yscale('log')
plt.xlim(0, nb_iterations)
plt.ylim(0.000001, 1)
plt.title("Variation du potentiel en fonction du nombre d'itérations pour la méthode matricielle")
plt.show()