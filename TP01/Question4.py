# Affiche un menu d'opérations disponibles
print("Choisissez une operation:\n    1. Addition\n    2. Soustraction\n    3. Multiplication\n    4. Division")
# Demande à l'utilisateur de saisir le numéro de l'opération choisie
operation = int(input())

# Demande à l'utilisateur de saisir deux nombres
nbr1 = float(input("Entrez le premier nombre: "))
nbr2 = float(input("Entrez le second nombre: "))

# Vérifie si l'opération choisie correspond à l'addition
estAddition = operation == 1
# Vérifie si l'opération choisie correspond à la soustraction
estSoustraction = operation == 2
# Vérifie si l'opération choisie correspond à la multiplication
estMultiplication = operation == 3
# Vérifie si l'opération choisie correspond à la division
estDivision = operation == 4


# Si l'opération choisie est l'addition, affiche le résultat de l'addition
if estAddition:
    print(f"Resultat: {round(nbr1+nbr2,1)}")
# Si l'opération choisie est la soustraction, affiche le résultat de la soustraction
elif estSoustraction:
    print(f"Resultat: {round(nbr1-nbr2,1)}")
# Si l'opération choisie est la multiplication, affiche le résultat de la multiplication
elif estMultiplication:
    print(f"Resultat: {round(nbr1*nbr2,1)}")
# Si l'opération choisie est la division
elif estDivision:
    # Vérifie si la division par zéro est tentée
    conditionDivisionZero = nbr2 == 0
    # Si la division par zéro est tentée, affiche une erreur
    if conditionDivisionZero:
        print("Erreur: Division par zero.")
    # Sinon, affiche le résultat de la division
    else:
        print(f"Resultat: {nbr1/nbr2}")
# Si l'opération choisie n'est pas valide, affiche un message d'erreur
else:
    print("L'operation n'est pas valide.")