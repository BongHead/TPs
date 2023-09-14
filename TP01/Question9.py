from math import sqrt
# Demander à l'utilisateur d'entrer les coefficients de l'équation quadratique
a = int(input("Veuillez entrer la valeur de a (coefficient de x^2): "))
b = int(input("Veuillez entrer la valeur de b (coefficient de x): "))
c = int(input("Veuillez entrer la valeur de c (terme constant): "))
# Calculer le discriminant
delta = (b**2)-4*a*c

# Vérifier si le discriminant est négatif (aucune racine réelle)
naPasDeSolution = delta < 0

if naPasDeSolution:
    # Cette ligne de code sera exécutée si le projectile n'atteint jamais l'altitude désirée.
    print("Le projectile n'atteint jamais l'altitude desiree.")
else:
    # Vérifier si le discriminant est nul (une seule racine réelle)
    aUneSeuleSolution = delta == 0

    if aUneSeuleSolution:
        # Calculer l'instant unique où le projectile atteint l'altitude
        x = (-b)/(2*a)

        # Vérifier si l'instant est positif
        estInstantPositif = x >= 1
        if estInstantPositif:
            print("Le projectile atteint l'altitude a un seul moment precis.")
            print(f"Instant de l'impact: {x}")
            # Afficher l'instant
        else:
            # Afficher que le projectile n'atteint jamais l'altitude désirée.
            print("Le projectile n'atteint jamais l'altitude desiree.")

    else:
        # Calculer les deux instants où le projectile atteint l'altitude
        x1 = (-b+sqrt(delta))/(2*a)
        x2 = (-b-sqrt(delta))/(2*a)

        # Vérifier si les instants sont positifs
        estInstant1PositifInstant2Negatif = x1 > 0 and x2 < 0
        estInstant2PositifInstant1Negatif = x1 < 0 and x2 > 0
        estInstant1PositifInstant2Positif = x1 > 0 and x2 > 0
        
        if estInstant1PositifInstant2Negatif:
            print("Le projectile atteint l'altitude a un seul moment precis.")
            print(f"Instant de l'impact: {x1}")
            # Afficher l'instant positif

        elif estInstant2PositifInstant1Negatif:
            print("Le projectile atteint l'altitude a un seul moment precis.")
            print(f"Instant de l'impact: {x2}")
            # Afficher l'instant positif

        elif estInstant1PositifInstant2Positif:
            print("Le projectile atteint l'altitude à deux moments distincts.")
            print(f"Instants de l'impact: {x1}, {x2}")
            # Afficher les deux instants
            
        else:
            print("Le projectile n'atteint jamais l'altitude desiree.")
            # Afficher que le projectile n'atteint jamais l'altitude désirée.