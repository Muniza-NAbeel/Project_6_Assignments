class Counter:
    count = 0                                               # Class variable jo tamaam objects ke count ko track karega
    
    def __init__(self):                                     # Constructor jo object create hone par call hota hai
        Counter.count += 1                                  # Har naye object create krnay pr count ko me 1 ka increment ho ga
    
    @classmethod
    def display_count(cls):                                 # Class method jo count ko display karega
        print(f"{cls.count} Number Of Objects Created.")    # Count ki value print karega

obj1 = Counter()                                            # Pehla object banaya hai
obj2 = Counter()                                            # Doosra object banaya hai
obj3 = Counter()                                            # Teesra object banaya hai
obj4 = Counter()
Counter.display_count()                                     # Count ko display karne ke liye class method ko call kiya hai