import unittest
from booklover.booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        bl1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_to_add = "War of the Worlds"
        bl1.add_book(book_to_add, 4)
        
        self.assertIn(book_to_add, bl1.book_list.book_name.values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bl1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_to_add = "War of the Worlds"
        bl1.add_book(book_to_add, 4)
        bl1.add_book(book_to_add, 4)
        
        expected = 1
        
        self.assertEqual(bl1.book_list.shape[0], expected)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        bl1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_to_add = "War of the Worlds"
        bl1.add_book(book_to_add, 4)
        
        self.assertTrue(bl1.has_read(book_to_add))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bl1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_to_add = "War of the Worlds"
        bl1.add_book(book_to_add, 4)
        unread_book = "To Kill a Mockingbird"
        
        self.assertFalse(bl1.has_read(unread_book))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        bl1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_to_add1 = "War of the Worlds"
        book_to_add2 = "To Kill a Mockingbird"
        book_to_add3 = "The Last Lecture"
        
        bl1.add_book(book_to_add1, 4)
        bl1.add_book(book_to_add2, 7)
        bl1.add_book(book_to_add3, 10)
        
        expected = 3
        
        self.assertEqual(bl1.num_books_read(), expected)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        bl1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        book_to_add1 = "War of the Worlds"
        book_to_add2 = "To Kill a Mockingbird"
        book_to_add3 = "The Last Lecture"
        book_to_add4 = "The Things We Carried"
        
        bl1.add_book(book_to_add1, 4)
        bl1.add_book(book_to_add2, 7)
        bl1.add_book(book_to_add3, 10)
        bl1.add_book(book_to_add4, 2)
        
        expected_fav_books = 3
        
        self.assertGreater(min(bl1.fav_books().book_rating), 3)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=3)