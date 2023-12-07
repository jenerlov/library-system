import unittest
import datetime
from my_library import LibrarySystem

class TestLibrarySystem(unittest.TestCase):
    
    def setUp(self):
        self.my_library = LibrarySystem('Testbibbla')
        self.my_library.add_book_to_library('Hattstugan', 'Elsa Beskow')
        
    def test_add_new_book_to_library(self):
        self.assertFalse(self.my_library.books[0]['is_borrowed'])
    
    def test_remove_book_from_library(self):
        self.my_library.add_book_to_library('Harry Potter', 'JK Rowling')
        self.my_library.remove_book_from_library('Harry Potter')
        self.assertFalse('Harry Potter' in [book['title'] for book in self.my_library.books])

    def test_borrow_book(self):
        self.my_library.borrow_book('Hattstugan')
        borrowed_date = self.my_library.books[0]['borrowed_date']
        self.assertIsNotNone(borrowed_date)
        
    def test_return_book(self):
        self.my_library.borrow_book('Hattstugan')
        self.my_library.return_book('Hattstugan')
        self.assertFalse(self.my_library.books[0]['is_borrowed'])
        overdue_days = self.my_library.calculate_overdue_days(
            self.my_library.books[0]['borrowed_date'], datetime.datetime.now()
        )
        self.assertEqual(overdue_days, 0)
        
    def test_is_available(self):
        self.my_library.borrow_book('Hattstugan')
        result = self.my_library.book_is_available('Hattstugan')
        self.assertFalse(result)
    
    def test_is_not_available(self):
        self.my_library.borrow_book('Hattstugan')
        result = self.my_library.book_is_not_available('Hattstugan')
        self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()