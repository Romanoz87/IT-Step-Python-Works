'''დავალება 3. ფუნქციით ვქმნით ლოკალურ ცვლადს იგივე დასახელებით რაც აქვს გლობალს 
და გამოგვაქვს ლოკალური მნიშვნელობა'''

def my_func(n):
    gl_str = n + " local"
    return gl_str
#===============================
    
gl_str = "Global"
print(my_func("This is Quote from"))



