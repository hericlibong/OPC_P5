# exercice 10

""" 
Vous devez créer deux classes : Person et Employee. 
La classe Person doit avoir les attributs name et age, et une méthode display_details() qui affiche le nom et l'âge de la personne.

La classe Employee doit hériter de la classe Person et avoir un attribut supplémentaire salary 
et une méthode display_details() qui affiche les détails de l'employé, y compris son salaire. 
Pensez à appeler les méthodes de la classe mère pour ne pas dupliquer le code.
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display_details(self):
    return f"Name: {self.name}, Age: {self.age}"


class Employee(Person):
  def __init__(self, name, age, salary):
    super().__init__(name, age)
    self.salary = salary

  def display_details(self):
    details = super().display_details()
    return f"{details}, Salary: {self.salary}"


# Test de la classe Employee
employee = Employee("Pierre", 30, 50000)
print(employee.display_details())