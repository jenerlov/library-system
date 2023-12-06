
class LibarySystem:
    
    def __init__(self, name):
        self.name = name
        self.books = []
    
    # dictionary för att varje bok ska ha en tite och författare 
    # eftersom man kan ta bort ett specifikt värde med hjälp av key?
    
    def add_book_to_libary(self, title, author):
        book = {'title': title, 'author': author, 'is_borrowed': False}
        self.books.append(book)   
        # print(f'{title} by {author} has been added to the {name}')
    
    # Använder title för att det är key som kan ta bort boken från listan
    def delete_book_from_libary(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                print(f'{title}  has been deleted from {self.name}')
                return
        
    #Metod för att kontrollera om en bok INTE finns på bibblan
    def book_is_not_available(self, title):
        for book in self.books:
                if book ['title'] == title and book['is_borrowed']:
                    print(f'{title} is currently not available')
                    return
    
    #Metod för om boken FINNS
    def book_is_available(self, title):
        for book in self.books:
            if book['title'] == title and not book['is_borrowed']:
                print(f'{self.books} is available at {self.name}')
                return
        
    
    def print_available_books(self):
        available_books = [book['title'] for book in self.books if not book['is_borrowed']]
        if available_books:
            print(f'These are all available books: {available_books}')
        else:
            print(f'No available books in the libary')
            


libary = LibarySystem('Josefins bibbla')
libary.add_book_to_libary('Harry Potter', 'JK Rowling')
libary.add_book_to_libary('Harry Potter 2', 'JK Rowling')
libary.print_available_books()
libary.book_is_available('Harry Potter 2')
libary.book_is_not_available('Harry Potter')
libary.book_is_available('Harry Potter')
libary.print_available_books()










    

    