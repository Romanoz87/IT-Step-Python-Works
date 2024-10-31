''' დავალება 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

'''
list1 = list(map(eval, input("Enter list elements: ").split()))
odd_list = filter(lambda x: x % 2 == 1, list1)
print(*odd_list)