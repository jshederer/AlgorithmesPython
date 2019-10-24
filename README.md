# AlgorithmesPython
 Algorithmes en Python pour les mathématiques

TripletsPythagore.py:
 Algorithme testé par rapport à l'algorithme basique avec un seuil de 1100
 L'algorithme basique est optimisé en prenant en compte les règles suivantes:
   * a < b < c donc a < seuil-2 et b < seuil-1
   * lorsque l'on parcourt les a pour un a donné, on pose que ...
   * lorsque l'on parcourt les b pour un a donné, on pose que le maximum possible pour b²=seuil²-a²
   * lorsque l'on parcourt les C pour un a et un b donnés, on pose que l'on cherche autour de c²=a²+b² (on cherche autour en raison des limitations techniques des nombres décimaux codés informatiquement)
