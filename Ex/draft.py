#exercice without class for comprehension

book = ['MacBeth' , 'frankstein' , 'antigone', 'la boite',  'the Canterville Ghost']

book_wanted = input("enter your title: ")
book_author = input("enter the author: ")

#displaying the book's details:
print(f"{book_wanted} by {book_author}")

#checking out, availability of the book:
if book_wanted in book:
    print(f"the book {book_wanted} is available")
else:
    print(f"the book {book_wanted} is checked out")

#returning the book:
if book_wanted not in book:
    print(f"The book {book_wanted} is not returned")
else:
    print(f"The book {book_wanted} is returned")


