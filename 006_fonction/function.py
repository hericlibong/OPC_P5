# Fonction calculate_average
def calculate_average(numbers):
  """
  Calcule la moyenne d'une liste de nombres.

  Parameters:
  numbers (list of float or int): La liste des nombres   dont on souhaite calculer la moyenne.

  Returns:
  float: La moyenne des nombres dans la liste
  """
  total = sum(numbers)
  average = total / len(numbers)
  return average

# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
     