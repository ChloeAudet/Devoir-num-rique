# -*- coding: utf-8 -*-

# Noms : Corinne Dumais, Élodie Lescure, Chloé Lavoie-Audet, Aricia Proulx

somme_relaxation = 5.915609836578369 + 5.979467868804932 + 5.976499795913696 + 5.861330986022949 + 6.20742392539978
print("Le temps moyen de calcul pour la méthode de la relaxation est: " + str(somme_relaxation/5))

somme_GS = 4.98681902885437 + 5.042869806289673 + 4.990609884262085 + 4.942980766296387 + 5.064237833023071
print("Le temps moyen de calcul pour la méthode de Gauss-Seidel est: " + str(somme_GS/5))

somme_SR = 3.184922933578491 + 3.1703970432281494 + 3.2503790855407715 + 3.1489179134368896 + 3.2011489868164062
print("Le temps moyen de calcul pour la méthode de la sur-relaxation est: " + str(somme_SR/5))

somme_mat = 0.03434014320373535 + 0.02876114845275879 + 0.02762603759765625 + 0.02848505973815918 + 0.030688762664794922
print("Le temps moyen de calcul pour la méthode matricielle est: " + str(somme_mat/5))
