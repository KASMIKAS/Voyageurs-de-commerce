import random
import math

'''Vous devez enlever le commentaire du fichier que vous voulez utiliser ou vous devez ecrire la direction du fichier 
que vous voulez tester avec dans votre repertoire'''
#fichier = 'C:/Users/KASMI/PycharmProjects/calculatrice/venv/Scripts/tsp101.txt'
#fichier = 'C:/Users/KASMI/PycharmProjects/calculatrice/venv/Scripts/tsp50.txt'
fichier = 'C:/Users/KASMI/PycharmProjects/calculatrice/venv/Scripts/tsp5.txt'
#fichier = 'C:/Users/KASMI/PycharmProjects/calculatrice/venv/Scripts/tsp25.txt'
#chemin = generer_sol_ini(25)
'''Ici vous devez modifiez n, par exemple si vous tester tsp5.txt => n = 5'''
n = 5
def generer_sol_ini(n):
    # Initialiser la liste S avec [1, 2, ..., n]
    S = list(range(1, n+1))

    # Générer une permutation aléatoire en utilisant l'algorithme décrit
    for i in range(1, n+1):
        # Tirer un entier aléatoire entre 1 et n
        j = random.randint(1, n)

        # Échanger S[i] et S[j]
        S[i-1], S[j-1] = S[j-1], S[i-1]

    return S
chemin = generer_sol_ini(n)
'''############################################################################################'''


def distance_euclidienne(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

'''############################################################################################'''
def lire_fichier(fichier):
    with open(fichier, 'r') as f:
        lignes = f.readlines()

    donnees = [ligne.strip().split('\t')[1:] for ligne in lignes[1:]]  # Ignorer la première ligne
    return donnees

'''############################################################################################'''



def distance_chemin(n,fichier,chemin):
    dist_final = 0
    donnees = lire_fichier(fichier)
    print(chemin)
    elt = 0
    i = 0
    id_point1 = chemin[0]
    x1, y1 = map(int, donnees[id_point1 - 1])
    dist = distance_euclidienne(x1, y1, 0, 0)
    while elt < n  :
        id_point1 = chemin[i]
        id_point2 = chemin[i + 1]
        elt = elt + 1
        i = i + 1
        # Récupérez les coordonnées des points à partir des données
        x1, y1 = map(int, donnees[id_point1 - 1])
        x2, y2 = map(int, donnees[id_point2 - 1])
        # Calculez la distance euclidienne
        dist = dist + distance_euclidienne(x1, y1, x2, y2)
        if i == n-1 :
            id_point1 = chemin[-1]
            x1, y1 = map(int, donnees[id_point1 - 1])
            dist_final = dist + distance_euclidienne(x1, y1, 0, 0)
            break

    return dist_final


#distance_chemin(5,fichier,chemin)





'''############################################################################################'''


def generer_listes_voisines(lst):
    voisines = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            # Créer une copie de la liste
            liste_voisine = lst.copy()

            # Échanger les éléments i et j
            liste_voisine[i], liste_voisine[j] = liste_voisine[j], liste_voisine[i]

            # Ajouter la liste voisine à la liste resultante
            voisines.append(liste_voisine)


    return voisines


# Exemple d'utilisation

#voisines = generer_listes_voisines(chemin)

#print(f"Liste initiale : {chemin}")
#print(f"Listes voisines : {voisines}")

'''############################################################################################'''


def meilleur_voisin(chemin):
    tab_de_val = []
    voisines = generer_listes_voisines(chemin)
    for v in voisines:
        distance = distance_chemin(n,fichier,v)
        tab_de_val.append(distance)
    m_v = min(tab_de_val)
    indexx = tab_de_val.index(m_v)
    return voisines[indexx]




'''############################################################################################'''

def meth_hill_climbing(n,chemin,max_depl):
    s = generer_sol_ini(n)
    nb_depl = 0
    stop = False
    while nb_depl <= max_depl and stop != True :
        s_prim = meilleur_voisin(chemin)
        if distance_chemin(n,fichier,s_prim) < distance_chemin(n,fichier,s):
            s = s_prim
        else:
            stop = True
        nb_depl = nb_depl + 1
    return print("Pour la methode de Hill Climbing on a trouve :",s,"de distance :", distance_chemin(n,fichier,s))
# Exemple d'utilisation
#max_depl = 10
#meth_hill_climbing(n,chemin,max_depl)
#print(distance_chemin(n,fichier,[11, 7, 9, 6, 4, 25, 22, 18, 8, 3, 17, 13, 2, 5, 16, 15, 12, 20, 23, 24, 21, 14, 19, 1, 10]))

'''############################################################################################'''


def meth_tabou(n,chemin,max_depl):
    s = generer_sol_ini(n)
    print("chemin :", s)
    tabous = []
    nb_depl = 0
    msol = s
    stop = False
    voisines = generer_listes_voisines(s)
    while nb_depl <= max_depl and stop == False :
        if len(voisines) != 0 :
            if all(elt != tabous for elt in voisines):
                s_prime = meilleur_voisin(s)
                    #print("Les voisins :",voisines)
                    #print("s_prime :",s_prime)
                    #print("msol :",msol)
            else:
                stop == True
        if len(tabous) == n:
            tabous = []
        tabous = tabous + [s]
        if distance_chemin(n,fichier,s_prime) < distance_chemin(n,fichier,msol)  :
            msol = s_prime
        s = s_prime
        nb_depl = nb_depl + 1
    return  print(" Pour la methode de tabou on a trouver :",msol,"de distance :",distance_chemin(n,fichier,msol))

# Exemple d'utilisation

#max_depl = 10
#chemin = generer_sol_ini(n)
#print(chemin)
#meth_tabou(n,chemin,max_depl)
#print(meth_tabou(n,chemin,max_depl))

