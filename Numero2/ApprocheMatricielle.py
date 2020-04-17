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
cavite[15:36, 0] = 300
cavite[:9, 20] = 300
cavite[42:, 20] = 300
cavite[8:16, 10] = 300
cavite[35:43, 10] = 300
cavite[8, 10:21] = 300
cavite[42, 10:21] = 300
cavite[15, :11] = 300
cavite[35, :11] = 300

# assignation d'une valeur au nombre d'itérations
nb_iterations = 150
n = 0

colonne_zeros = np.zeros((51, 1))
ligne_zeros = np.zeros((1, 301))

# calcul avec méthode matricielle
while n <= nb_iterations:
    cavite = (np.vstack((cavite[1:, 0:], ligne_zeros)) + np.vstack((ligne_zeros, cavite[:50, 0:]))
              + np.hstack((cavite[0:, 1:], colonne_zeros)) + np.hstack((colonne_zeros, cavite[0:, :300])))/4
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

# affichage du graphique 2d
color_map = plt.imshow(cavite, aspect='auto')
cb = plt.colorbar(orientation='vertical')
plt.xlabel('X[mm]')
# plt.xticks((50, 100, 150, 200, 250, 300), ('10', '20', '30', '40', '50', '60'))
# plt.yticks((0, 10, 20, 30, 40), ('10', '8', '6', '4', '2'))
plt.ylabel('Y[mm]')
plt.text(1.175, 0.5, 'Potentiel[V]', horizontalalignment='left', verticalalignment='center',
         rotation=90, clip_on=False, transform=plt.gca().transAxes)
plt.title('Potentiel dans la cavité pour ' + str(nb_iterations) + ' itérations avec une approche matricielle')
plt.show()