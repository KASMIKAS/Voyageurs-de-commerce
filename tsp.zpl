# KASMI Mohamed amine
# pour tester sur plusieurs fichiers il suffit de changer la variable fichier 
# par le nom du fichier que vous voulez texter avec.


param fichier := "tsp5.txt";


param nb := read fichier as "1n" use 1;
set I := {0..nb};
set Villes := {read fichier as "<1n>" skip 1, <0>};
param a[Villes] := read fichier as "<1n> 2n" skip 1, <0> 0;
param b[Villes] := read fichier as "<1n> 3n" skip 1, <0> 0;
var u[I] ;
var x[I*I] binary;


# Define the distance function
defnumb d(i,j) := sqrt((a[i] - a[j])^2 + (b[i] - b[j])^2);


# Objective function
minimize total_distance:
    sum <i,j> in I*I: x[i,j] * d(i,j);


# Constraints
subto c1:
    forall <j> in I : sum <i> in I with j != i: x[i,j] == 1;

subto c2:
    forall <i> in I : sum <j> in I with i != j: x[i,j] == 1;
	
subto c3 :
         u[0] == 1;

subto c4:
        forall <i> in {1..nb}:
		        u[i] >= 2 and u[i] <= nb + 1;

set Z := {1..nb};


subto c5:
    forall <i,j> in Z*Z with i != j:
	        u[i] - u[j] + 1 <= (nb+1)*(1-x[i,j]);





