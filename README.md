# README - Scripts de résolution du Problème du Voyageur de Commerce (TSP)

## Auteur

KASMI Mohamed Amine

## Description

Ces deux fichiers fournissent deux approches différentes pour résoudre le Problème du Voyageur de Commerce (TSP) :

1. **Fichier Python (`fichier1.py`)** : Implémente des méthodes heuristiques pour trouver un chemin proche de l’optimal.

   * Méthodes disponibles :

     * Hill Climbing
     * Recherche Tabou
   * Fonctionnalités :

     * Lecture d’un fichier de données TSP (coordonnées des villes)
     * Génération d’une solution initiale aléatoire
     * Calcul de la distance totale d’un chemin
     * Génération des voisins d’une solution
     * Sélection du meilleur voisin
     * Optimisation par Hill Climbing et Tabou

2. **Fichier Zimpl (`fichier2.zpl`)** : Implémente le TSP sous forme d’un problème d’optimisation mathématique.

   * Utilise des variables binaires pour représenter les arcs entre villes
   * Fonction objectif : minimiser la distance totale parcourue
   * Contraintes :

     * Chaque ville est visitée exactement une fois (c1 et c2)
     * Variables auxiliaires `u[i]` pour éviter les sous-tours (c3, c4, c5)
   * Calcul des distances euclidiennes entre villes à partir des coordonnées

---

## Instructions d’utilisation

### Fichier Python

1. Modifier la variable `fichier` pour pointer vers le fichier TSP souhaité.
2. Ajuster `n` en fonction du nombre de villes dans le fichier.
3. Décommenter la méthode à tester (`meth_hill_climbing` ou `meth_tabou`) et définir `max_depl`.
4. Exécuter le script :

```bash
python fichier1.py
```

### Fichier Zimpl

1. Modifier la variable `fichier` pour pointer vers le fichier TSP souhaité.
2. Les données du fichier doivent être au format :

```
ID	X	Y
1	10	20
2	15	25
...
```

3. Résoudre le modèle dans un solveur compatible Zimpl (ex. CPLEX via Zimpl ou SCIP).

---

## Structure des fichiers

### Python (`fichier1.py`)

* `generer_sol_ini(n)` : génère une permutation aléatoire de villes
* `distance_euclidienne(x1, y1, x2, y2)` : calcule la distance entre deux points
* `lire_fichier(fichier)` : lit le fichier TSP et extrait les coordonnées
* `distance_chemin(n, fichier, chemin)` : calcule la distance totale d’un chemin
* `generer_listes_voisines(lst)` : génère toutes les permutations voisines par échange
* `meilleur_voisin(chemin)` : retourne le voisin avec la plus petite distance
* `meth_hill_climbing(n, chemin, max_depl)` : Hill Climbing pour optimiser le chemin
* `meth_tabou(n, chemin, max_depl)` : Recherche tabou pour optimiser le chemin

### Zimpl (`fichier2.zpl`)

* `param fichier` : nom du fichier TSP
* `param nb` : nombre de villes
* `set I` : ensemble des indices de villes
* `set Villes` : ensemble des villes lues
* `param a, b` : coordonnées X et Y des villes
* `var x[I*I]` : variables binaires pour les arcs
* `var u[I]` : variables auxiliaires pour éviter les sous-tours
* `defnumb d(i,j)` : fonction distance euclidienne
* `minimize total_distance` : fonction objectif
* Contraintes `c1` à `c5` pour garantir un tour valide

---

## Remarques

* Les deux scripts nécessitent que le fichier TSP contienne les coordonnées des villes séparées par tabulations.
* Le fichier Python est adapté pour des TSP de petite taille (ex. 5 à 25 villes).
* Le modèle Zimpl peut traiter des instances plus grandes mais nécessite un solveur pour l’optimisation exacte.

---

## Exemple d’exécution Python

```python
chemin = generer_sol_ini(n)
meth_hill_climbing(n, chemin, max_depl=10)
meth_tabou(n, chemin, max_depl=10)
```

---

## Exemple d’exécution Zimpl

* Charger le fichier `.zpl` dans un solveur compatible (ex. CPLEX via Zimpl)
* Cliquer sur “Run” pour résoudre le TSP et obtenir la distance minimale et les arcs sélectionnés.
