'''შექმენით ორი კლასი:
I. Student, ატრიბუტებით: name, mark, address, სტატიკური ატრიბუტი row_id
II. Address, ატრიბუტებით: city, street


Student კლასის address ატრიბუტს მნიშვნელობად უნდა მიანჭოთ Address კლასის ეგზემპლარი.

შექმენით ორივე კლასის რამდენიმე ეგზემპლარი.

json მოდულის დახმარებით ფაილში შეინახეთ სტუდენტები.

მოახდინეთ წაკითხვა.

შეცვალეთ ატრიბუტ(ებ)ის მნიშვნელობა (მაგ.: mark, str), დაამატეთ ახალი ატრიბუტი grade მნიშვნელობით A, B, C, D (A -> [91-100], B -> [81-90], C -> [71-80], D -> <=70).

შეცვლილი მონაცემები შეინახეთ ფაილში.'''

import json
from json import JSONEncoder


class Student:
    row_id = 1
    def __init__(self, name, mark, address, row_id=1):
        self.row_id = Student.row_id
        
        self.name = name
        self._mark = mark
        self.address = address
        Student.row_id += 1
        
    #getter
    @property
    def mark(self):
        return self._mark
    
    #mark setter
    @mark.setter
    def mark(self, new_mark):
        self._mark = new_mark



class Address(Student):
    def __init__(self, city, street):
        self.city = city
        self._street = street

    #getter
    @property
    def street(self):
        return self._street
    
    #set new street
    @street.setter   
    def street(self, value):
        self._street = value
     

class Encode(JSONEncoder):
    def default(self, o):
        return o.__dict__
    

    
st1 = Student('Nikoloz', 51, Address('Tbilisi', 'Ortachala'))
    
st2 = Student('Giorgi', 88, Address('Tbilisi', 'Didube'))
              
st3 = Student('Davit', 95, Address('Tbilisi', 'Rustaveli ave'))
               
st4 = Student('Nana', 98, Address('Tbilisi', 'Nutsubidze 4 distr'))
               
st5 = Student('Tamari', 72, Address('Tbilisi', 'Digomi'))
           
st6 = Student('Joni', 69, Address('Tbilisi', 'Didube'))



# ქულის შეცვლა setter-ით
st5.mark = 11   

#ქუჩის მისამართის შეცვლა setter-ით
st3.address.street = 'Ponichala'



students = [st1, st2, st3, st4, st5, st6]
                
#ლისტი გადაგვყავს json ფორმატში
json_student = json.dumps(students, cls=Encode, indent=2)


# ვწერთ მონაცემებს json ფაილში
with open('students_data5.json', mode='w', encoding='utf8') as file:              
    json_info1 = json.dump(students, file, cls=Encode, indent=2)


# json ფაილიდან შემოგვაქვს ინფორმაცია, ვცვლით მისამართს და ქულას. ვამატებთ ახალ მნიშვნელობას Grade  სახით
print('-'*100)
print(f"{'N':<4} {'Name':<10} {'mark':<11}{'City':<10}{'Street':<25}{'Grade'}")
print('='*100)

with open('students_data5.json', mode = 'r', encoding='utf-8') as file:
    json_info = json.load(file)

    # ქულის შეცვლა 
    json_info[1]['_mark'] = 12  

    # ქუჩის მისამართის შეცვლა
    json_info[3]['address']['_street'] = 'Digmis Masivi' 


    for stud in json_info:
        
        if stud['_mark'] <= 70:
            value = 'D'
        elif 71 <= stud['_mark'] < 80:
            value = 'C'
        elif 81<= stud['_mark'] < 90:
            value = 'B'
        else:
            value = 'A'
        stud.update({"grade": value})
        print(f"{stud['row_id']:<5}{stud['name']:<10} {stud['_mark']:<10} {stud['address']['city']:<10}{stud['address']['_street']:<25}{stud['grade']}")


# შეცვლილ მონაცემებს ვწერთ json ფაილში
with open('students_data5.json', mode = 'w', encoding='utf-8') as file:
    json.dump(json_info,  file, cls=Encode, indent=2)
  






        


