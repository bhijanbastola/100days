"""
    You are tasked with designing a system for a vehicle rental company. The company rents out various types of vehicles like Cars and Bikes, and each vehicle has some shared characteristics but also some distinct ones.

Requirements:

Each Vehicle has attributes such as:

vehicle_id: A unique identifier for the vehicle.
brand: The brand of the vehicle.
rental_price: Price per day to rent the vehicle.
Both Car and Bike are types of Vehicles.

A Car has an additional attribute: number_of_doors.
A Bike has an additional attribute: bike_type (e.g., mountain bike, racing bike).
You should provide methods to:

Calculate total rental cost: Given the number of rental days, calculate the total cost for any vehicle.
Display vehicle details: For both cars and bikes, display details including the unique attributes (e.g., number_of_doors for cars, bike_type for bikes).
Implement the following OOP concepts:

Abstraction: Provide a clean interface for calculating the total rental cost and displaying vehicle details, hiding the internal logic.
Inheritance: Both Car and Bike should inherit common functionality from the Vehicle class.
Polymorphism: Use method overriding so that the method for displaying vehicle details works differently for cars and bikes.

"""
class Vechile:
    def __init__(self,vechile_id,brand,rental_price,days):
        self.vechile_id=vechile_id
        self.brand=brand
        self.days=days
        self.rental_price=rental_price

    def calculate_total_rental_cost(self):
        return self.rental_price * self.days

    def display_vechiles_details(self):
        print(f"{self.vechile_id}-{self.brand}")

        


class Cars(Vechile):
    
    def __init__(self,vechile_id,brand,rental_price,days,number_of_doors):
        super().__init__(vechile_id,brand,rental_price,days)
        self.number_of_doors=number_of_doors

    def display_vechiles_details(self):
        print(f"Car ID: {self.vechile_id}\n Brand: {self.brand}\n Number of Doors: {self.number_of_doors}")


    
class Bikes(Vechile):

    def __init__(self,vechile_id,brand,rental_price,days,bike_type):
        super().__init__(vechile_id,brand,rental_price,days)
        self.bike_type=bike_type


    def display_vechiles_details(self):
        print(f"Bike ID: {self.vechile_id}\n Brand: {self.brand}\n Type: {self.bike_type}")

c=Cars(1,"BMW",1000,5,4)
c.display_vechiles_details()
print(f"Rental Cost: {c.calculate_total_rental_cost()}")

b=Bikes(2,"Yamaha",500,4,"Adventure Bike")
b.display_vechiles_details()
print(f"Rental Cost: {b.calculate_total_rental_cost()}")



    

        