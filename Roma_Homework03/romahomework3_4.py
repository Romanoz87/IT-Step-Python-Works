jami = 0
while True:
    number1 =input("Enter number: ")
    if number1 == "sum":  # რიცხვების შეყვანის დასასრულება და დაჯამება  "sum" სტრიქონით
        print(jami)
        break
    elif int(number1) >= 0:
        jami = jami + int(number1)
    elif int(number1) < 0:
        jami = jami + 0
        
print("End")    