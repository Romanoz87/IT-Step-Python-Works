''' დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.

Car კლასს დაუმატეთ  თითეული ატრიბუტისთვის set და get თვისებები მათი ცვლილებებისთვის.

დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის მთელი და ა.შ. '''


class Car:
    def __new__(cls, brand, model, year):
        
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
        
    # def __new__(self):
    #     ...

    
    # set new brand name
    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            raise ValueError ("Brand name must contain only letters")
        

    # set new model name   
    def set_model(self, new_model):
       
       self._model = new_model
        

    # Set new year
    def set_year(self, updated_year):
        if isinstance(updated_year, int):
            self._year = updated_year
        else:
            print(f"Invalid year: {updated_year}. It must be an integer.")
  

    # Get full information
    def get(self):
        print(f"Brand: {self._brand}, Model: {self._model}, {self._year} Year")
        

car1 = Car("Mersedes", "C200", 2005)
car1.get()
car1.set_model("E500")
car1.get()
car1.set_year(2001)
car1.set_brand("Audi")
car1.get()