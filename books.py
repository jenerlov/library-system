
# Skapa en BookData- klass för att få fram title och author på böckerna som läggs in i biblioteket
class BookData:
    def __init__(self, title, author ):
        self.title = title
        self.author = author
        self.is_borrowed = False
        
    def print_book(self):
        print (f'{self.title}: {self.author}')
            
    
    # Instanser av böcker, som hämtar information från BookData-klassen? För att få titel och författare
book1 = BookData(title='Harry Potter', author='J.K Rowling')
book2 = BookData(title='Hejhej', author='Namn')
book3 = BookData(title=' Hejhej2', author='Namn')