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
nb_iterations = 500
n = 0

colonne_zeros = np.zeros((51, 1))
ligne_zeros = np.zeros((1, 301))

colonne_pot = np.nonzero

# calcul avec méthode matricielle
while n <= nb_iterations:
    cavite_modifiee = np.vstack((cavite[1:, 0:], ligne_zeros)) + np.vstack((ligne_zeros, cavite[:50, 0:])) \
             + np.hstack((cavite[0:, 1:], colonne_zeros)) + np.hstack((colonne_zeros, cavite[0:, :300]))
    cavite_modifiee = cavite_modifiee[1:50, 1:300]
    np.hstack((cavite_modifiee, ))
    n += 1

# affichage du graphique 2d
color_map = plt.imshow(cavite, aspect='auto')
cb = plt.colorbar(orientation='vertical')
plt.xlabel('X[mm]')
plt.xticks((50, 100, 150, 200, 250, 300), ('10', '20', '30', '40', '50', '60'))
plt.yticks((0, 10, 20, 30, 40), ('10', '8', '6', '4', '2'))
plt.ylabel('Y[mm]')
plt.text(1.175, 0.5, 'Potentiel[V]', horizontalalignment='left', verticalalignment='center',
         rotation=90, clip_on=False, transform=plt.gca().transAxes)
plt.title('Potentiel dans la cavité pour ' + str(nb_iterations) + ' itérations avec une approche matricielle')
plt.show()