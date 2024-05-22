def log_decorator(func):
    """
    Décorateur qui affiche et enregistre les détails des arguments et du résultat de la fonction décorée.

    Parameters:
    func (function): La fonction à décorer.

    Returns:
    function: La fonction enveloppée avec l'enregistrement des détails avant et après l'appel.
    """
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec les arguments {args} et {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} a retourné {result}")
        return result
    return wrapper

@log_decorator
def calculate_area(shape, *dimensions):
    """
    Calcule l'aire de différentes formes géométriques.

    Parameters:
    shape (str): Le type de forme ('circle', 'rectangle', 'triangle').
    *dimensions: Les dimensions nécessaires pour calculer l'aire.

    Returns:
    float: L'aire de la forme.
    """
    if shape == 'circle':
        radius = dimensions[0]
        area = 3.14159 * radius ** 2
    elif shape == 'rectangle':
        length, width = dimensions
        area = length * width
    elif shape == 'triangle':
        base, height = dimensions
        area = 0.5 * base * height
    else:
        raise ValueError("Forme non supportée")
    return area

# Appels de la fonction avec différentes formes
print("Calcul de l'aire d'un cercle :")
area_circle = calculate_area('circle', 5)

print("\nCalcul de l'aire d'un rectangle :")
area_rectangle = calculate_area('rectangle', 10, 20)

print("\nCalcul de l'aire d'un triangle :")
area_triangle = calculate_area('triangle', 10, 5)
