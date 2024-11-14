''' ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, 
    პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ
    მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა. '''

def count_symbol(str1, symb):
    print(f" The symbol '{symb}' is {str1.count(symb)} times in {str1}\n")


str1 = input("Enter sting...\n") 
symb = input("Enter symbol:...\n")
count_symbol(str1, symb)