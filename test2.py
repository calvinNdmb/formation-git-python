a=10#Créer une variable de type int
b=5.5#Créer une variable de type float
c='hello'#Créer une variable de type string
d=True#Créer une variable de type booléen
e=[1,2,3]#Créer une variable de type liste

#boucle for
for i in range(5):
    print(i)#affiche i de 0 à 4

while a > 0:
    print(a)#affiche a tant que a est supérieur à 0
    a -= 1#diminue a de 1 à chaque itération

def addition(x,y):
    return x + y#fonction qui retourne la somme de x et y

#appel de la fonction addition
resultat = addition(3,4)
print(resultat)#affiche le résultat de l'addition

