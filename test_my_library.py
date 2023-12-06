import unittest
from my_library import LibrarySystem

class TestLibrarySystem(unittest.TestCase):
    
    def test_add_new_book_to_library(self):
        library = LibrarySystem('Test Library')
        library.add_book_to_library('Tomtebobarnen', 'Elsa Beskow')
        self.assertFalse(library.books[0]['is_borrowed'])
    
    def test_remove_book_from_library(self):
        library = LibrarySystem('Test Library')  
        library.add_book_to_library('Harry Potter', 'JK Rowling')
        library.remove_book_from_library('Harry Potter')
        self.assertFalse('Harry Potter' in [book['title'] for book in library.books])
        
    def test_borrow_book(self):
        library = LibrarySystem('Test Library')
        library.add_book_to_library('Tomtebobarnen', 'Elsa Beskow')
        library.borrow_book('Tomtebobarnen')
        self.assertFalse(library.books[0]['is_borrowed'])

def test_return_book(self):
    library = LibrarySystem('Test Library')
    library.add_book_to_library('Tomtebobarnen', 'Elsa Beskow')
    library.borrow_book('Tomtebobarnen')
    library.return_book('Tomtebobarnen')
    self.assertFalse(library.books[0]['is_borrowed'])  # Should be False, not True
    self.assertIsNotNone(library.books[0]['return_date'])

        
    def test_book_is_available(self):
        library = LibrarySystem('Test Library')
        library.add_book_to_library('Tomtebobarnen', 'Elsa Beskow')
        library.borrow_book('Tomtebobarnen')
        result = library.book_is_not_available('Tomtebobarnen')
        self.assertIsNone(result)
    
    def test_book_is_not_available(self):
        library = LibrarySystem('Test Library')
        library.add_book_to_library('Tomtebobarnen', 'Elsa Beskow')
        result = library.book_is_available('Tomtebobarnen')
        self.assertIsNone(result)
        
if __name__ == '__main__':
    unittest.main()