# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # Called when you print the object
    def __str__(self):
        return f"{self.title} by {self.author}"

    # Called when using ==
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # Called when using <
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # Called when using +
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    # Called when using 'in'
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    # Called when using []
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"{key} is not a valid key"

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)                   # Uses __str__: prints "The Hobbit by J.R.R Tolkien"
print(book1 == book2)          # Uses __eq__: compares title and author
print(book3 < book2)           # Uses __lt__: compares page numbers
print(book1 + book3)           # Uses __add__: adds page numbers and returns string
print("Lion" in book3)         # Uses __contains__: checks if "Lion" in title or author
print(book3["author"])         # Uses __getitem__: returns the author
print(book2["num_pages"])      # Uses __getitem__: returns number of pages