my_list_1 = [43,'22', 12, 66, 210, ["hi"]]
print("index of 210 is", my_list_1.index(210))  # a. 210-ის ინდექსი
my_list_1.append("hello")                       # b. "hello" დამატება სიის ბოლოს
print(my_list_1)
del my_list_1[2]                               # c. მეორე ინდექსზე მდგომი ელემენტის წაშლა
print(my_list_1)
my_list_2 = my_list_1                         # d.  შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist_1-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

my_list_2.clear()
print(my_list_1)
print(my_list_2)



