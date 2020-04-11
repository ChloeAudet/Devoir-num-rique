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

nb_iterations = 25
n = 0
w = 0.75  # Environ maximum avant que l'image soit affectée
            # et éventuellement que la convergence soit brisée

# calcul Gauss-Seidel
while n <= nb_iterations:
    for j in range(1, Nv - 1):
        for i in range(1, Nh - 1):
            if j > 22 and j < 28 and i > 15:
                cavite[j][i] = 0
            elif j < 9 and i < 21:
                continue
            elif i < 11 and j < 16:
                continue
            elif i < 21 and j > 41:
                continue
            elif j > 34 and i < 11:
                continue
            else:
                cavite[j][i] = 0.25 * (1 + w) * (cavite[j+1][i] + cavite[j-1][i]
                           + cavite[j][i+1] + cavite[j][i-1]) - w * cavite[j][i]
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
plt.title('Potentiel dans la cavité pour ' + str(nb_iterations) + ' itérations avec Gauss-Seidel et Sur-relaxation')
plt.show()