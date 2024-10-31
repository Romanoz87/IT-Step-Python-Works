# guess number 
import random
rand_num = random.randint(0, 100)
i = 1
while True:
    num1 = int(input(f"Enter number. try {i}-th: _ _ "))
    if num1 == rand_num:
        print(f" Congrats!! you guessed number with {i}-th try")
        break
    elif num1 > rand_num:
        print("Too big number. Try agan!!!")
    elif num1 < rand_num:
        print("Too small number. Try again!!!")
    i += 1
print()
print("Game Over")