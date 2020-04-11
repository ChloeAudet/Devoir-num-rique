
import numpy as np
import matplotlib.pyplot as plt

Nh = 301  # nombre de noeuds dans la direction des x
Nv = 51  # nombre de noeuds dans la direction des y

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

nb_iterations = 100
n = 0

# calcul méthode relaxation
while n <= nb_iterations:
    cavite_modifiee = cavite.copy()
    for j in range(1, Nv - 1):
        for i in range(1, Nh - 1):
            # électrode maintenue à un potentiel nul
            if j == 25 and i > 15:
                cavite_modifiee[j][i] = 0
            elif j < 10 and i < 18:
                continue
            elif i < 10 and j > 6 and j < 16:
                continue
            elif i < 22 and j > 40:
                continue
            elif j > 34 and j < 45 and i < 15:
                continue
            else:
                cavite_modifiee[j][i] = 0.25*(cavite[j+1][i] + cavite[j-1][i] + cavite[j][i+1] + cavite[j][i-1])
    n += 1
    cavite = cavite_modifiee

color_map = plt.imshow(cavite)
cb = plt.colorbar(orientation='horizontal')
plt.show()




