import math

def liste_triplets_optimise(seuil):
    resultat = []
    coef_a = (-1+math.sqrt(2*seuil**2-1))/(2*seuil)
    seuil_a = math.ceil(seuil*coef_a)
    for a in range(1,seuil_a+1):
        coef_b = math.sqrt(1-a**2/seuil**2)
        seuil_b = min(math.ceil(seuil*coef_b),seuil-1)
        for b in range(a+1,seuil_b+1):
            test = math.sqrt(a**2+b**2)
            seuil_bas = math.floor(test)
            seuil_haut = math.ceil(test)
            if seuil_bas<=seuil:
                for c in range(max(max(a,b)+1,math.floor(test)),min(seuil,math.ceil(test))+1):
                    if verification_triplet(a,b,c):
                        resultat.append((a,b,c))
    return resultat
