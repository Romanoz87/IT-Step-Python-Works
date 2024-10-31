
'''დავალება 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending).
 დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით.
'''

list1 = list(input("Enter list elements: ").split())  
print(list1)
str1 =  input("Input Ending: ")

filtered_list = list(filter(lambda x: x.endswith(str1), list1))

if len(list1) == 0:
   print("You must enter at least one element to compare")
elif len(filtered_list) == 0:
   print("There is no matching")
else:
  print(f"Words Ending with '{str1}' are: {filtered_list}")

