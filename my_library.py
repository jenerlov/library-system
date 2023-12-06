import datetime
class LibrarySystem:
    
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book_to_library(self, title, author):
        book = {'title': title, 'author': author, 'is_borrowed': False, 'borrowed_date': None, 'return_date': None}
        self.books.append(book)   
        print(f'{title} by {author} has been added to the {self.name}')
    

    def remove_book_from_library(self, title):
        updated_books = []
        book_removed = False
        
        for book in self.books:
            if book['title'] == title:
                print(f'{title}  has been deleted from {self.name}')
                book_removed = True
            else:
                updated_books.append(book)
        
        if not book_removed:
            print(f'{title} not found in {self.name}')
        
        self.books = updated_books
        
    def borrow_book(self, title):
        for book in self.books:
            if book['title'] == title:
                if not book['is_borrowed']:
                    book['is_borrowed'] = False
                    book['borrowed_date'] = datetime.datetime.now()
                    print(f'{title} has been borrowed')
                    return
                else: 
                    print(f'{title} is already borrowed')
                    return
        print(f'{title} not found in {self.name}')
                    
    
    def return_book(self, title):
        current_date = datetime.datetime.now()
        for book in self.books:
                if book['title'] == title:
                    if book['is_borrowed']:
                        borrowed_date = book['borrowed_date']
                        book['is_borrowed'] = False
                        book['return_date'] = current_date
                        overdue_days = self.calculate_overdue_days(borrowed_date, return_date=current_date)
                    
                        print(f'{title} has been returned')
                        if overdue_days > 0:
                            print(f'The book is overdue by {overdue_days} days')
                        return
                    else:
                        print(f'{title} is not currently borrowed')
                        return
        print(f'{title} not found in {self.name}')            
            
    def calculate_overdue_days(self, borrowed_date, return_date):
        due_date = borrowed_date + datetime.timedelta(days=14)
        overdue_days = max(0, (return_date - due_date).days)
        return overdue_days

        
    def book_is_not_available(self, title):
        for book in self.books:
                if book ['title'] == title and book['is_borrowed']:
                    print(f'{title} is currently not available')
                    return
    
    #Metod för om boken FINNS
    def book_is_available(self, title):
        for book in self.books:
            if book['title'] == title and not book['is_borrowed']:
                print(f'{title} is available at {self.name}')
                return
        
    
    def print_available_books(self):
        available_books = [book['title'] for book in self.books if not book['is_borrowed']]
        if available_books:
            print(f'These are all available books: {available_books}')
        else:
            print(f'No available books in the library')
            


library = LibrarySystem('Josefins bibbla')
library.add_book_to_library('Harry Potter', 'JK Rowling')
library.add_book_to_library('Röda Rummet', 'August Strindberg')
library.print_available_books()

library.remove_book_from_library('Röda Rummet')
library.print_available_books()


library.return_book('Harry Potter')
library.print_available_books()
