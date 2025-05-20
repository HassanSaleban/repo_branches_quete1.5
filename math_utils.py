# Variables
PI = 3.14159
GRAVITY = 9.81

def carre(x):
    return x ** 2

def cube(x):
    return x ** 3

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n-1)

def aire_cercle(rayon):
    return PI * rayon ** 2

def energie_cinetique(masse, vitesse):
    return 0.5 * masse * vitesse ** 2
