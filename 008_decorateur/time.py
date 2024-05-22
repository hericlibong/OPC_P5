"""  
    Créez un décorateur appelé timeit qui prend une fonction en argument.
    Le décorateur doit enregistrer l'heure de début juste avant l'appel de la fonction et l'heure de fin juste après l'appel.
    Calculez la différence entre l'heure de fin et l'heure de début pour obtenir le temps d'exécution.
    Affichez le temps d'exécution en secondes.
    Appliquez le décorateur à une fonction de test qui effectue une tâche simple, comme 
    une boucle qui somme les nombres de 1 à 1 000 000.

"""

import time

def timeit(func):
    """
    Décorateur qui mesure et affiche le temps d'exécution de la fonction décorée.

    Parameters:
    func (function): La fonction à décorer.

    Returns:
    function: La fonction enveloppée avec la mesure du temps d'exécution.
    """
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Temps d'exécution de {func.__name__}: {execution_time: .4f} secondes")
        return result
    return wrapper




@timeit
def example_function():
    # Une simple boucle qui somme les nombres de 1 à 1 000 000
    total = 0
    for i in range(1, 1000001):
        total += i
    return total

# Appel de la fonction décorée
result = example_function()
print(f"Le résultat est {result}")