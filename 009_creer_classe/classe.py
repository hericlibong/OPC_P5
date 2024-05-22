# Exercice 9

""" 
Instructions
Vous devez créer une classe appelée Rectangle pour représenter un rectangle avec une largeur et une longueur. 
La classe doit avoir les attributs width et length initialisés dans la méthode __init__. La classe doit également 
avoir des méthodes pour calculer l'aire du rectangle calculate_area et le périmètre du rectangle calculate_perimeter.

Aire = largeur * longueur
Périmètre = 2 * (largeur + longueur)
"""


class Rectangle:
    def __init__(self, width, length):
        """
        Initialise un nouveau rectangle avec une largeur et une longueur.

        Parameters:
        width (float): La largeur du rectangle.
        length (float): La longueur du rectangle.
        """
        if width <= 0 or length <= 0:
            raise ValueError("La largeur et la longueur doivent être des valeurs positives.")
        self.width = width
        self.length = length

    def calculate_area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
        float: L'aire du rectangle.
        """
        return self.width * self.length

    def calculate_perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
        float: Le périmètre du rectangle.
        """
        return 2 * (self.width + self.length)

    def __str__(self):
        """
        Fournit une représentation textuelle de l'objet Rectangle.

        Returns:
        str: La représentation textuelle de l'objet Rectangle.
        """
        return f"Rectangle(width={self.width}, length={self.length})"

# Test de la classe Rectangle
try:
    rectangle = Rectangle(5, 3)  # 5:width & 3:length
    print(rectangle)  # Utilise la méthode __str__
    print("Largeur:", rectangle.width)
    print("Longueur:", rectangle.length)
    print("Aire:", rectangle.calculate_area())
    print("Périmètre:", rectangle.calculate_perimeter())
except ValueError as e:
    print(e)

# Test de validation des entrées
try:
    invalid_rectangle = Rectangle(-5, 3)  # Test avec des valeurs invalides
except ValueError as e:
    print(e)  # Affiche l'erreur
