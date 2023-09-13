# Demandez à l'utilisateur d'entrer son poids en kg
poids = float(input("Entrez votre poids en kg: "))
# Demandez à l'utilisateur d'entrer sa taille en mètres
taille  = float(input("Entrez votre taille en m: "))

# Calculez l'Indice de Masse Corporelle (IMC) en utilisant la formule IMC = poids / (taille^2)
IMC = poids/(taille**2)

# Affichez l'IMC avec une précision de deux décimales
print(f"Votre IMC est: {round(IMC,2)}")

# Définissez des conditions pour déterminer la catégorie de poids en fonction de l'IMC
# Si l'IMC est inférieur à 18.5, la personne est en sous-poids
estSousPoids = IMC < 18.5

# Si l'IMC est inférieur à 24.9, la personne a un poids normal
estPoidsNormal = IMC >= 18.5 and IMC < 25

# Si l'IMC est inférieur à 30, la personne est en surpoids
estSurPoids =  IMC >= 25 and IMC < 30

# Utilisez des instructions conditionnelles pour afficher la catégorie de poids
if estSousPoids:
    print("Vous etes en sous-poids.")
elif estPoidsNormal:
    print("Votre poids est normal.")
elif estSurPoids:
    print("Vous etes en surpoids.")
else:
    print("Vous etes obese.")