class Laptop:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Laptop Brand is: {self.brand}")
        print(f"Laptop Model is: {self.model}")
        print(f"Year is: {self.year}")

l1 = Laptop("Dell", "Inspiron 15", 2021)

l1.display_details()
