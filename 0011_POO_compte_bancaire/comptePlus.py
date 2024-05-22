class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        """
        Initialise un nouveau compte bancaire avec un titulaire et un solde initial.

        Parameters:
        account_holder (str): Le nom du titulaire du compte.
        initial_balance (float): Le solde initial du compte.
        """
        if initial_balance < 0:
            raise ValueError("Le solde initial ne peut pas être négatif.")
        self.__account_holder = account_holder
        self.__account_balance = initial_balance

    def deposit(self, amount: float):
        """
        Dépose un montant sur le compte bancaire.

        Parameters:
        amount (float): Le montant à déposer.
        """
        if amount > 0:
            self.__account_balance += amount
            print(f"{amount:.2f}€ déposés sur le compte de {self.__account_holder}")
        else:
            print("Le montant déposé est invalide. Veuillez déposer un montant positif.")

    def withdraw(self, amount: float):
        """
        Retire un montant du compte bancaire.

        Parameters:
        amount (float): Le montant à retirer.
        """
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
        """
        Affiche le solde du compte bancaire et le nom du titulaire.
        """
        print(f"Compte de {self.__account_holder}, Solde: {self.__account_balance:.2f}€")

    @property
    def account_holder(self):
        """
        Retourne le nom du titulaire du compte.
        """
        return self.__account_holder

    @property
    def account_balance(self):
        """
        Retourne le solde actuel du compte.
        """
        return self.__account_balance

# Test de la classe BankAccount
try:
    account = BankAccount("Patrick", 100)
    account.deposit(50)
    account.withdraw(200)
    account.display_balance()
except ValueError as e:
    print(e)

# Test de validation des entrées
try:
    invalid_account = BankAccount("Patrick", -100)  # Test avec un solde initial invalide
except ValueError as e:
    print(e)  # Affiche l'erreur

try:
    account.deposit(-50)  # Test avec un montant de dépôt invalide
except ValueError as e:
    print(e)  # Affiche l'erreur

try:
    account.withdraw(-30)  # Test avec un montant de retrait invalide
except ValueError as e:
    print(e)  # Affiche l'erreur
