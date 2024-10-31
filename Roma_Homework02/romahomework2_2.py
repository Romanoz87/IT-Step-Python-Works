#დავალება 2
'''დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. 
თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.
'''
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")