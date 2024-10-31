# დავალება 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს.
 

from functools import reduce
try:
    element = list(map(eval, input("Enter numbers list").split()))
except NameError as name:
    print("\nYou entered wrong type value!!!!!.\n")
except SyntaxError as synt:
    print("\nYou entered special symbol!!!!!!!\n")
except TypeError as typ:
    print("\nWrong type parameter!!!!!!d\n")

elementebis_namravli = reduce(lambda x, y: x * y, element)
print(f" Entered parameters list {element},\n output: {elementebis_namravli}")
