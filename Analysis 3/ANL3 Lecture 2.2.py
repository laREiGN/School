### COMPOSITION / AGGREGATION
#   Part 3
#

print("PART 3")

# Let's make a simple class to hold and display book information
class Book:
    def __init__(self, title, author, publishing_year):
        self.title = title
        self.author = author
        self.year = publishing_year
        
    def display(self):
        print("TITLE: %s, by %s (%d)" % (self.title, self.author, self.year))

# ... and class shelf that will just store books
class Shelf:
    def __init__(self):
        self.books = []
        
    def add(self, book):
        self.books.append(book)
        
    def show(self):
        print("\nThis shelf contains:")
        for b in self.books:
            b.display()
        
# Create 3 books
book1 = Book("Intro. to Python", "Jos", 2015)
book2 = Book("Hobbit", "Tolkien", 1937)
book3 = Book("Pride and Prejudice", "Jane Austen", 1813)

# To test that everything works, we will call display for all
book1.display()
book2.display()
book3.display()

# Next we create our shelf object and add 2 books to it
myshelf = Shelf()
myshelf.add(book1)
myshelf.add(book2)

# If everything is implemented correctly,
# ... calling show method will display all books
myshelf.show()


print("\n\nEOF part 3")
print("-"*20)