from datetime import date

class Car:
    counter = 0
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        Car.counter += 1
     
    def car_info(self):
        print(f"Car name-- {self.name} model-- {self.model} {self.year} years model")
    

    def age_of_car(self):
        current_date = date.today()
        current_year = current_date.year
        print("age of car is: ", current_year - self.year, "year")


    def total_cars():
        print("\nWe have total number: ", Car.counter, "of cars")
        


class ElectricCar(Car):
    def __init__(self, name, model, year, battery_life):
        super().__init__(name, model, year)
        
        self.battery_life = battery_life
    
    def battery_info(self):
        print(f"{self.name} {self.model}'s battery life is {self.battery_life} hours")

#=============================================================================================================
    
car1 = Car("Mersedes", "C200", 2009)                                 
car1.car_info()                                                     # გამოაქვს მანქანებზე ინფორმაცია
car1.age_of_car()
car2 = Car("BMW", "M5", 2022)
car2.car_info()
car2.age_of_car()                                                  # ითვლის მანქანის ასაკს 


electric1 = ElectricCar("Tesla", "Model3", 2008, 30 )                  # ელექტრო მანქანების ინფორმაცია
electric1.battery_info()                                               # გამოაქვს ელ მანქანების ელემენტის ხანგრძლივობა
electric1.age_of_car()
electric2 = ElectricCar("Tesla", "Model s", 2005, 30 )
electric2.car_info()

Car.total_cars()                                                        # გამოაქვს მანქანების სრული რაოდენობა
