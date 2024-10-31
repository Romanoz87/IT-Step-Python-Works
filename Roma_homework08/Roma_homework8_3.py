# შეყვანილი რიცხვის ფაქტორიალის გამოთვლა ფუნქციით
def factorial(n):
    sum = 1
    i = 1
    for i in range(n):
        sum = sum * (i + 1)
        i += 1
    return sum

n = int(input("enter Number you want to count factorial: "))
print(f"\nEntered number is '{n}', facrotial is: {factorial(n)}\n")