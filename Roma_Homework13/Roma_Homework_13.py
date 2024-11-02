import os, csv


students =[ 
            [4, 'Nika', 33, 'C', 'Math', 60],
            [11, 'Giorgi', 23, 'A', 'Math', 92],
            [7, 'Dato', 22, 'B', 'Math', 82],
            [9, 'Ana', 28, 'B', 'History', 86],
            [15, 'Nino', 23, 'A', 'Geography', 98],
            [17, 'Merabi', 21, 'C', 'Geography', 68],
            [21, 'Nino', 29, 'A', 'History', 98],
            [12, 'Gela', 41, 'D', 'Geography', 58],
            [13, 'Natia', 25, 'A', 'Math', 98],
            ]
try:
    id1 = int(input("input ID: "))
except ValueError as ex:
    print("Enter Valid Value only numbers for ID")

name = input("input name: ").capitalize()
age = input("input age: ")
grade = input("input grade: ").capitalize()
subject_name = input("subject name: ").capitalize()
mark = input("input mark: ")
  
students_update = [id1, name, age, grade, subject_name, mark]
students.sort(key=lambda x: x[0])

path = "files"
filename = "data3.csv"
os.makedirs(path, exist_ok=True)
filename = os.path.join(path, filename)


def input_data(students_update):                                                                     # 1 ფაილის შექმნა და მონაცემების ჩაწერა
    with open(filename, mode ='w', encoding = 'utf-8', newline="") as file:
        writer1 = csv.writer(file)
        writer1.writerow(['ID', 'name', 'age', 'grade', 'subject_name', 'mark'])
        writer1.writerows(students)
        writer1.writerow(students_update)




def stud_info(filename):
    with open(filename, mode ='r', encoding = 'utf-8', newline="") as file:                              #2 ფაილის წაკითხვა და მონაცემების კონსოლში გამოტანა
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]:<5}{row[1]:<8}{row[2]:<10}{row[3]:<10}{row[4]:<15}{row[5]:<5}")

def file_choose(id):                                                                                          #3 მომხმარებელი ირჩევს კონკრეტულ ID და იღემს მის შესახებ ინფორმაციას
    with open(filename, mode ='r', encoding = 'utf-8', newline="") as file:
        reader = csv.reader(file)    
    
        for row in reader:
            if id == row[0]:
                print(row)

def average_mark(entry):                                                                            #4 ვითვლით საშუალო ქულას კონკრეტულ საგანში
    average = []
    
    with open(filename, mode ='r', encoding = 'utf-8', newline="") as file:
        reader = csv.reader(file)   
        for grade in reader:
            if entry == grade[4]:
                average.append(grade[5])
                average1 = list(map(int, average))
                avg = sum(average1) / len(average1)

    print(f"Average Mark of '{entry}' is {avg} points")
       
            
    

def update(input_id, input_subject,input_new_mark):                                    #5 ??? აქ უნდა განახლდეს მონაცემი ახალი ქულის შეტანისას, მაგრამ ბოლოში ემატება
    with open(filename, mode ='r', encoding = 'utf-8', newline="") as file:
        reader = csv.reader(file) 
    
        for row in reader:
            if input_id == row[0] and input_subject == row[4]:
                row[5] = input_new_mark
                input_data(row)
                    
                break

    




input_data(students_update)
stud_info(filename)

choose_id = input("\nchoose id of student you interested in: ")
file_choose(choose_id)

entry = input("Choose Subject: ").capitalize()

average_mark(entry)

input_id = input("input Id: ")
input_subject = input("input subject: ").capitalize()
input_new_mark = input("enter new mark: ")
update(input_id, input_subject,input_new_mark)

     
    
