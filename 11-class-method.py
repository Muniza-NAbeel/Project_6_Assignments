class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self, title):    # Constructor jo book ka title set karega
        self.title = title
        Book.Increment_total_books()   # Class method ko call karega jab bhi ek naya book object create hoga


    @classmethod
    def increment_total_books(cls):    # Class method jo total books ko increment karega
        cls.total_books += 1

    @classmethod
    def display_count(cls):     # Class method jo total books ko display karega
        print(f"Total books: {cls.total_books}")

book1 = Book("Python")
book2 = Book("Generative AI")

Book.display_count()  