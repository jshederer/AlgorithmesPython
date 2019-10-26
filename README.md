# AlgorithmesPython
 Algorithmes en Python pour les mathématiques

TripletsPythagore.py:
 L'algorithme basique est optimisé en prenant en compte les règles suivantes:
   * a < b < c donc a < seuil-2 et b < seuil-1
   * lorsque l'on parcourt les a pour un a donné, on pose que a est au maximum égal au seuil multiplié par un coefficient D. b>=a+1. Si a=max(a)==D*seuil, b>=max(a)+1 donc b>=D*seuil+1. On obtient alors (D*seuil)²+(D*seuil+1)² <= a²+b². c<=seuil donc c²<=seuil². a²+b²=c². Si a=max(a)=D*seuil, on a alors (D*seuil)²+(D*seuil+1)²<=seuil². Le coefficient D doit être au minimum celui pour lequel (D*seuil)²+(D*seuil+1)²=seuil² donc 2*seuil²*D²+2*seuil*D+(1-seuil²)=0. Il suffit alors de résoudre l'équation polynomiale du second degré de variable D. Le discriminant est 4*seuil²*(2*seuil²-1). D doit être compris entre 0 et 1 pour optimiser l'algorithme. La racine positive simplifiée de l'équation polynomiale est: (-1+sqrt(2*seuil²-1))/(2*seuil). max(a)=D*seuil=(-1+sqrt(2*seuil²-1))/2
   * lorsque l'on parcourt les b pour un a donné, on pose que le maximum possible pour b²=seuil²-a²
   * lorsque l'on parcourt les C pour un a et un b donnés, on pose que l'on cherche autour de c²=a²+b² (on cherche autour en raison des limitations techniques des nombres décimaux codés informatiquement: afin de ne pas subir les effets de bord du codage informatique imparfait, on reste sur des calculs en valeur entière)
   L'algorithme a été testé par rapport à l'algorithme brut avec de nombreux seuils différents.
   Pour un seuil de 100, l'algorithme utilise 6799 boucles contre 166650 pour l'algorithme brut.
   Pour un seuil de 500, l'algorithme utilise 185135 boucles (moins d'une seconde) contre 20833250 (plus de 20 secondes) pour l'algorithme brut.
   
 
