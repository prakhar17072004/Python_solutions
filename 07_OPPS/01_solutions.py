class Car:
    # self is here like this keyword
    def __init__(self,brand,model):
        self.brand = brand
        self.model= model
    def full_name(self):
        return f"{self.brand} {self.model}"

      

my_car = Car("Toyata","Corolla") 
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
