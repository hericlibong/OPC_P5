# Exercice 11

""" 
Instructions
En utilisant les principes de la Programmation Orientée Objet (POO), 
créez une classe BankAccount qui représente un compte bancaire.

Un compte bancaire a les attributs suivants :

account_holder : le nom du titulaire du compte (string) ;
balance : le solde du compte (float).
La classe doit avoir les méthodes suivantes :

deposit(amount): pour déposer de l'argent sur le compte ;
withdraw(amount): pour retirer de l'argent du compte ;
display_balance(): pour afficher le solde et le nom du propriétaire du compte.
Remarques :

Assurez-vous d'effectuer les vérifications nécessaires dans la méthodewithdraw() 
pour éviter que le solde devienne négatif et dans la méthode deposit() de déposer un montant négatif.
"""

class BankAccount:
  def __init__(self, account_holder:str, initial_balance:float=0.0):
    self.__account_holder = account_holder
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(f"{amount:.2f}€ déposés sur le compte de {self.__account_holder}")
    else:
      print("Le montant déposé est invalide. Veuillez déposer un montant positif.")

  def withdraw(self, amount):
    print(f"{self.__account_holder} tente de retirer {amount:.2f}€")
    if amount > 0:
      if self.__account_balance >= amount:
        self.__account_balance -= amount
        print(f"{amount:.2f}€ retirés du compte de {self.__account_holder}")
      else:
        print("Montant disponible insuffisant. Retrait non effectué.")
    else:
      print("Montant de retrait invalide. Veuillez retirer un montant positif.")

  def display_balance(self):
    print(f"Compte {self.__account_holder} balance: {self.__account_balance:.2f}€")


account = BankAccount("Patrick", 100)
account.deposit(50)
account.withdraw(200)
account.display_balance()