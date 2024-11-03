'''1. Define the Book Class:
    Properties:
▪ title: The title of the book.
▪ author: The author of the book.
▪ available: An indicator of availability.
    Methods:
▪ A method to display the book's details.
▪ A method to check out the book, changing its availability status.
▪ A method to return the book.'''

class Book:
    #properties of a book 
    def __init__(self, title, author, available):
        self.title = title 
        self.author = author  
        self.available = True 

    #methods of a book
    def display_book(self):
        
        if self.available:
            availability = "Available"
            return "the book you chose is available"
        else:
            availability = "Checked out"
            return "you checked out the chosen book"
        
    def checkout_book(self):
        
        if self.available:
            availability = False
            return 'your book ', self.title ,'is checked out!'
        else: 
            return 'your book' , self.title ,'is available!'
        
    def return_book(self):
        
        if not self.available:
            self.available = True
            return 'you returned the book!', self.title
        else:
            return "you haven't returned the book", self.title
'''
2.Create Subclasses of Book for Different Types of Books:
    Subclass Novel:
▪Adds a genre property to indicate the literary genre.
▪Overrides the display method to include the genre.
    Subclass Magazine:
▪Adds an issue property to indicate the magazine issue number.
▪Overrides the display method to include the issue number.
'''

#subclass inheriting from the class book
class type(Book):
    
    #property: genre and issue
    def __init__(self, genre, issue):
        self.genre = genre
        self.issue = issue

    #display methode in progress...