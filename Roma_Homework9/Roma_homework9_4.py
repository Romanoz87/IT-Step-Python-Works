# დავალება 4. ფუნქციით დავაჯამოთ შეყვანილი რიცხვის ცალკეული ციფრების ჯამი.
def sum_of(number):
    numbers = map(int, list(number))
    return sum(numbers)
#=========================

number = input("Enter Number: ")
print(sum_of(number))
