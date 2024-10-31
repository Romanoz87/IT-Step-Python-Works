#დავალება 4
num_list = [44, 23, 11, 8, 20, 56, 33, 55]
num1 = int(input("Enter Number: "))
if num_list[2] < num1 and  num1 < num_list[7]:
    print("More than list elements")
elif num1 == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")   

