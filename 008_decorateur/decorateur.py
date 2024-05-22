# exercice 8

""" 

Vous devez écrire un décorateur appelé log_decorator qui 
enroule une fonction donnée et affiche un message avant et après l'exécution de la fonction.

Le décorateur doit fonctionner avec des fonctions qui ne prennent pas d'arguments. 
Vous pouvez supposer que les fonctions sur lesquelles le décorateur sera appliqué ne prendront pas d'arguments.
"""

def log_decorator(func):
    """
    Décorateur qui affiche un message avant et après l'exécution de la fonction décorée.

    Parameters:
    func (function): La fonction à décorer.

    Returns:
    function: La fonction enveloppée avec le message avant et après l'appel.
    """
    def wrapper():
        print("Le message avant l'appel de la fonction")
        func()
        print("Le message après l'appel de la fonction")
    return wrapper

@log_decorator
def function_test():
    """
    Fonction de test qui affiche un message. 
    Cette fonction ne prend pas d'arguments.
    """
    print("Cette fonction ne prend pas d'arguments.")

# Appel de la fonction test
function_test()
