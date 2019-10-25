import math

def verification_triplet(a,b,c):
    return a**2+b**2==c**2

def liste_triplets_brut_smart_smart_smart(seuil):
    resultat = []
    seuil_a = min(math.ceil((-1+math.sqrt(2*seuil**2-1))/(2)),seuil-2)
    for a in range(1,seuil_a+1):
        seuil_b = min(math.ceil(math.sqrt(seuil**2-a**2)),seuil-1)
        for b in range(a+1,seuil_b+1):
            test = math.sqrt(a**2+b**2)
            seuil_c_bas = max(b+1,math.floor(test))
            seuil_c_haut = min(math.ceil(test),seuil)
            if seuil_c_bas<=seuil:
                for c in range(seuil_c_bas,seuil_c_haut+1):
                    if verification_triplet(a,b,c):
                        resultat.append((a,b,c))
    return resultat
