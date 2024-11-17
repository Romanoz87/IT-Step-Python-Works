# 4. პითონის Stack.py ფაილში შექმნილია Stack კლასი, დაწერეთ კლასის ფუნქციები (push და pop)

class Stack:
    def __init__(self):
        self.stack = []

    #TODO Use list append method to add element
    def push(self, data):
       self.stack.append(data)

    #TODO Use list pop method to remove element
    def pop(self):
       self.stack.pop()


    def get_info(self):
        print(self.stack)


val1 = Stack()

val1.push(33)
val1.push(55)
val1.push(56)
val1.push(30)
val1.pop()
val1.get_info()
