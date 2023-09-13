# Demander à l'utilisateur de choisir le type de conversion
conv = int(input("Type de conversion :\n1: Kilometres vers Miles (K vers M)\n2: Miles vers Kilometres (M vers K)\nEntrez votre choix (1 ou 2): "))

# Demande de la distance à l'utilisateur
dist = float(input("Entrez la distance a convertir: "))

# Vérifie si l'utilisateur a choisi la conversion de kilomètres en miles
choixKmEnMiles = conv == 1

# Conversion de la distance en fonction du choix de l'utilisateur
if choixKmEnMiles:
    # Conversion de kilomètres en miles
    ml = dist*0.621371
    # Affichage du résultat de la conversion
    print(f"{dist} kilometres equivalent a {round(ml,2)} miles.")

else:
    # Conversion de miles en kilomètres   
    km = dist/0.621371
    # Affichage du résultat de la conversion
    print(f"{dist} miles equivalent a {round(km,2)} kilometres.")