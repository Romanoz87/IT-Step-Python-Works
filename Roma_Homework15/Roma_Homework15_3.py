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
        
   
    
    # set new brand name
    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.isalpha():
            self._brand = new_brand
        else:
            raise ValueError ("Brand name must contain only letters")
    
    #get brand name
    def get_brand(self):
        print(self._brand)
        

    # set new model name   
    def set_model(self, new_model):
       
       self._model = new_model

    # get model name
    def get_model(self):
        print(self._model)
        

    # Set new year
    def set_year(self, updated_year):
        if isinstance(updated_year, int):
            self._year = updated_year
        else:
            print(f"Invalid year: {updated_year}. It must be an integer.")

    #get year
    def get_year(self):
        print(self._year)

    #get full info 
    def get_full_info(self):
        print(f"Brand: {self._brand}, Model: {self._model}, {self._year} Year")



car1 = Car("Mersedes", "C200", 2005)
car1.get_full_info()
car1.set_model("E500")
car1.get_model()
car1.set_year(2001)
car1.set_brand("Audi")
car1.get_brand()
car1.get_full_info()