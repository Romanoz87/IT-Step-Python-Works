#დავალება 2. ფუნქციას გადავცემთ arr1 სიას და გამოაქვს ელემენტების ჯამი
def arr_sum(*args):
    for i in args:
        return sum(*args)
#====================================================

arr1 = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
print(arr_sum(arr1))