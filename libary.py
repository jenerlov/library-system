
class LibarySystem:
    
    def __init__(self, name):
        self.name = name
        self.books = []
    
    # dictionary för att varje bok ska ha en tite och författare 
    def add_book_to_libary(self, title, author):
        book = {'title': title, 'author': author, 'is_borrowed': False}
        self.books.append(book)   
        # print(f'{title} by {author} has been added to the {name}')
    
    def delete_book_from_libary(self):
        # print(f'{title} by {authos} has been deleted from {name}')
        pass
    
    def book_is_not_available(self):
        # print(f'{self.book} is currently not available')
        pass
    
    def book_is_available(self):
        # print(f'{self.book} is available at {self.name}')
        pass
    
    def print_available_books(self):
        for book in self.books:
            
            print(f'These are all available books: {book}')
        pass
    
    available_books = ['book1', 'book2', 'book3']
    print_available_books(available_books)
    
    

    