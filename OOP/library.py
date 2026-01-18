# 1. Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}."

# 2. Child Class (Inheritance)
class Member(Person):
    def __init__(self, name, age, member_id):
        # Using super() to reuse Person's initialization
        super().__init__(name, age)
        self.member_id = member_id

    # Method Overriding (Changing how introduce works for Member)
    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} My Member ID is {self.member_id}."
    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
class Library:
    # Class Variable: Shared by all Library branches
    library_name = "City Central Library"

    def __init__(self):
        # Composition: The Library *has* a list of books
        self.books = [] 
        # Composition: The Library *has* a list of members
        self.members = []

    def add_book(self, book_obj):
        # We are passing a Book OBJECT here, not just a string
        self.books.append(book_obj)
        print(f"Added {book_obj.title} to the library.")

    def register_member(self, member_obj):
        self.members.append(member_obj)
        print(f"Welcome, {member_obj.name}!")

    def show_collection(self):
        print(f"\n--- {Library.library_name} Collection ---")
        for book in self.books:
            print(book) 
    
    # 1. Create the Library
my_lib = Library()

# 2. Create Books (Instances)
b1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
b2 = Book("1984", "George Orwell")

# 3. Create a Member (Inheritance in action)
new_member = Member("Alice", 30, "M001")

# 4. Use the Library (Composition in action)
my_lib.add_book(b1)
my_lib.add_book(b2)
my_lib.register_member(new_member)

# 5. Show results
my_lib.show_collection()
print("\nMember Info:")
print(new_member.introduce())
