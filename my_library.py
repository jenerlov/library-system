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
        for book in self.books:
            if book['title'] == title:
                print(f'{title} has been deleted from {self.name}')
            else:
                updated_books.append(book)

        if len(updated_books) == len(self.books):
            print(f'{title} not found in {self.name}')

        self.books = updated_books
        
    def borrow_book(self, title):
        for book in self.books:
            if book['title'] == title:
                if not book['is_borrowed']:
                    book['is_borrowed'] = True
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

        
    
    #Metod för om boken FINNS i bibblo
    def book_is_available(self, title):
        if title in self.books:
            if not self.books[title]['is_borrowed']:
                print(f'Book {title} is available')
                return True
            else:
                print(f'{title} is not available')
                return False
        else:
            print(f'{title} does not exist in Josefins Bibbla')
            return False
            
    
    # def book_is_not_available(self, title):        
    #     for book in self.books:
    #             if not book ['title'] == title and book['is_borrowed']:
    #                 print(f'{title} is currently not available')
    #                 return
    #             else:
    #                 print(f'Book titled {title} does not exist')
        
    # Printa ut alla tillgängliga böcker som finns i bibblan
    def print_available_books(self):
        available_books = [book['title'] for book in self.books if not book['is_borrowed']]
        if available_books:
            print(f'These are all available books: {available_books}')
        else:
            print(f'No available books in the library')
            


# instanser
print('\n') # radbrytning
my_library = LibrarySystem('Josefins bibbla')
my_library.add_book_to_library('Harry Potter', 'JK Rowling')
my_library.add_book_to_library('Röda Rummet', 'August Strindberg')
my_library.add_book_to_library('Sagan Om Ringen', 'J.R.R Tolkien')

my_library.remove_book_from_library('Röda Rummet')
my_library.print_available_books()

my_library.return_book('Harry Potter')
my_library.print_available_books()
