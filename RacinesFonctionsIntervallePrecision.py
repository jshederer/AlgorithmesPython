
def test1(x):
    return x**3-3*x+4

def test2(x):
    return x**2-3*x-4

def test3(x):
    return x**2-3*x+4

test4="x**3-3*x+4"
test5="x**2-3*x-4"
test6="x**2-3*x+4"

def transformation_fonction(fonction,x):
    if type(fonction) == type(str()):
        return eval(fonction.replace("x",str(x)))
    else:
        return fonction(x)

def trouver_racines(fonction,min,max,precision):
    if min>=max:
        print("Le minimum de recherche doit être inférieur au maximum de recherche")
        return False
    x=min
    xprec = x
    fprec = transformation_fonction(fonction,x)
    pas = 10**(-precision)
    print("Pas de balayage de x pour la recherche de racine(s):",pas)
    trouve = False
    while x<=max:
        x=x+pas
        fx = transformation_fonction(fonction,x)
        if fx*fprec<=0:
            #print("Bascule: image de ",xprec,"=>",fprec,"/image de ",x,"=>",fx)
            trouve = True
            if abs(fprec) < abs(fx):
                print("Racine de la fonction:",round(xprec,precision))
            else:
                print("Racine de la fonction:",round(x,precision))
        xprec=x
        fprec=fx
    if not trouve:
        print("Pas de racine pour la fonction")
        return False
    else:
        return True

def trouver_racines_param(fonction,min,max,precision):
    if type(fonction) == type(str()):
        print("Recherche des racines de la fonction",fonction,"sur un intervalle [",min,";",max,"] avec une précision de ",precision)
    else:
        print("Recherche des racines d'une fonction programmée sur un intervalle [",min,";",max,"] avec une précision de ",precision)

    trouver_racines(fonction,min,max,precision)

def trouver_racines_input():
    print("Recherche des racines d'une fonction saisie sur un intervalle saisi avec une précision saisie")
    min=float(input("Saisir le début de l'intervalle de recherche:"))
    max=float(input("Saisir la fin de l'intervalle de recherche:"))
    precision=int(input("Saisir la précision de recherche:"))
    fonction=input("Saisir la fonction:")
    print("Recherche des racines de la fonction",fonction,"sur un intervalle [",min,";",max,"] avec une précision de ",precision)
    trouver_racines(fonction,min,max,precision)

#Exemples:
    # trouver_racines_param(test1,-40,40,1)
    # trouver_racines_param(test1,-3,-2,5)
    # trouver_racines_param(test2,-20,20,4)
    # trouver_racines_param(test3,-20,20,4)
    # trouver_racines_param(test4,-40,40,1)
    # trouver_racines_param(test4,-3,-2,5)
    # trouver_racines_param(test5,-20,20,4)
    # trouver_racines_param(test6,-20,20,4)
    # trouver_racines_input()
