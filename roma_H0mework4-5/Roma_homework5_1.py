lis1 = []

while True:
    char = input("enter symbol:__")
    if  char == "e":
        print("Exit")
        break
    if char == "a":
        x = input("enter number: ")
        lis1.append(x)
        print(lis1)
    if char == "r" and len(lis1) > 0:
        lis1.pop()
        print(lis1)
    
print("End")