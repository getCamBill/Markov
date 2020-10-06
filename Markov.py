import re
import numpy as np
import matplotlib.pyplot as plt

"""
Добро пожаловать в этот код, написанный с энтузиазмом и Camille.
Надеюсь, вы не использовали онлайн-переводчик ...
"""

"""
(a) Écrire une fonction simu, prenant pour paramètres Q, X0 et un
entier n, et renvoyant une trajectoire de la chaîne de Markov
jusqu'au temps n.
"""
def simu(Q, Xo, n) -> list:
    """
    fonction simu renvoyant une trajectoire de la chaîne de Markov
    jusqu'au temps n.

    :param Q:matrice de transition
    :param Xo: condition initiale, qui peut être une variable aléatoire
    :param n:temps n
    :return: trajectoire de la chaîne de Markov
    """
    # tautologies
    zero, un, deux, trois, quatre = 0, 1, 2, 3, 4
    # Condition initiales:
    x0 = int(np.random.random() < Xo)
    trajectoire = [x0]
    for t in range(un, n + un):
        _1 = Q[x0-un,zero]
        _2 = _1 + Q[x0 - un, un]
        _3 = _2 + Q[x0 - un, deux]
        rd = np.random.random()
        x0 = un if rd < _1 else deux if rd < _2 else trois if rd < _3 else quatre
        trajectoire.append(x0)

    return trajectoire

def trouver_mesure_invariante(Pi) -> list:
    """
    Permet de retrouver les mesures invariantes
    :param Pi: matrice stochastique
    :return:
    """
    pi1 = Pi.transpose() # il faut transposer la matrice de départ
    propre = np.linalg.eig(pi1)[1] # le vecteur propre
    return abs(propre[:, 0]/sum(abs(propre[:, 0]))).transpose()

"""
(d) 
Écrire une fonction permettant de calculer le nombre moyen de fois,
noté Mn, que la chaîne réalise le motif 123 lors d'une trajectoire
en fonction de n.
"""
def Mn(Q, Xo, n, N) -> tuple:
    сумма = [] # somme en Russe, comme notre gas est Russe ...

    def шаблон(traj: list) -> int: # pattern en Russe, ceci n'est pas un runingag ...
        nb = len(re.findall('123', "".join(map(str, traj)), re.DOTALL))
        return nb

    for i in range(1, N):
        сумма.append(шаблон(simu(Q, Xo, n)))
    return sum(сумма)/n, сумма

def Fonction(Q, Xo, n) -> tuple:
    список = [] # liste en Russe, toujours pas ...
    for i in range(1, n):
        список.append(simu(Q, Xo, n)[n])
    return список.count(1)/n, список.count(2)/n,список.count(3)/n,список.count(4)/n

def show(Mn: list, idnum: int) -> plt:
    if idnum != 1:
        chaine_1 = "Graphe de la suite Mn"
        chaine_2 = "Nb apparition du motif '123'"
        chaine_3 = "n simulation"
    else:
        chaine_1 = "Graphe de la trajectoire"
        chaine_2 = "Etats"
        chaine_3 = "temps n"

    taille = len(Mn)
    copernic = [ i for i in range(taille)]
    plt.scatter(copernic, Mn, color='firebrick')
    plt.plot(copernic, Mn, color='darkslategrey')
    plt.title(chaine_1)
    plt.xlabel(chaine_3)
    plt.ylabel(chaine_2)
    plt.show()

# --------------------------------------
if __name__ == "__main__":

    X_0 = np.random.randint(1, 15)

    # (a)
    P = np.array([[0, 2/7, 2/7, 3/7],
                  [3/17, 9/17, 5/17, 0],
                  [1/4, 1/4, 1/4, 1/4],
                  [1/3, 1/3, 1/3, 0]])

    Riazan = simu(P, X_0, 10) # ville de naissance de Andreï Andreïevitch Markov, un mec famous
    print(Fonction(P, X_0, 1000)) # => (0.182, 0.37, 0.279, 0.169) proche de [0.18814905 0.37385461 0.28588882 0.15210751]
    print("Trajectoire : ",Riazan)
    show(Riazan, 1)
    # (d)
    print("Mesure invarainte : ",trouver_mesure_invariante(P))
    blobe = Mn(P, X_0, 10, 100)
    print("Pour n = 100 :", blobe[0])
    show(blobe[1], 2)
    blobe = Mn(P, X_0, 10, 1000)
    print("Pour n = 1 000 :", blobe[0])
    show(blobe[1], 2)
    blobe = Mn(P, X_0, 10, 10000)
    print("Pour n = 10 000 :", blobe[0])
    # show(blobe[1], 2)
    blobe = Mn(P, X_0, 10, 100000)
    print("Pour n = 100 000 :", blobe[0])
    # show(blobe[1], 2)


# ---------------------------------------
