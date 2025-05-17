class MathUtils:
    @staticmethod      # Static method jo do numbers ka sum return karta hai
    def add(a, b):
        return a + b
    
# Static method ko class ke Instance ke baghair direct call karein gaye
result = MathUtils.add(5, 3)
print(f"Sum of 5 and 3 is : {result}")