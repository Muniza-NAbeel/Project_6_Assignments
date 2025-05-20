class Book:
    total_books = 0  # Class variable to keep track of total books

    def __init__(self):    # Constructor jo book ka title set karega
        Book.increment_total_books()   # Class method ko call karega jab bhi ek naya book object create hoga

    @classmethod
    def increment_total_books(cls):    # Class method jo total books ko increment karega
        cls.total_books += 1

book1 = Book()
book2 = Book()

Book.display_count()  
