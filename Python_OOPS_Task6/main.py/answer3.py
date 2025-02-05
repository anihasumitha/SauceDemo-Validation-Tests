class Vehicle: #main class
    def __init__(self,model,rental_rate):
        self.model=model
        self.rental_rate=rental_rate
        pass
    
    def calculate_rental(self):
        return self.calculate_rental

class Car(Vehicle): #child class
    def __init__(self, model, rental_rate, no_of_passengers):
        super().__init__(model, rental_rate) #inherits attributes from Vehicle class
        self.__no_of_passengers=no_of_passengers #no of passengers info is private 

    def calculate_rental(self): #calculating rental for car,using inheritance here
        super().calculate_rental() 
        car_rent=self.rental_rate*self.__no_of_passengers
        return car_rent


class Bike(Vehicle): #child class
    def __init__(self, model, rental_rate,hours): #we use hours attribute to calculate rent
        super().__init__(model, rental_rate)
        self.hours=hours

    def calculate_rental(self): #calculating rental for bike, using inheritance here
        super().calculate_rental()
        bike_rent=self.rental_rate*self.hours
        return bike_rent




class Truck(Vehicle): #child class
    def __init__(self, model, rental_rate, days): #using additional attribute,days
        super().__init__(model, rental_rate)
        self.days=days

    def calculate_rental(self): #calculating rental for truck, using inheritance here
        super().calculate_rental()
        truck_rent=self.rental_rate*self.days 
        return truck_rent


#Testing the classes
car=Car("BMW",10000,4) #calculates car rental
print("Car Rent:",car.calculate_rental())

bike=Bike("Electric bike",5000,5)#calculates bike rental
print("Bike Rent:",bike.calculate_rental())

truck=Truck("Ram ProMaster",7000,5) #calculates truck rental
print("Truck Rent:",truck.calculate_rental())



