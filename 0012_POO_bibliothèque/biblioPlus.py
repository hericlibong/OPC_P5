class Book:
    def __init__(self, title, author, year):
        """
        Initialise un nouveau livre avec un titre, un auteur et une année de publication.

        Parameters:
        title (str): Le titre du livre.
        author (str): L'auteur du livre.
        year (int): L'année de publication du livre.
        """
        if not title or not isinstance(title, str):
            raise ValueError("Le titre doit être une chaîne de caractères non vide.")
        if not author or not isinstance(author, str):
            raise ValueError("L'auteur doit être une chaîne de caractères non vide.")
        if not isinstance(year, int) or year < 0:
            raise ValueError("L'année doit être un entier positif.")
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}"


class Library:
    def __init__(self):
        """
        Initialise une nouvelle bibliothèque avec des listes pour les livres disponibles et empruntés.
        """
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        """
        Ajoute un livre à la liste des livres de la bibliothèque.

        Parameters:
        book (Book): Le livre à ajouter.
        """
        if book in self.books:
            print(f"Le livre '{book.title}' est déjà dans la bibliothèque.")
        else:
            self.books.append(book)

    def remove_book(self, book_title):
        """
        Retire un livre de la liste des livres disponibles.

        Parameters:
        book_title (str): Le titre du livre à retirer.

        Returns:
        bool: True si le livre a été retiré, False sinon.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return True
        print(f"Le livre '{book_title}' n'a pas été trouvé dans la bibliothèque.")
        return False

    def borrow_book(self, book_title):
        """
        Emprunte un livre et l'ajoute à la liste des livres empruntés.

        Parameters:
        book_title (str): Le titre du livre à emprunter.

        Returns:
        bool: True si le livre a été emprunté, False sinon.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                print(f"Le livre '{book.title}' a été emprunté.")
                return True
        print(f"Le livre '{book_title}' n'est pas disponible.")
        return False

    def return_book(self, book_title):
        """
        Retourne un livre, le retire de la liste des livres empruntés et le rajoute à la liste des livres disponibles.

        Parameters:
        book_title (str): Le titre du livre à retourner.

        Returns:
        bool: True si le livre a été retourné, False sinon.
        """
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                print(f"Le livre '{book.title}' est de nouveau disponible.")
                return True
        print(f"Le livre '{book_title}' n'a pas été trouvé parmi les livres empruntés.")
        return False

    def available_books(self):
        """
        Renvoie la liste des titres des livres disponibles.

        Returns:
        list: Les titres des livres disponibles.
        """
        return [book.title for book in self.books]

    def borrowed_books(self):
        """
        Renvoie la liste des titres des livres empruntés.

        Returns:
        list: Les titres des livres empruntés.
        """
        return [book.title for book in self.borrowed_books]


# Utilisation de la classe Library
library = Library()
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
book3 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Livres disponibles:", library.available_books())

library.borrow_book("1984")
print("Livres empruntés:", library.borrowed_books())

library.return_book("1984")
print("Livres disponibles après retour d'emprunt:", library.available_books())
