import unittest
import datetime
from my_library import LibrarySystem

class TestLibrarySystem(unittest.TestCase):
    
    def setUp(self):
        print('\n')
        self.my_library = LibrarySystem('Testbibbla')
        self.my_library.add_book_to_library('Hattstugan', 'Elsa Beskow')
        self.my_library.add_book_to_library('Sagan Om Ringen', 'J.R.R Tolkien')
        
    def test_add_new_book_to_library(self):
        print('\n')
        print('TEST ADD NEW BOOK:')
        self.assertFalse(self.my_library.books[0]['is_borrowed'])
    
    def test_remove_book_from_library(self):
        print('\n')
        print('TEST REMOVE BOOK:')
        self.my_library.add_book_to_library('Harry Potter', 'JK Rowling')
        self.my_library.remove_book_from_library('Harry Potter')
        self.assertFalse('Harry Potter' in [book['title'] for book in self.my_library.books])

    def test_is_available(self):
        print('\n')
        print('TEST BOOK IS AVAILABLE:')
        self.my_library.borrow_book('Sagan Om Ringen')
        result = self.my_library.book_is_available('Sagan Om Ringen')
        self.assertFalse(result)
        
    def test_borrow_book(self):
        print('\n')
        print('TEST BORROW BOOK:')
        self.my_library.borrow_book('Hattstugan')
        borrowed_date = self.my_library.books[0]['borrowed_date']
        self.assertIsNotNone(borrowed_date)
        
    def test_return_book(self):
        print('\n')
        print('TEST RETURN BOOK')
        self.my_library.borrow_book('Sagan Om Ringen')
        self.my_library.return_book('Sagan Om Ringen')
        self.assertFalse(self.my_library.books[0]['is_borrowed'])
        
    
    def test_is_not_available(self):
        print('\n')
        print('TEST BOOK IS NOT AVAILABLE:')
        self.my_library.borrow_book('Sagan Om Ringen')
        result = self.my_library.book_is_available('Sagan Om Ringen')
        self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()