# დავალება 5: დავაბრუნოთ შეტანილი ტექსტის შებრუნებული ვარიანტი

def reversed_text(n):
    if len(n) == 0:
        return n
    else:
       return  reversed_text(n[1:]) + n[0]
    
#=================================

text = input("Enter some text to reverse:   ")   
print(reversed_text(text))