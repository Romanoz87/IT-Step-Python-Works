'''1. შექმენით პითონის კლასი Node რომელსაც ექნება ორი ატრიბუტი (value, next), შემდეგ შექმენით LinkedList კლასი ატრიბუტით head.

2. LinkedList კლასში შექმენით append მეთოდი, რომლის საშუალებითაც ჩაამტებთ სიის ბოლოში ახალ ნოუდს (Node  კლასის ახალ ობიექტს)

3. LinkedList კლასში შექმენით remove მეთოდი, რომლის საშუალებითაც წაშლით სიიდან მის ბოლო ელემენტს(Тail-ს)'''



class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
  

  def append(self, value):
    if self.head is None:    
      self.head = Node(value)
    else:
      current_node = self.head

      while current_node.next:
        current_node = current_node.next
      
      current_node.next = Node(value)
  

  def remove(self):
    if self.head is None:
      raise ValueError("LinkedList is empty...")

    if self.head.next is None:
      self.head = None
    
      return

    current_node = self.head
    while current_node.next.next:
      current_node = current_node.next
    
    current_node.next = None
  

  def view_elemets(self):
    if self.head is None:
      raise ValueError("List is empty...")
    
    current_node = self.head

    while current_node:
      if current_node.next:
        print(current_node.value, end=' -> ')
      else:
        print(current_node.value)

      current_node = current_node.next


# =============
ll1 = LinkedList()

ll1.append(22)
ll1.append(2)
ll1.append(77)
ll1.append(6)
ll1.append(43)
ll1.append(76)
ll1.append(89)
ll1.append(75)

ll1.remove()



ll1.view_elemets()