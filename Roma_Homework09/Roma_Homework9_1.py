# დავალება 1.  გლობალურ სიას ფუნქციის გამოძახებით ვამატებთ ელემენტს

def list_append(n):
    
    global int_list
    return  int_list.append(n)
#==============================================
    
int_list = [10,20,30,40]
n = int(input("Enter Element: "))
list_append(n)
print(int_list)