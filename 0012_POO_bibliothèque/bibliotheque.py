# Exercice 12

"""
Instructions
Vous devez créer un programme pour gérer une bibliothèque. Une bibliothèque peut contenir plusieurs livres. 
Chaque livre a un titre, un auteur et une année de publication. Les utilisateurs de la bibliothèque peuvent 
emprunter des livres, les rendre et afficher la liste des livres disponibles.

Créez une classe Book avec les attributs title, author, et year.
Créez une classe Library avec deux attributs books (livres disponibles dans la bibliothèque) et borrowed_books (livres empruntés)
Ajoutez les méthodes suivantes à la classe Library :
add_book(self, book): Ajoute un livre à la bibliothèque.
remove_book(self, book_title): Supprime un livre de la bibliothèque en utilisant le titre du livre comme argument.
borrow_book(self, book_title): Emprunte un livre de la bibliothèque en utilisant le titre du livre comme argument. 
Le livre doit être retiré de la liste des livres disponibles et ajouté dans la liste des livres empruntés.
return_book(self, book_title): Rend un livre emprunté à la bibliothèque en utilisant le titre du livre comme argument. 
Le livre doit être retiré de la liste des livres empruntés et ajouté dans la liste des livres disponibles.
available_books(self): Renvoie une liste contenant les titres des livres disponibles dans la bibliothèque.
borrowed_books(self): Renvoie une liste contenant les titres des livres empruntés de la bibliothèque.
"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    def add_book(self, book):
        """Ajoute un livre à la liste des livres de la bibliothèque."""
        self.books.append(book)

    def remove_book(self, book_title):
        """Retire un livre de la liste des livres disponibles."""
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return True
        return False  # Si le livre n'est pas trouvé

    def borrow_book(self, book_title):
        """Emprunte un livre et l'ajoute à la liste des livres empruntés."""
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrow_books.append(book)
                # print(f"Le livre {book.title} a été emprunté")
                return True
        return False

    def return_book(self, book_title):
        """Retourne un livre, le retire de la liste des livres empruntés et le rajoute à la liste des livres disponibles."""
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.books.append(book)
                # print(f"Livre {book.title} est de nouveau disponible.")
                return True
        return False

    def available_books(self):
        """Renvoie la liste des titres des livres disponibles."""
        return [book.title for book in self.books]

    def borrowed_books(self):
        """Renvoie la liste des titres des livres empruntés."""
        return [book.title for book in self.borrow_books]

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
