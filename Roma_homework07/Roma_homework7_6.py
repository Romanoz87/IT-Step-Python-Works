customers1 = ["Irakli", "Giorgi", "Nona", "Oto"]
customers2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

customers_set1 = set(customers1)  #სია გადაგვყავს სეტ მონაცემთა ტიპში
customers_set2 = set(customers2)
print(customers_set1.intersection(customers_set2))  # გამოაქვს ორივე მონაცემთა საერთო მნიშვნელობა