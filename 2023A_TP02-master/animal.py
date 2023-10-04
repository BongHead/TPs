def creer_animal(age=0, jrs_gestation=0, energie=0, disponible=True):
   return {"age":age,"jrs_gestation":jrs_gestation,"energie":energie,"disponible":disponible}


def obtenir_age(animal):
    # TODO: Retourner la valeur de l'âge de l'animal donné (Int)
    return animal.get("age")


def obtenir_jours_gestation(animal):
    # TODO: Retourner le nombre de jours de gestation de l'animal donné (Int)
    return animal.get("jrs_gestation")


def obtenir_energie(animal):
    # TODO: Retourner la quantité d'énergie de l'animal donné (Int)
    return animal.get("energie")


def obtenir_disponibilite(animal):
    # TODO: Retourner l'état de disponibilité de l'animal (Booléen)
    return animal.get("disponible")


def incrementer_age(animal, puberte):
    # TODO: Incrémenter l'âge de l'animal de 1
    # TODO: Si l'animal est plus âgé que l'âge de la puberté, incrémenter son nombre de jours de gestation de 1
    animal["age"] += 1
    if animal.get("age") > puberte:
        animal["jrs_gestation"] += 1


def definir_jours_gestation(animal, jrs_gest):
    # TODO: Mettre à jour le nombre de jours de gestation de l'animal avec la valeur jrs_gest donnée (Int)
    animal["jrs_gestation"] = jrs_gest


def ajouter_energie(animal, valeur):
    # TODO: Ajouter la quantité d'énergie donnée (valeur) à l'énergie actuelle de l'animal (Int)
    animal["energie"] += valeur


def definir_disponibilite(animal, disponibilite):
    # TODO: Mettre à jour l'état de disponibilité de l'animal en utilisant le paramètre permis (Booléen)
    animal["disponible"] = disponibilite