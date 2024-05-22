# Exercice 7

""" 
Instructions
Écrivez une fonction appelée square qui prend en paramètre un nombre et renvoie le carré de ce nombre. 
Cependant, la fonction doit gérer les erreurs potentielles, 
notamment le cas où le paramètre n'est pas un nombre (int ou float).

Si le paramètre n'est pas un nombre, la fonction doit afficher un message 
d'erreur "Le paramètre doit être un nombre !" et renvoyer None.
"""


def square(number):
  """
  Calcule le carré d'un nombre donné et gére les erreurs si le paramètre n'est pas un nombre.

  Parameters:
  number (int or float): Le nombre dont on veut calculer le carré.

  Returns:
  int or float: Le carré du nombre si le paramètre est un nombre.
  None: Si une erreur survient, retourne None et affiche un message d'erreur.
  """
  try:
      result = number ** 2
      return result
  except TypeError:
      print("Le paramètre doit être un nombre !")
      return None

# Exemple d'utilisation de la fonction avec un nombre valide (int)
result = square(5)
print("Le cas d'un nombre entier :", result, 2)
# Exemple d'utilisation de la fonction avec un nombre valide (float)
result = square(3.2)
print("Le cas d'un nombre décimal :", round(result, 2))
# Exemple d'utilisation de la fonction avec un nombre invalide (string)
result = square("hello")
print("Type invalide:", result)  
