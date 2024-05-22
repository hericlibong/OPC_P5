def square(number):
    """
    Calcule le carré d'un nombre donné et gère les erreurs si le paramètre n'est pas un nombre.

    Parameters:
    number (int or float): Le nombre dont on veut calculer le carré.

    Returns:
    int or float: Le carré du nombre si le paramètre est un nombre.
    None: Si le paramètre n'est pas un nombre valide, retourne None et affiche un message d'erreur.

    Examples:
    >>> square(5)
    25
    >>> square(3.2)
    10.24
    >>> square("hello")
    Le paramètre doit être un nombre !
    None
    """
    if isinstance(number, (int, float)):
        return number ** 2
    else:
        print("Le paramètre doit être un nombre !")
        return None

# Exemple d'utilisation de la fonction avec un nombre valide (int)
result = square(5)
print("Le cas d'un nombre entier :", result)  # 25

# Exemple d'utilisation de la fonction avec un nombre valide (float)
result = square(3.2)
print("Le cas d'un nombre décimal :", round(result, 2))  # 10.24

# Exemple d'utilisation de la fonction avec un nombre invalide (string)
result = square("hello")
print("Type invalide :", result)  # Le paramètre doit être un nombre ! None

# Tests supplémentaires
# Exemple d'utilisation de la fonction avec None
result = square(None)
print("None comme paramètre :", result)  # Le paramètre doit être un nombre ! None

# Exemple d'utilisation de la fonction avec une liste
result = square([2])
print("Liste comme paramètre :", result)  # Le paramètre doit être un nombre ! None
