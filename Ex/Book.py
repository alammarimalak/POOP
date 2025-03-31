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
    def __init__(self, title, author):
        self.title = title 
        self.author = author  
        self.available = True 

    #methods of a book
    def display_book(self):        
        print(self.title, self.author, self.available)
        
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

#2)create subclasses of book for different types of books
class Novel(Book):
    def __init__(self,title, author, genre):
        super().__init__(title,author)
        self.genre = genre

    def displayBook(self):
        return super().display_book() , self.genre
    
class Magazine(Book):
    def __init__(self,title,author,issue):
        super().__init__(title,author)
        self.issue = issue

    def displayBook(self):
        return super().display_book(), self.issue
    
#3)defining the member class:
class Member:
    def __init__(self,name):
        self.name = name
        self.checkouts = []

    def checkOut(self):
        isCheckedOut = True
        if isCheckedOut:
            self.checkouts.append(self.title)
            self.available = False
        else:
            print(self.title, "is not checked out !")

    def returnCheckedBook(self):
        isCheckedOut = False
        if isCheckedOut:
            self.checkouts.remove(self.title)
            self.available = True
        else:
            print("the book is being checked out")

    def displayCheckedBooks(self):
        for i in self.checkouts:
            print(i)