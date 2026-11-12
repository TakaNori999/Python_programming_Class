class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def start_engine(self):
        print("Engine started!")
    def display_info(self):
        print(f"{self.model} = {self.year}")

car1 = Car("Toyota car", 2024)
car2 = Car("Honda car", 2011)
car3 = Car("Nissan car", 1980)

car1.start_engine()
car2.display_info()