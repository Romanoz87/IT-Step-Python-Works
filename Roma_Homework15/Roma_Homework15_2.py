'''2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). კლასს შეუქმენით __eq__ მეთოდი რომელიც შეამოწმებს ორი წიგნის ტოლობას.
ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.


'''

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title.title() == other.title.title() and self.author.title() == other.author.title()  

b1 = Book("idiot", "Fyodor Dostoevsky")
b2 = Book("Idiot", "Fyodor Dostoevsky")
print(b1==b2)