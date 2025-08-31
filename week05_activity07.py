class LibraryItem:
    # This class included attributes of title and author.
    def __init__(self, title, author):
        self.title = title  
        self.author = author

    # This method to show details of one item.
    def show_item_details(self):
        print(f'Title: {self.title}, author: {self.author}')

class Book(LibraryItem):
    # This class is encapsulated from LibraryItem.
    def __init__(self, title, author):
        super().__init__(title, author)

    # This method is encapsulated from LibraryItem.
    def show_item_details(self):
        super().show_item_details()

class Magazine(LibraryItem):
    # This class is encapsulate from LibraryItem, and have a new attribute of issue frequency
    def __init__(self, title, author, issue_frequency):
        super().__init__(title, author)
        self.issue_frequency = issue_frequency

    # This for showing magazine issue frequency.
    def issue(self):
        print(f'Issue frequency is: {self.issue_frequency}')   

class Library:
    # Manages all items in the library.
    def __init__(self):
        self.items = []

    # This method for list all items.
    def list_all(self):
        for item in self.items:
            item.show_item_details()

    # This method for add one item to library.
    def add_lib_item(self, item):
        self.items.append(item)
        print(f"'{item.title}' has been added.")

    # This method for remove one item by title.
    def remove_item(self, title):
    # Iterate each item
        for item in self.items:
            if item.title == title:
                self.items.remove(item)
                break

# Create a library instance
my_library = Library()

# Create some book and magazine instances
book1 = Book("Example Book 1", "Jothep")
book2 = Book("Another Book", "JSK")
magazine1 = Magazine("National Journal", "Bob", "Monthly")

# Add items to the library
my_library.add_lib_item(book1)
my_library.add_lib_item(book2)
my_library.add_lib_item(magazine1)

# List all items
my_library.list_all()

# Remove an item and list them again
my_library.remove_item("Another Book")
my_library.list_all()
