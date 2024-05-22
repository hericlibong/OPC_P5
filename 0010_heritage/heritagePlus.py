class Person:
    def __init__(self, name, age):
        """
        Initialise une nouvelle personne avec un nom et un âge.

        Parameters:
        name (str): Le nom de la personne.
        age (int): L'âge de la personne.
        """
        if not isinstance(name, str):
            raise ValueError("Le nom doit être une chaîne de caractères.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("L'âge doit être un entier positif.")
        self.name = name
        self.age = age

    def display_details(self):
        """
        Affiche les détails de la personne.

        Returns:
        str: Les détails de la personne.
        """
        return f"Name: {self.name}, Age: {self.age}"

    def __str__(self):
        """
        Fournit une représentation textuelle de l'objet Person.

        Returns:
        str: La représentation textuelle de l'objet Person.
        """
        return self.display_details()


class Employee(Person):
    def __init__(self, name, age, salary):
        """
        Initialise un nouvel employé avec un nom, un âge et un salaire.

        Parameters:
        name (str): Le nom de l'employé.
        age (int): L'âge de l'employé.
        salary (float): Le salaire de l'employé.
        """
        super().__init__(name, age)
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Le salaire doit être un nombre positif.")
        self.salary = salary

    def display_details(self):
        """
        Affiche les détails de l'employé.

        Returns:
        str: Les détails de l'employé.
        """
        details = super().display_details()
        return f"{details}, Salary: {self.salary}"

    def __str__(self):
        """
        Fournit une représentation textuelle de l'objet Employee.

        Returns:
        str: La représentation textuelle de l'objet Employee.
        """
        return self.display_details()


# Test de la classe Employee
try:
    employee = Employee("Pierre", 30, 50000)
    print(employee)  # Utilise la méthode __str__
except ValueError as e:
    print(e)

# Test de validation des entrées
try:
    invalid_employee = Employee("Pierre", -1, 50000)  # Test avec un âge invalide
except ValueError as e:
    print(e)  # Affiche l'erreur

try:
    invalid_employee = Employee("Pierre", 30, -50000)  # Test avec un salaire invalide
except ValueError as e:
    print(e)  # Affiche l'erreur
